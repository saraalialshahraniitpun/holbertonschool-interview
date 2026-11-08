# Making Change

This project contains a solution for the classic change-making problem implemented in Python 3.

## Resources
* [Coin Change Problem - Dynamic Programming](https://en.wikipedia.org/wiki/Change-making_problem)

## Requirements
* Allowed editors: `vi`, `vim`, `emacs`
* All files interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/python3`
* Code should use the `PEP 8` style (version 1.7.x)
* All files must be executable

## Tasks

### 0. Change comes from within
* **File:** `0-making_change.py`
* **Prototype:** `def makeChange(coins, total)`
* **Description:** Determine the fewest number of coins needed to meet a given amount `total`.
  * If `total` is 0 or less, returns `0`.
  * If `total` cannot be met by any number of coins, returns `-1`.
