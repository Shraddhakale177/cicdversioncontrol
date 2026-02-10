
"""Simple CLI for the demo Python app"""


def greet(name: str) -> str:
    """Return a friendly greeting message."""
    return f"Hello, {name}! This app proves the CI/CD flow works."


def main() -> None:
    """Run the app via CLI arguments."""
    import argparse

    parser = argparse.ArgumentParser(description="Run the greeting app.")
    parser.add_argument("name", nargs="?", default="developer", help="The person to greet.")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
