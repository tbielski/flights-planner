from behave import *
from datetime import datetime
from flights_planner.FlightRepository import FlightRepository
from flights_planner.EconomyFlight import EconomyFlight
from flights_planner.BusinessFlight import BusinessFlight
from flights_planner.PremiumFlight import PremiumFlight

use_step_matcher("re")


@given("there is a flights_repository")
def step_impl(context):
    context.repository = FlightRepository([])


@given("there is a business flight")
def step_impl(context):
    context.business_flight = BusinessFlight("0", "Gdańsk", "Warszawa", datetime(2019, 12, 12, 22, 00))


@when("we add a business flight")
def step_impl(context):
    context.repository.add_flight(context.business_flight)


@then("flights_repository1 should have one flight")
def step_impl(context):
    assert context.business_flight.flight_id == "0"
    assert len(context.repository.data_source) == 1
    assert context.repository.data_source[0].flight_id == "0"



@given("there is a economy flight")
def step_impl(context):
    context.economy_flight = EconomyFlight("0", "Gdańsk", "Warszawa", datetime(2019, 12, 12, 22, 00))


@when("we add an economy flight")
def step_impl(context):
    context.repository.add_flight(context.economy_flight)


@then("flights_repository2 should have one flight")
def step_impl(context):
    assert context.economy_flight.flight_id == "0"
    assert len(context.repository.data_source) == 1
    assert context.repository.data_source[0].flight_id == "0"




@given("there is a premium flight")
def step_impl(context):
    context.premium_flight = PremiumFlight("0", "Gdańsk", "Warszawa", datetime(2019, 12, 12, 22, 00))


@when("we add a premium flight")
def step_impl(context):
    context.repository.add_flight(context.premium_flight)


@then("flights_repository3 should have one flight")
def step_impl(context):
    assert context.premium_flight.flight_id == "0"
    assert len(context.repository.data_source) == 1
    assert context.repository.data_source[0].flight_id == "0"
