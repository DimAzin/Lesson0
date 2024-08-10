import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner_test = Runner("TestRunner1")

        for _ in range(10):
            runner_test.walk()

        self.assertEqual(runner_test.distance, 50)

    def test_run(self):
        runner_test = Runner("TestRunner2")

        for _ in range(10):
            runner_test.run()

        self.assertEqual(runner_test.distance, 100)

    def test_challenge(self):
        runner1 = Runner("TestRunner3")
        runner2 = Runner("TestRunner4")

        for _ in range(10):
            runner1.run()

        for _ in range(10):
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
