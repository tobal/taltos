
import unittest
from test.CommonUnittest import MusicUnittest
from test.CommonUnittest import MainScreenUnittest

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(MusicUnittest)
suite.addTests(loader.loadTestsFromModule(MainScreenUnittest))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)