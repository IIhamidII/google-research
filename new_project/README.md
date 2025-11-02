# New Project

This project provides a simple command line utility that greets users by name. It serves as an example template for adding new
experiments or utilities to the `google-research` repository.

## Getting Started

Create a virtual environment and install the required dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then run the CLI:

```bash
python -m new_project.main --name="Ada"
```

## Project Structure

- `new_project/`: Python package containing the source code.
  - `__init__.py`: Makes the directory a package.
  - `main.py`: Entry point for the CLI utility.
- `requirements.txt`: Python dependencies for the project.
- `README.md`: Project documentation.

## Testing

Run the unit tests using:

```bash
python -m unittest discover -s new_project/tests
```
