from flights_planner.Flight import Flight


class BusinessFlight(Flight):

    def __init__(self, flight_id, departure, arrival, date):
        super().__init__(flight_id, 75, departure, arrival, date)

    def add_passenger(self, passenger):
        number_of_passengers = len(self.passenger_set)
        if passenger.vip:
            self.passenger_set.add(passenger)
        return len(self.passenger_set) == number_of_passengers + 1

    def remove_passenger(self, passenger):
        return False
