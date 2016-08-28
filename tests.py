
"""Site manager. Runs tests and server from CLI."""

import unittest


def test():
    """Run unit tests."""
    tests = unittest.TestLoader().discover('tests', pattern='*.py')
    unittest.TextTestRunner(verbosity=1).run(tests)

if __name__ == "__main__":
    test()
