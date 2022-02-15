import unittest
from datetime import datetime
from flights_planner.BusinessFlight import BusinessFlight
from flights_planner.EconomyFlight import EconomyFlight
from flights_planner.PremiumFlight import PremiumFlight
from flights_planner.FlightRepository import FlightRepository
from flights_planner.Passenger import Passenger


class FlightRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.rep = FlightRepository([])
        self.flight1 = EconomyFlight(0, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 15, 28))
        self.flight2 = BusinessFlight(1, "Warszawa", "Kraków", datetime(2019, 12, 12, 14, 53))
        self.flight3 = BusinessFlight(2, "Paryż", "Nowy Jork", datetime(2019, 12, 12, 9, 14))
        self.flight4 = EconomyFlight(3, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 21, 37))
        self.flight5 = PremiumFlight(4, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 7, 55))
        self.passenger1 = Passenger("Michał", True)
        self.passenger2 = Passenger("Marcin", True)
        self.passenger3 = Passenger("Maciek", True)
        self.passenger4 = Passenger("Milena", True)
        self.passenger5 = Passenger("Michalina", True)
        self.rep.add_flight(self.flight1)
        self.rep.add_flight(self.flight2)
        self.rep.add_flight(self.flight3)
        self.rep.add_flight(self.flight4)
        self.rep.add_flight(self.flight5)

    def test_new_flights(self):
        self.assertListEqual(self.rep.data_source, [self.flight1, self.flight2, self.flight3, self.flight4,
                                                    self.flight5])

    def test_find_flights_cities1(self):
        result = self.rep.find_flights("Gdańsk", "Warszawa", datetime(2019, 12, 12, 6, 00),
                                       datetime(2019, 12, 12, 22, 00), 100)
        self.assertListEqual(result, [self.flight1, self.flight4, self.flight5])

    def test_find_flights_cities2(self):
        result = self.rep.find_flights("Paryż", "Nowy York", datetime(2019, 12, 12, 6, 00),
                                       datetime(2019, 12, 12, 22, 00), 100)
        self.assertListEqual(result, [])

    def test_find_flights_dates1(self):
        result = self.rep.find_flights("Gdańsk", "Warszawa", datetime(2019, 12, 12, 8, 00),
                                       datetime(2019, 12, 12, 22, 00), 100)
        self.assertListEqual(result, [self.flight1, self.flight4])

    def test_find_flights_dates2(self):
        result = self.rep.find_flights("Gdańsk", "Warszawa", datetime(2019, 12, 12, 8, 00),
                                       datetime(2019, 12, 12, 21, 00), 100)
        self.assertListEqual(result, [self.flight1])

    def test_find_flights_price(self):
        result = self.rep.find_flights("Gdańsk", "Warszawa", datetime(2019, 12, 12, 6, 00),
                                       datetime(2019, 12, 12, 22, 00), 55)
        self.assertListEqual(result, [self.flight1, self.flight4])

    def test_find_flights_category_cheapest(self):
        result = self.rep.find_flights("Gdańsk", "Warszawa", datetime(2019, 12, 12, 6, 00),
                                       datetime(2019, 12, 12, 22, 00), 100, "cheapest")
        self.assertEqual(result, self.flight1)

    def test_find_flights_category_fastest(self):
        result = self.rep.find_flights("Gdańsk", "Warszawa", datetime(2019, 12, 12, 6, 00),
                                       datetime(2019, 12, 12, 22, 00), 100, "fastest")
        self.assertEqual(result, self.flight5)

    def test_add_passenger_premium(self):
        self.assertTrue(self.flight5.add_passenger(self.passenger1))

    def test_add_passenger_economy(self):
        self.assertTrue(self.flight2.add_passenger(self.passenger1))

    def test_add_passenger_business(self):
        self.assertTrue(self.flight4.add_passenger(self.passenger1))

    def test_remove_passenger_premium(self):
        self.flight5.add_passenger(self.passenger1)
        self.assertTrue(self.flight5.remove_passenger(self.passenger1))

    def test_remove_passenger_economy(self):
        self.flight2.add_passenger(self.passenger1)
        self.assertFalse(self.flight2.remove_passenger(self.passenger1))

    def test_remove_passenger_business(self):
        self.assertFalse(self.flight4.remove_passenger(self.passenger1))

    def test_find_flights_people(self):
        self.flight5.add_passenger(self.passenger1)
        self.flight5.add_passenger(self.passenger2)
        self.flight5.add_passenger(self.passenger3)
        self.flight5.add_passenger(self.passenger4)
        self.flight5.add_passenger(self.passenger5)
        result = self.rep.find_flights("Gdańsk", "Warszawa", datetime(2019, 12, 12, 6, 00),
                                       datetime(2019, 12, 12, 22, 00), 100)
        self.assertListEqual(result, [self.flight1, self.flight4])
