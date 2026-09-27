# Changelog

## [1.0.0] - Initial Release
- Basic menu-driven calculator: Add, Subtract, Multiply, Divide, Power, Modulus.
- Known issues (found during testing, see test case sheet):
  - Dividing by zero crashes the program (unhandled ZeroDivisionError).
  - Entering non-numeric input crashes the program (unhandled ValueError).

## [2.0.0] - Bug Fix Release
- Fixed: Division by zero now shows a friendly error message instead of crashing.
- Fixed: Non-numeric input now shows a friendly error message and re-prompts instead of crashing.
- Improved: Input validation loop for numbers.
- All regression + new test cases passing (see Calculator_Test_Cases.xlsx).
