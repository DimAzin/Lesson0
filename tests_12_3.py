import unittest
from tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    is_frozen = True

    def skip_if_frozen(func):
        def func_wrapper(self, *args, **kwargs):
            if self.is_frozen:
                print("Тесты в этом кейсе заморожены")
                return unittest.skip('Тесты в этом кейсе заморожены')
            return func(self, *args, **kwargs)
        return func_wrapper

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            for place, participant in result.items():
                print(f"Место {place}: {participant.name} финишировал")

    @skip_if_frozen
    def test_run_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.assertEqual(result, {1: 'Усэйн', 2: 'Ник'})
        self.__class__.all_results.append(result)

    @skip_if_frozen
    def test_run_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.assertEqual(result, {1: 'Андрей', 2: 'Ник'})
        self.__class__.all_results.append(result)

    @skip_if_frozen
    def test_run_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.assertEqual(result, {1: 'Усэйн', 2: 'Андрей', 3: 'Ник'})
        self.__class__.all_results.append(result)


class RunnerTest(unittest.TestCase):
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

    @skip_if_frozen
    def test_run(self):
        runner_test = Runner("TestRunner2")

        for _ in range(10):
            runner_test.run()

        self.assertEqual(runner_test.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("TestRunner3")
        runner2 = Runner("TestRunner4")

        for _ in range(10):
            runner1.run()

        for _ in range(10):
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)

