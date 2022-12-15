import unittest as ut
from lab32 import *


class TestCalculator(ut.TestCase):

    def setUp(self):
        self.cash_calculator = CashCL('RUB', 1000, '2022-10-21')
        self.cash_calculator.add_record(Rec(30,'Заправка BP', '2021-10-21'))
        self.cash_calculator.add_record(Rec(300,'Поездака в Нижний Новгород', ''))
        self.cash_calculator.add_record(Rec(300,'Поездака в Кисловодск', '2022-10-21'))
        self.cash_calculator.add_record(Rec(10,'Покупка хлеба ',  '2022-10-21'))


    def test_get_today_stat(self):
        self.assertEqual(self.cash_calculator.get_today_stat(), 300)

    def test_last_seven_days_stat(self):
        self.assertEqual(self.cash_calculator.last_sevendays_stat(), 640)

    def test_curr_date_count(self):
        self.assertEqual(self.cash_calculator.curr_date_count(), 310)

    def test_get_today_cash_remained(self):
        self.assertEqual(self.cash_calculator.get_today_cash_remained(), 'На сегодня осталось 700 RUB')