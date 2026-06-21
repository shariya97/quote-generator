from flask import Flask, render_template, redirect
import requests
import sqlite3

app = Flask(__name__)


# Create database table
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote TEXT,
            author TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()


# Fetch quote from API
def get_random_quote():
    try:
        url = "https://zenquotes.io/api/random"

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()[0]

            return {
                "quote": data["q"],
                "author": data["a"]
            }

    except Exception as e:
        print("ERROR:", e)

    return None


# Save quote to database
def save_quote(quote, author):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO quotes (quote, author) VALUES (?, ?)",
        (quote, author)
    )

    conn.commit()
    conn.close()


# Get quote history
def get_history():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
    "SELECT quote, author, created_at FROM quotes ORDER BY id DESC LIMIT 5"

    )

    data = cursor.fetchall()
    conn.close()

    return data


# Get total quotes count
def get_total_quotes():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM quotes")

    total = cursor.fetchone()[0]

    conn.close()

    return total


# Clear quote history
def clear_history():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM quotes")

    conn.commit()
    conn.close()


@app.route('/')
def home():
    history = get_history()
    total_quotes = get_total_quotes()

    return render_template(
        'index.html',
        quote=None,
        author=None,
        history=history,
        total_quotes=total_quotes
    )


@app.route('/generate')
def generate():

    result = get_random_quote()

    if result:
        save_quote(
            result['quote'],
            result['author']
        )

        history = get_history()
        total_quotes = get_total_quotes()

        return render_template(
            'index.html',
            quote=result['quote'],
            author=result['author'],
            history=history,
            total_quotes=total_quotes
        )

    return redirect('/')


@app.route('/clear')
def clear():

    clear_history()

    return redirect('/')


if __name__ == '__main__':
    init_db()
    app.run(debug=True)

