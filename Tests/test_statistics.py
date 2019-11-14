import unittest
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from Calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/StatsData.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_Pop_Mean_calculator(self):
        test_mean_data = CsvReader('Tests/Data/StatsData.csv').data
        answer = CsvReader('Tests/Data/StataDataAns.csv').data
        dataset = []
        for row in test_mean_data:
            a = int(row['PopData'])
            dataset.append(a)
        for column in answer:
            result = float((column['Mean']))
        self.assertEqual(self.statistics.mean(dataset), result)



    def test_Mode_calculator(self):
        test_mode_data = CsvReader('Tests/Data/StatsData.csv').data
        answer = CsvReader('Tests/Data/StataDataAns.csv').data
        dataset = []
        for row in test_mode_data:
            x = int(row['PopData'])
            dataset.append(x)
        for column in answer:
            result = float(column['Mode'])
        self.assertEqual(self.statistics.mode(dataset), result)



    def test_Median_calculator(self):
        test_median_data = CsvReader('Tests/Data/StatsData.csv').data
        answer = CsvReader('Tests/Data/StataDataAns.csv').data
        dataset = []
        for row in test_median_data:
            x = int(row['PopData'])
            dataset.append(x)
        for column in answer:
            result = float(column['Median'])
        self.assertEqual(self.statistics.median(dataset), result)

    def test_popstddev_calculator(self):
        test_popstd_data = CsvReader('Tests/Data/StatsData.csv').data
        answer = CsvReader('Tests/Data/StataDataAns.csv').data
        dataset = []
        for row in test_popstd_data:
            x = int(row['PopData'])
            dataset.append(x)
        for column in answer:
            result = float(column['Pop_Std'])
        self.assertEqual(self.statistics.pop_stddev(dataset), result)



if __name__ == '__main__':
    unittest.main()