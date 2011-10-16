
import unittest
from test.CommonUnittest import MusicUnittest
from test.CommonUnittest import MainScreenUnittest
from test.CommonUnittest import GameModeUnittest

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(MusicUnittest)
suite.addTests(loader.loadTestsFromModule(MainScreenUnittest))
suite.addTests(loader.loadTestsFromModule(GameModeUnittest))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)