import math


def _to_number(value):
    try:
        number = float(value.strip())
    except (ValueError, AttributeError):
        return None
    if not math.isfinite(number) or number < 0:
        return None
    return number


def parse_claim(text):
    if not isinstance(text, str):
        return None
    parts = text.split(':')
    if len(parts) != 2:
        return None
    plan = parts[0].strip()
    months = _to_number(parts[1])
    if not plan or months is None:
        return None
    return plan.title(), months


def age_average(ages_csv):
    if not isinstance(ages_csv, str) or not ages_csv.strip():
        return None
    values = []
    for item in ages_csv.split(','):
        item = item.strip()
        if not item.isascii() or not item.isdigit():
            return None
        values.append(int(item))
    return round(sum(values) / len(values), 2)


def payable_charge(text):
    if not isinstance(text, str):
        return None
    parts = text.split('|')
    if len(parts) != 2:
        return None
    charge = _to_number(parts[0])
    discount = _to_number(parts[1])
    if charge is None or discount is None:
        return None
    total = charge * 1.18 - discount
    if not math.isfinite(total):
        return None
    return round(max(total, 0), 2)


def show(label, result, hint):
    if result is None:
        print(f"Invalid input. Expected format: {hint}")
    else:
        print(label, result)


def main():
    print("==== Running parse_claim ====")
    user_input = input("Enter plan:age in months (e.g. standard:30): ")
    show("Plan and Age:", parse_claim(user_input), "plan:months")

    print("\n==== Running age_average ====")
    user_input = input("Enter product ages as CSV (e.g. 12,24,36): ")
    show("Average Age:", age_average(user_input), "comma separated whole numbers")

    print("\n==== Running payable_charge ====")
    user_input = input("Enter charge|discount (e.g. 1500|200): ")
    show("Payable Charge:", payable_charge(user_input), "charge|discount")


if __name__ == "__main__":
    main()
