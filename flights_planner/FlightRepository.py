class FlightRepository:

    def __init__(self, data_source=[]):
        self.__data_source = data_source

    def add_flight(self, flight):
        self.data_source.append(flight)

    def find_flights(self, city1, city2, date1, date2, price, category=None):
        result = []
        cheapest = None
        fastest = None
        for i in self.data_source:
            if len(i.passenger_set) == i.capacity:
                pass
            elif i.departure == city1 and i.arrival == city2 and date1 <= i.date <= date2 and i.price <= price:
                result.append(i)
                if cheapest is None or i.price < cheapest.price:
                    cheapest = i
                if fastest is None or i.date < fastest.date:
                    fastest = i
        if category == "cheapest":
            return cheapest
        elif category == "fastest":
            return fastest
        elif category is None:
            return result

    @property
    def data_source(self):
        return self.__data_source

    @data_source.setter
    def data_source(self, value):
        self.__data_source = value
