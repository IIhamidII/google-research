"""Command line entry point for the new project."""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
  """Creates the argument parser for the CLI."""
  parser = argparse.ArgumentParser(
      description="Greet a user by name from the new project CLI.")
  parser.add_argument(
      "--name",
      required=True,
      help=(
          "Name of the person to greet. For example, use `--name=\"Ada\"` "
          "to print `Hello, Ada!`."))
  return parser


def greet(name: str) -> str:
  """Generates a greeting for the provided name."""
  normalized = name.strip()
  if not normalized:
    raise ValueError("Name must contain at least one non-space character.")
  return f"Hello, {normalized}!"


def main(argv: list[str] | None = None) -> None:
  """Runs the CLI."""
  parser = build_parser()
  args = parser.parse_args(argv)
  message = greet(args.name)
  print(message)


if __name__ == "__main__":
  main()
