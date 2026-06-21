# Quote Generator Hub

A Flask-based web application that fetches random inspirational quotes from an external API and stores them in a SQLite database for viewing quote history.

## Features

* Generate random quotes using the ZenQuotes API
* Display quote author and content
* Store generated quotes in SQLite database
* View recent quote history
* Track total number of quotes generated
* Clear quote history
* Responsive and modern user interface
* Built using Flask, HTML, CSS, and SQLite

## Technologies Used

* Python
* Flask
* SQLite
* Requests
* HTML5
* CSS3
* ZenQuotes API

## Project Structure

quote-generator/

├── app.py

├── database.db

├── requirements.txt

├── README.md

├── static/

│   └── style.css

└── templates/

```
└── index.html
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/shariya97/quote-generator.git
```

2. Navigate to the project folder

```bash
cd quote-generator
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
python app.py
```

5. Open your browser and visit

```text
http://127.0.0.1:5000
```

## How It Works

1. User clicks the "Generate New Quote" button.
2. Flask sends a request to the ZenQuotes API.
3. A random quote is returned.
4. The quote is displayed on the webpage.
5. The quote is saved to the SQLite database.
6. The quote history section updates automatically.

## API Used

ZenQuotes API

https://zenquotes.io/

## Future Improvements

* Search quotes by author
* Favorite quotes feature
* Export quote history
* User authentication
* Dark/Light theme toggle

## Author

Shariya



