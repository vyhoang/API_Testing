# Created by vy at 6/17/2021
Feature: Verify if Books are added and deleted using Library API
  # Enter feature description here

  @library
  Scenario: Verify AddBook API functionality
    Given the book details which need to be added to library
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And status code of response should be 200

  @library
  Scenario Outline: Verify AddBook API functionality
    Given the book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then book is successfully added
      Examples:
        |isbn | aisle |
        | cceadd| 011001122  |
        | efeafe| 01100233  |
