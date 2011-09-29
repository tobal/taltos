
import unittest
from test.CommonUnittest import MusicUnittest

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(MusicUnittest)
#suite.addTests(loader.loadTestsFromModule(test_something2))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)