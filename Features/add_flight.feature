Feature: Add Flight
  Adding flight to a flights repository.

  Scenario: Add Business flight
    Given there is a flights_repository
    Given there is a business flight
    When we add a business flight
    Then flights_repository1 should have one flight

  Scenario: Add Economy flight
    Given there is a flights_repository
    Given there is a economy flight
    When we add an economy flight
    Then flights_repository2 should have one flight

  Scenario: Add Premium flight
    Given there is a flights_repository
    Given there is a premium flight
    When we add a premium flight
    Then flights_repository3 should have one flight
