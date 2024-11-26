import sqlite3


def main():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # cursor.execute('CREATE TABLE IF NOT EXISTS stocks')

if __name__ == "__main__":
    main()