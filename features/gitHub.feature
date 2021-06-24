# Created by vy at 6/23/2021
Feature: GitHub API validation
  # Enter feature description here

  Scenario: Session management check
    Given I have gitHub auth credentials
    When I hit getRepo API of gitHub
    Then status code of response should be 200
