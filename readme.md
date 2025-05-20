# 🧪 Fuzzy Element Symbol Matcher

This Python script attempts to match a user-provided word to a sequence of **chemical element symbols** (like `He`, `Li`, `O`, etc.), even if the match is imperfect. It uses a **recursive backtracking** algorithm with a configurable tolerance for spelling mismatches.

---

## 🔍 How It Works

Given an input word (e.g. `hello`), the script will:

1. Convert it to lowercase.
2. Search for substrings that match element symbols (like `h`, `he`, `li`, etc.).
3. Allow a specified number of character mismatches (`max_mismatches`).
4. Return the best possible combination of element symbols that reconstructs the word, partially or fully.

### Example

Enter a word: `unicorn`

**Output:**
Closest match found (2 letters off):
UCoRn
Elements: U (Uranium), Co (Cobalt), Rn (Radon)
Unmatched letters: ni

---

## ⚙️ Configuration

You can change the allowed number of character mismatches in the `fuzzy_spell()` function by modifying the `max_mismatches` parameter:

```python
result = fuzzy_spell(word, max_mismatches=2)
```
### 🧠 Features
Complete list of 118 periodic table elements 
Case-insensitive matching
Supports fuzzy spelling with customizable mismatch tolerance
Highlights unmatched characters

### 🛠️ Requirements
**Python 3.x**


### 🚀 Clone the repository
```bash
git clone github.com/Chaose3/Periodic_Table.git
```
### Change directory
```bash
cd Periodic Table
```
### Run the script
```bash
python fuzzy_elements.py
```
Enter a word and see if it can be constructed from element symbols!


### 🧪 Potential Use Cases
```
Educational chemistry games

Science-themed puzzles

Chemistry name generators

Nerdy Easter eggs 🧠
```
### 📜 License
This project is open-source and free to use under the MIT License.

