def fibonacci(number):
    if number < 0:
        raise ValueError("number must be non-negative")
    if number == 0:
        return 0
    if number == 1:
        return 1

    previous = 0
    current = 1

    for _ in range(2, number + 1):
        previous, current = current, previous + current

    return current


if __name__ == "__main__":
    target = 10
    print(f"F({target}) =", fibonacci(target))
