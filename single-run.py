import random

def run_trial(num_prisoners=100):
    # Create a random permutation of boxes
    boxes = list(range(1, num_prisoners + 1))
    random.shuffle(boxes)

    # Each prisoner follows the cycle strategy
    for prisoner in range(1, num_prisoners + 1):
        current_box = prisoner
        found = False

        for _ in range(num_prisoners // 2):
            number = boxes[current_box - 1]  # boxes are 0-indexed

            if number == prisoner:
                found = True
                break

            current_box = number

        if not found:
            return False  # At least one prisoner failed

    return True  # All prisoners succeeded


def simulate(trials=10_000):
    successes = 0

    for _ in range(trials):
        if run_trial():
            successes += 1

    probability = successes / trials
    return probability


if __name__ == "__main__":
    trials = 50_000
    probability = simulate(trials)
    print(f"Estimated success probability: {probability:.4f}")

    