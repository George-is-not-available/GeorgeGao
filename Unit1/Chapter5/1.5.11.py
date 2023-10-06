import time
import sys

def dynamic_progress_bar(iterations, delay):
    for i in range(iterations + 1):
        progress = i / iterations
        bar_length = 40
        bar = '*' * int(bar_length * progress)
        spaces = ' ' * (bar_length - len(bar))
        sys.stdout.write(f'\r[{bar}{spaces}] {int(progress * 100)}%')
        sys.stdout.flush()
        time.sleep(delay)

try:
    total_iterations = 100
    delay = 1

    dynamic_progress_bar(total_iterations, delay)
    print("\nProgress complete!")

