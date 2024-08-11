import unittest
from tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):

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

    def test_run_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.assertEqual(result, {1: 'Усэйн', 2: 'Ник'})
        self.__class__.all_results.append(result)

    def test_run_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.assertEqual(result, {1: 'Андрей', 2: 'Ник'})
        self.__class__.all_results.append(result)

    def test_run_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.assertEqual(result, {1: 'Усэйн', 2: 'Андрей', 3: 'Ник'})
        self.__class__.all_results.append(result)

if __name__ == '__main__':
    unittest.main()
