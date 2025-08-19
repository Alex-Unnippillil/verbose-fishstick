"""Command line interface for verbose-fishstick."""

import argparse
from .calculator import add, subtract


def main(argv: list[str] | None = None) -> None:
    """Run the CLI."""
    parser = argparse.ArgumentParser(description="Simple calculator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_add = subparsers.add_parser("add", help="Add two numbers")
    parser_add.add_argument("a", type=float, help="First number")
    parser_add.add_argument("b", type=float, help="Second number")

    parser_sub = subparsers.add_parser("subtract", help="Subtract two numbers")
    parser_sub.add_argument("a", type=float, help="First number")
    parser_sub.add_argument("b", type=float, help="Second number")

    args = parser.parse_args(argv)

    if args.command == "add":
        result = add(args.a, args.b)
    elif args.command == "subtract":
        result = subtract(args.a, args.b)
    else:
        parser.error("Unknown command")
        return

    print(result)


if __name__ == "__main__":  # pragma: no cover
    main()
