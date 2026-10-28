# BookBot

**A Python command-line tool for analyzing book text and generating word and character frequency statistics.**

BookBot reads a text file, analyzes its contents, and produces a formatted report showing the total word count and the frequency of individual alphabetic characters. This project focuses on text processing, file I/O, data structures, and sorting in Python.

> **Status: Work in Progress**
>
> BookBot is an active learning project. The core text analysis functionality is implemented, and additional features and improvements are planned as development continues.

## Features

- **Word counting** — Calculates the total number of words in a text file.
- **Character frequency analysis** — Counts character occurrences without distinguishing between uppercase and lowercase letters.
- **Frequency-based sorting** — Ranks characters from most frequent to least frequent.
- **Formatted output** — Displays a readable report in the terminal with the source file, word count, and character statistics.
- **Command-line input** — Accepts a file path as an argument, allowing different text files to be analyzed without modifying the source code.

## Roadmap

The following improvements are planned as the project evolves:

- [ ] **Input validation and error handling** — Handle missing files, invalid paths, and other common input errors gracefully.
- [ ] **Improved character filtering** — Make character filtering and reporting behavior more explicit and configurable.
- [ ] **Expanded text statistics** — Explore additional metrics, such as sentence counts, paragraph counts, and average word length.
- [ ] **Automated testing** — Add unit tests to verify word counting, character frequency calculations, sorting, and error handling.
- [ ] **Improved command-line experience** — Provide clearer usage instructions and more helpful feedback when running the program.
- [ ] **Code quality and maintainability** — Continue refining function responsibilities, readability, and overall project structure.

_The roadmap is subject to change as development and learning progress._

## Tech Stack

- **Language:** Python 3
- **Standard library:** `sys` and Python's built-in file I/O
- **Core concepts:** Functions, dictionaries, tuples, lists, string manipulation, file reading, command-line arguments, and custom sorting keys

## Getting Started

### Prerequisites

- Python 3 installed on your system
- A plain-text file to analyze

### Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/Addair89/BookBot.git
cd BookBot
```

### Run BookBot

Pass the path to a text file as a command-line argument:

```bash
python3 main.py books/YOUR_BOOK.txt
```

Replace `YOUR_BOOK.txt` with the name of a text file in the `books` directory.

BookBot will read the file, analyze its contents, and print a report to the terminal.

## Example Output

The following illustrates the report format. The values are examples, not results from a specific book.

```text
============ BOOKBOT ============
Analyzing book found at books/example.txt...
----------- Word Count -----------
Found 12345 total words
--------- Character Count ---------
e: 1200
t: 950
a: 875
o: 800
...
============= END =============
```

## How It Works

BookBot separates its responsibilities into two Python modules.

| Module     | Responsibility                                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------ |
| `main.py`  | Handles command-line arguments, reads the input file, coordinates the analysis, and prints the report. |
| `stats.py` | Implements word counting, character frequency counting, and sorting of character statistics.           |

### Analysis Workflow

1. **Read the input:** Load the contents of the specified book file.
2. **Count words:** Split the text on whitespace and count the resulting words.
3. **Count characters:** Build a dictionary that tracks character frequencies, normalizing character case.
4. **Sort the results:** Convert the frequency data into a sortable collection and order it by count in descending order.
5. **Generate the report:** Print the total word count and the frequency of alphabetic characters.

## What I'm Learning

This project reinforces foundational programming concepts through practical implementation:

- Breaking programs into small, reusable functions with clear responsibilities.
- Reading external files and processing their contents.
- Using dictionaries to aggregate and track frequency data.
- Transforming collections into formats suitable for sorting and reporting.
- Applying custom sorting keys to organize data by specific criteria.
- Working with command-line arguments.
- Separating data processing from presentation to improve code organization.
- Identifying opportunities to improve reliability, maintainability, and error handling.

## Project Background

BookBot was built as part of my [Boot.dev](https://www.boot.dev/) programming education. It is part of my ongoing effort to strengthen my programming fundamentals through hands-on projects.

As I continue developing my software engineering skills, I plan to expand this project while applying the same principles to increasingly complex applications involving backend development, data modeling, APIs, and application logic.

## Author

**Jared Addair**

- GitHub: [@Addair89](https://github.com/Addair89)
- Repository: [BookBot](https://github.com/Addair89/BookBot)
