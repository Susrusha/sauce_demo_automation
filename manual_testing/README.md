# Manual Testing - SauceDemo

Manual testing of the SauceDemo e-commerce web application (https://www.saucedemo.com/).

## Documents
- [Test Cases and Bug Reports (PDF)](SauceDemo_Test_Cases_and_Bug_Reports.pdf)

## Summary

| Item | Details |
|------|---------|
| Application | SauceDemo (https://www.saucedemo.com/) |
| Total test cases | 18 |
| Passed | 16 |
| Failed | 2 |
| Defects reported | 2 |
| Tester | N Susrusha |

## Test Coverage

| Module | Test Cases |
|--------|-----------|
| Login | 5 (TC_01 - TC_05) |
| Product Listing | 6 (TC_06 - TC_11) |
| Cart | 3 (TC_12 - TC_14) |
| Checkout | 3 (TC_15 - TC_17) |
| Logout | 1 (TC_18) |

## Testing Types
- Functional testing
- Negative testing
- Exploratory testing (with standard_user, locked_out_user, problem_user)

## Defects Found (problem_user)

| Bug ID | Title | Severity | Priority |
|--------|-------|----------|----------|
| BUG_01 | Product images are broken/mismatched | Medium | High |
| BUG_02 | Sorting by Price (Low to High) does not work correctly | Medium | Medium |

## Related
The login test cases (TC_01 - TC_05) are automated in this repository using
Python, Selenium and Pytest with the Page Object Model.