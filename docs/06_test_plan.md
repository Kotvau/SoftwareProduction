# TEST PLAN – RoomLight Prototype CLI

## Scope

- Configuration deploy to groups<+
- Validating user input
- Exiting the program

## Environment

- VSCode terminal (Windows / bash)
- Python 3.12

## Method

Start the program and go through all menu options manually.

## Results

Test results are recorded in:
`docs/TEST_RESULTS.md` (Pass/Fail per test case)

---

## Test Cases

| REQ       | Requirement                                                | Test Case | Title & Steps                                                                                                             |
| --------- | ---------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------- |
| SW Design | Start the program                                          | TEST 001  | Program starts and shows menu correctly                                                                                   |
| REQ-7     | Monitoring that shows saved and deployed lighting settings | TEST 002  | Show lights (1) <br>• Lights are listed correctly                                                                         |
| REQ-7     |                                                            | TEST 003  | Show setups (2) <br>• Light name, lumen, and temperature are shown                                                        |
| REQ-7     |                                                            | TEST 004  | Show groups (3) <br>• All existing groups are shown with their lights                                                     |
| REQ-1     | User can configure different lighting configurations       | TEST 005  | Create config (4) <br>• New configuration is saved <br>• Empty input is not accepted                                      |
| REQ-2     | User can group configurations with rooms/areas             | TEST 006  | Create new group (5) <br>• New group exists after creation <br>• Lights are moved to new group and removed from old group |
| REQ-2     |                                                            | TEST 007  | Assign config to group (6) <br>• Selected configuration is assigned to chosen light group                                 |
| REQ-3     | User can centrally sync configurations to every room       | TEST 008  | Deploy (7) <br>• All lights in the chosen group are deployed                                                              |
| REQ-3     | User can centrally sync configurations to every room       | TEST 009  | Global config (8) <br>• All lights are moved to GLOBAL group <br>• Configuration is applied to all lights                 |
| SW Design | Exit the program                                           | TEST 010  | Exit (0) <br>• Program shuts down correctly                                                                               |

---

## Notes

- All tests are executed manually via CLI menu navigation.
- Input validation must reject empty or invalid entries.
- Group and configuration changes must persist correctly during runtime.
