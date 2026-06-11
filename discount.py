def calculate_discount(previous_total, current_total=0):
    if previous_total + current_total >= 50000000:
        return 0.1
    return 0