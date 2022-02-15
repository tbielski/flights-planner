from behave import *
from datetime import datetime
from flights_planner.FlightRepository import FlightRepository
from flights_planner.EconomyFlight import EconomyFlight
from flights_planner.BusinessFlight import BusinessFlight
from flights_planner.PremiumFlight import PremiumFlight
from flights_planner.Passenger import Passenger

use_step_matcher("re")


@given("there is a filled flights repository1")
def step_impl(context):
    context.flight1 = EconomyFlight(0, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 15, 28))
    context.flight2 = BusinessFlight(1, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 21, 37))
    context.flight3 = PremiumFlight(2, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 7, 55))
    context.repository = FlightRepository([context.flight1, context.flight2, context.flight3])


@when("we search for cheapest flight")
def step_impl(context):
    context.result = context.repository.find_flights("Gdańsk", "Warszawa", datetime(2019, 12, 12, 6, 00),
                                                     datetime(2019, 12, 12, 22, 00), 100, "cheapest")


@then("find_flights return one cheapest flight")
def step_impl(context):
    assert context.result == context.flight1


@given("there is a filled flights repository2")
def step_impl(context):
    context.flight1 = EconomyFlight(0, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 15, 28))
    context.flight2 = BusinessFlight(1, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 21, 37))
    context.flight3 = PremiumFlight(2, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 7, 55))
    context.repository = FlightRepository([context.flight1, context.flight2, context.flight3])


@when("we search for fastest flight")
def step_impl(context):
    context.result = context.repository.find_flights("Gdańsk", "Warszawa", datetime(2019, 12, 12, 6, 00),
                                                     datetime(2019, 12, 12, 22, 00), 100, "fastest")


@then("find_flights return one fastest flight")
def step_impl(context):
    assert context.result == context.flight3


@given("there is a filled flights repository3")
def step_impl(context):
    context.flight1 = EconomyFlight(0, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 15, 28))
    context.flight2 = BusinessFlight(1, "Warszawa", "Kraków", datetime(2019, 12, 12, 21, 37))
    context.flight3 = PremiumFlight(2, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 7, 55))
    context.repository = FlightRepository([context.flight1, context.flight2, context.flight3])


@when("we search for flights between cities")
def step_impl(context):
    context.result = context.repository.find_flights("Gdańsk", "Warszawa", datetime(2019, 12, 12, 6, 00),
                                                     datetime(2019, 12, 12, 22, 00), 100)


@then("find_flights return array of flights between these cities")
def step_impl(context):
    assert context.result == [context.flight1, context.flight3]


@given("there is a filled flights repository4")
def step_impl(context):
    context.flight1 = EconomyFlight(0, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 15, 28))
    context.flight2 = BusinessFlight(1, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 21, 37))
    context.flight3 = PremiumFlight(2, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 7, 55))
    context.repository = FlightRepository([context.flight1, context.flight2, context.flight3])


@when("we search for flight between dates")
def step_impl(context):
    context.result = context.repository.find_flights("Gdańsk", "Warszawa", datetime(2019, 12, 12, 8, 00),
                                                     datetime(2019, 12, 12, 22, 00), 100)


@then("find_flights return array of flights between dates")
def step_impl(context):
    assert context.result == [context.flight1, context.flight2]


@given("there is a filled flights repository5")
def step_impl(context):
    context.flight1 = EconomyFlight(0, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 15, 28))
    context.flight2 = BusinessFlight(1, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 21, 37))
    context.flight3 = PremiumFlight(2, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 7, 55))
    context.repository = FlightRepository([context.flight1, context.flight2, context.flight3])


@when("we search for flights below price")
def step_impl(context):
    context.result = context.repository.find_flights("Gdańsk", "Warszawa", datetime(2019, 12, 12, 6, 00),
                                                     datetime(2019, 12, 12, 22, 00), 70)


@then("find_flights return array of flights below price")
def step_impl(context):
    assert context.result == [context.flight1]


@given("there is a filled flights repository with passengers")
def step_impl(context):
    context.passenger1 = Passenger("Michał", True)
    context.passenger2 = Passenger("Marcin", True)
    context.passenger3 = Passenger("Maciek", True)
    context.passenger4 = Passenger("Milena", True)
    context.passenger5 = Passenger("Michalina", True)
    context.flight1 = EconomyFlight(0, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 15, 28))
    context.flight2 = BusinessFlight(1, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 21, 37))
    context.flight3 = PremiumFlight(2, "Gdańsk", "Warszawa", datetime(2019, 12, 12, 7, 55))
    context.flight1.add_passenger(context.passenger1)
    context.flight1.add_passenger(context.passenger2)
    context.flight1.add_passenger(context.passenger3)
    context.flight1.add_passenger(context.passenger4)
    context.flight1.add_passenger(context.passenger5)
    context.repository = FlightRepository([context.flight1, context.flight2, context.flight3])


@when("we search for flights with available places")
def step_impl(context):
    context.result = context.repository.find_flights("Gdańsk", "Warszawa", datetime(2019, 12, 12, 6, 00),
                                                     datetime(2019, 12, 12, 22, 00), 100)


@then("find_flights return array of flights with available places")
def step_impl(context):
    assert context.result == [context.flight2, context.flight3]
