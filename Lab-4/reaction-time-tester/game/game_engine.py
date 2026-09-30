import pygame
from .round import Round
from .sounds import Sounds

# Game Engine

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (90, 90, 90)
GREEN = (40, 180, 90)
BLUE = (50, 90, 170)
RED = (190, 50, 50)
DARK = (30, 34, 48)

# key -> (name, rounds, min_wait_ms, max_wait_ms)
DIFFICULTIES = {
    pygame.K_1: ("Easy", 3, 1000, 2000),
    pygame.K_2: ("Medium", 5, 1000, 3000),
    pygame.K_3: ("Hard", 7, 500, 5000),
}

class GameEngine:
    def __init__(self, width, height, rounds_total=5, min_wait_ms=1000, max_wait_ms=3000):
        self.width = width
        self.height = height

        self.result_pause_ms = 800  # brief pause on the result screen between rounds
        self.false_start_pause_ms = 1200

        self.font = pygame.font.SysFont("Arial", 30)
        self.small_font = pygame.font.SysFont("Arial", 22)
        self.big_font = pygame.font.SysFont("Arial", 46)
        self.sounds = Sounds()
        self.quit_requested = False

        self.difficulty = "Medium"
        self.start_session(rounds_total, min_wait_ms, max_wait_ms)

    def start_session(self, rounds_total, min_wait_ms, max_wait_ms):
        self.rounds_total = rounds_total
        self.min_wait_ms = min_wait_ms
        self.max_wait_ms = max_wait_ms
        self.reaction_times = []
        self.false_starts = 0
        self.result_shown_at = None
        self.game_over = False
        self.round = Round(self.min_wait_ms, self.max_wait_ms)

    def handle_event(self, event):
        if self.game_over:
            self._handle_results_input(event)
            return
        is_click = event.type == pygame.MOUSEBUTTONDOWN
        is_space = event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE
        if (is_click or is_space) and self.round.state in ("waiting", "go"):
            reaction_ms = self.round.register_input()
            if reaction_ms is None:
                self.false_starts += 1
                self.sounds.play("false_start")
            else:
                self.reaction_times.append(reaction_ms)
            self.result_shown_at = pygame.time.get_ticks()

    def _handle_results_input(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key in DIFFICULTIES:
            name, rounds, lo, hi = DIFFICULTIES[event.key]
            self.difficulty = name
            self.start_session(rounds, lo, hi)
        elif event.key in (pygame.K_ESCAPE, pygame.K_q):
            self.quit_requested = True

    def handle_input(self):
        # Reserved for continuously-held-key input; every action here
        # is a discrete click/keypress, handled in handle_event.
        pass

    def update(self):
        if self.game_over:
            return

        was_waiting = self.round.state == "waiting"
        self.round.update()
        if was_waiting and self.round.state == "go":
            self.sounds.play("go")

        now = pygame.time.get_ticks()
        if self.round.state == "result":
            if now - self.result_shown_at >= self.result_pause_ms:
                self._start_next_round()
        elif self.round.state == "false_start":
            # A false start does not use up a round; the round is replayed.
            if now - self.result_shown_at >= self.false_start_pause_ms:
                self.round = Round(self.min_wait_ms, self.max_wait_ms)

    def _start_next_round(self):
        if len(self.reaction_times) >= self.rounds_total:
            self.game_over = True
            self.sounds.play("session_end")
            return
        self.round = Round(self.min_wait_ms, self.max_wait_ms)

    def average_reaction_ms(self):
        if not self.reaction_times:
            return 0
        return round(sum(self.reaction_times) / len(self.reaction_times))

    def render(self, screen):
        if self.game_over:
            self._render_results(screen)
            return

        if self.round.state == "waiting":
            bg = GRAY
            message = "Wait for green..."
        elif self.round.state == "go":
            bg = GREEN
            message = "Click now!"
        elif self.round.state == "false_start":
            bg = RED
            message = "Too soon! False start"
        else:
            bg = BLUE
            message = f"{self.round.reaction_ms} ms"

        screen.fill(bg)

        text_surf = self.big_font.render(message, True, WHITE)
        text_rect = text_surf.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(text_surf, text_rect)

        round_num = min(len(self.reaction_times) + 1, self.rounds_total)
        round_text = self.font.render(f"Round {round_num}/{self.rounds_total}", True, WHITE)
        screen.blit(round_text, (10, 10))

        avg_text = self.font.render(f"Avg: {self.average_reaction_ms()} ms", True, WHITE)
        screen.blit(avg_text, (self.width - 190, 10))

        info = self.small_font.render(f"{self.difficulty}  |  False starts: {self.false_starts}", True, WHITE)
        screen.blit(info, (10, self.height - 34))

    def _render_results(self, screen):
        screen.fill(DARK)
        title = self.big_font.render("Session complete!", True, WHITE)
        screen.blit(title, title.get_rect(center=(self.width // 2, 40)))

        y = 85
        for i, ms in enumerate(self.reaction_times, start=1):
            line = self.small_font.render(f"Round {i}: {ms} ms", True, WHITE)
            screen.blit(line, line.get_rect(center=(self.width // 2, y)))
            y += 24

        summary = self.font.render(
            f"Average: {self.average_reaction_ms()} ms   False starts: {self.false_starts}", True, GREEN)
        screen.blit(summary, summary.get_rect(center=(self.width // 2, y + 18)))

        hint = self.small_font.render("Play again:  1 = Easy   2 = Medium   3 = Hard", True, WHITE)
        exit_hint = self.small_font.render("Esc = Exit", True, WHITE)
        screen.blit(hint, hint.get_rect(center=(self.width // 2, self.height - 50)))
        screen.blit(exit_hint, exit_hint.get_rect(center=(self.width // 2, self.height - 22)))
