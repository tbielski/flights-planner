from abc import ABC, abstractmethod


class Flight(ABC):

    def __init__(self, flight_id, price, departure, arrival, date):
        self.__flight_id = flight_id
        self.__passenger_set = set()
        self.__departure = departure
        self.__arrival = arrival
        self.__date = date
        self.__price = price
        self.__capacity = 5

    @property
    def flight_id(self):
        return self.__flight_id

    @property
    def passenger_set(self):
        return self.__passenger_set

    @passenger_set.setter
    def passenger_set(self, value):
        self.__passenger_set = value

    @property
    def departure(self):
        return self.__departure

    @property
    def arrival(self):
        return self.__arrival

    @property
    def date(self):
        return self.__date

    @property
    def price(self):
        return self.__price

    @property
    def capacity(self):
        return self.__capacity

    @abstractmethod
    def add_passenger(self, passenger):
        pass

    @abstractmethod
    def remove_passenger(self, passenger):
        pass
