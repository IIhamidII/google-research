"""Unit tests for the new project CLI."""

import unittest

from new_project import main


class MainTest(unittest.TestCase):

  def test_greet_with_valid_name(self):
    self.assertEqual(main.greet("Ada"), "Hello, Ada!")

  def test_greet_strips_whitespace(self):
    self.assertEqual(main.greet("  Alan  "), "Hello, Alan!")

  def test_greet_rejects_empty_name(self):
    with self.assertRaises(ValueError):
      main.greet("   ")


if __name__ == "__main__":
  unittest.main()
