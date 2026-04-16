# Local Project Chat Agent

A command-line AI agent for inspecting local software projects with safe built-in tools like `ls`, `cat`, `grep`, `calculate`, and `compact`. It supports both manual slash commands and automatic tool use for common project questions.

![doctests](https://img.shields.io/github/actions/workflow/status/MiaUrosevic/Lab-more-project/doctests.yml?label=doctests)
![integration-tests](https://img.shields.io/github/actions/workflow/status/MiaUrosevic/Lab-more-project/integration-tests.yml?label=integration-tests)
![flake8](https://img.shields.io/github/actions/workflow/status/MiaUrosevic/Lab-more-project/flake8.yml?label=flake8)
![coverage](https://img.shields.io/badge/coverage-91%25-brightgreen)
![pypi](https://img.shields.io/pypi/v/cmc-csci40-mia)

## Demo

![demo](demo.gif)

## Features

- Safe local file inspection with path validation
- Manual slash commands such as `/ls`, `/cat`, `/grep`, `/calculate`, and `/compact`
- Automatic tool routing for common file and arithmetic questions
- One-shot CLI usage
- `--debug` support for showing tool calls
- `--provider` support
- Doctests, integration tests, flake8, and coverage reporting

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python chat.py
python chat.py "what is 2 + 2?"
python chat.py --debug "what files are in the .github folder?"
python chat.py --provider groq "show me README.md"
```

## Example: Webscraping Project
This example is good because it shows the agent answering a high-level question about a real project directory.

```bash
$ cd test_projects/webpage_project
$ python ../../chat.py "what is this project about?"
```

## Example: Markdown Compiler
This example is good because it shows the agent inspecting implementation details across source files.

```bash
$ cd test_projects/markdown_compiler
$ python ../../chat.py "find def in *.py"
```

## Example: Mia.Urosevic.github.io
This example is good because it shows the agent reading and summarizing project files in a realistic scraping codebase.

```bash
$ cd test_projects/webscraping_project
$ python ../../chat.py "show me README.md"
```

---

# Step 4: save the file

Press:

```text
Cmd + S
