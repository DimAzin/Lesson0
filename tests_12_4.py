import unittest, logging
from runner import Runner

logging.basicConfig(filename='runner_tests.log', level=logging.INFO, filemode='w', format='%(levelname)s: %(message)s', encoding='utf-8')

class RunnerTest1(unittest.TestCase):
    is_frozen = False

    def skip_if_frozen(func):
        def func_wrapper(self, *args, **kwargs):
            if self.is_frozen:
                print("Тесты в этом кейсе заморожены")
                return unittest.skip('Тесты в этом кейсе заморожены')
            return func(self, *args, **kwargs)
        return func_wrapper

    @skip_if_frozen
    def test_walk(self):
        runner_test = Runner("TestRunner1")

        for _ in range(10):
            runner_test.walk()

        self.assertEqual(runner_test.distance, 50)
        logging.info('"test_walk1" выполнен успешно')

    @skip_if_frozen
    def test_run(self):
        runner_test = Runner("TestRunner2")

        for _ in range(10):
            runner_test.run()

        self.assertEqual(runner_test.distance, 100)
        logging.info('"test_run1" выполнен успешно')

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("TestRunner3")
        runner2 = Runner("TestRunner4")

        for _ in range(10):
            runner1.run()

        for _ in range(10):
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)

class RunnerTest2(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("TestRunner5", -5)
            runner.walk()
            logging.info('"test_walk2" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(12345, 5)
            runner.run()
            logging.info('"test_run2" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")


if __name__ == '__main__':
    unittest.main()
