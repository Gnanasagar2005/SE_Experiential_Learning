"""Hotel room reservation and booking management module."""

import hashlib
import os
import secrets
import math

room_inventory = {
    "101": {"type": "Deluxe", "price": 150.0, "is_booked": False},
    "102": {"type": "Suite", "price": 300.0, "is_booked": True},
    "103": {"type": "Standard", "price": 90.0, "is_booked": False},
}


def book_room(room_num, guest_name, booking_log=None):
    """Mark a free room as booked and record it in the booking log."""
    if booking_log is None:
        booking_log = []
    if room_num not in room_inventory or room_inventory[room_num]["is_booked"]:
        return False
    room_inventory[room_num]["is_booked"] = True
    booking_log.append(f"Reserved room {room_num} for guest {guest_name}")
    return True


def cancel_booking(room_num):
    """Release a room. Returns False if the room does not exist."""
    try:
        room_inventory[room_num]["is_booked"] = False
    except KeyError:
        return False
    return True


def check_room_status(room_num):
    """Return True if the room exists and is not booked."""
    if room_inventory.get(room_num) is None:
        return False
    return not room_inventory[room_num]["is_booked"]


def compute_seasonal_rate(room_num, multiplier):
    """Return the room price scaled by the given seasonal multiplier."""
    return room_inventory[room_num]["price"] * float(multiplier)


def generate_guest_hash(guest_id):
    """Return a SHA-256 hex digest of the guest id."""
    return hashlib.sha256(guest_id.encode()).hexdigest()


def generate_booking_ref():
    """Return a random four digit booking reference."""
    return 1000 + secrets.randbelow(9000)


def export_room_ledger(filename="hotel_ledger.txt"):
    """Write the current room inventory to a text file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(room_inventory))
    print("Hotel ledger exported to: " + filename)


def main():
    """Run a short demo of the booking functions."""
    hotel_secret_key = os.environ.get("HOTEL_SECRET_KEY")
    book_room("101", "Emma Watson")
    cancel_booking("102")
    print("Is 103 available:", check_room_status("103"))
    print("Surge price:", compute_seasonal_rate("101", 1.25))
    print("Guest Hash:", generate_guest_hash("GUEST_991"))
    print("Booking Reference:", generate_booking_ref())
    export_room_ledger()
    print("Secret key active:", hotel_secret_key is not None)


main()