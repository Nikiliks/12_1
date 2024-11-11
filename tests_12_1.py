import unittest
import runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r1 = runner.Runner('First')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    def test_run(self):
        r1 = runner.Runner('First')
        for i in range(10):
            r1.run()
        self.assertEqual(r1.distance, 100)

    def test_challenge(self):
        r1 = runner.Runner('First')
        r2 = runner.Runner('Second')
        for i in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)

if __name__ == '__main__':
    unittest.main()
