# 0x08. N Queens

This project is part of the Software Engineering curriculum at **Holberton School**. It solves the classic **N Queens puzzle** using the **Backtracking** algorithm in Python.

---

## 🎯 Description
The N queens puzzle is the challenge of placing $N$ non-attacking queens on an $N \times N$ chessboard. This program finds and prints all possible unique configurations/solutions for a given $N$.

---

## ⚙️ Requirements & Constraints
- **Language:** Python 3 (version 3.8.5+)
- **Allowed Module:** Only `sys` is allowed.
- **Error Handling:**
  - Wrong number of arguments $\rightarrow$ `Usage: nqueens N` (Exit status 1)
  - $N$ is not an integer $\rightarrow$ `N must be a number` (Exit status 1)
  - $N$ is less than 4 $\rightarrow$ `N must be at least 4` (Exit status 1)

---

## 🚀 Usage & Execution
Make the file executable and run it from the command line:

```bash
chmod +x 0-nqueens.py
./0-nqueens.py 4
