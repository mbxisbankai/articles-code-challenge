# Articles Code Challenge
This project is a simple content management system built using Python and SQLite.

## Developer
Roy Mbui

## Features

- Author and Magazine models with full CRUD functionality
- Articles associated with authors and magazines
- SQL-powered relationship methods
- Transaction-safe article creation

## Setup

1. Clone the repo
```
git clone git@github.com:mbxisbankai/articles-code-challenge.git
```
2. Create and activate a virtual environment
```
pipenv install && pipenv shell
```
3. Install dependencies using `pip install -r requirements.txt` or via Pipenv
```
pipenv install sqlite3
```
4. Initialize the database by running
```
python3 scripts/setup_db.py
```
5. Run this to populate the database with sample data
```
python3 db/seed.py
```

---


