#!/usr/bin/env python3
import functools
import time

def retry(max_attempts: int, delay: float = 1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {str(e)}")
                    if attempt == max_attempts - 1:
                        raise
                        time.sleep(delay)
        return wrapper
    return decorator


@retry(max_attempts=3, delay=0.5)
def error_function():
    print("Attempting function...")
    raise ValueError("Random error occurred")


def main():
    try:
        error_function()
    except ValueError as e:
        print(f"Function failed after all attempts: {e}")


if __name__ == "__main__":
    main()
