
import unittest
from test.CommonUnittest import MusicUnittest
from test.CommonUnittest import MainScreenUnittest
from test.CommonUnittest import GameModeUnittest
from test.CommonUnittest import ConstantsUnittest

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(MusicUnittest)
suite.addTests(loader.loadTestsFromModule(MainScreenUnittest))
suite.addTests(loader.loadTestsFromModule(GameModeUnittest))
suite.addTests(loader.loadTestsFromModule(ConstantsUnittest))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)