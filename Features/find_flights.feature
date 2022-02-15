Feature: Find Flights
  Finding flights by parameters.

  Scenario: Find cheapest flight
    Given there is a filled flights repository1
    When we search for cheapest flight
    Then find_flights return one cheapest flight

  Scenario: Find fastest flight
    Given there is a filled flights repository2
    When we search for fastest flight
    Then find_flights return one fastest flight

  Scenario: Find flights between cities
    Given there is a filled flights repository3
    When we search for flights between cities
    Then find_flights return array of flights between these cities

  Scenario: Find flights between dates
    Given there is a filled flights repository4
    When we search for flight between dates
    Then find_flights return array of flights between dates

  Scenario: Find flights below price
    Given there is a filled flights repository5
    When we search for flights below price
    Then find_flights return array of flights below price

  Scenario: Find flights with available places
    Given there is a filled flights repository with passengers
    When we search for flights with available places
    Then find_flights return array of flights with available places
