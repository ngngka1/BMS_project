import sqlite3

conn = sqlite3.connect('example.db')

def main():
    cursor = conn.cursor()

    # cursor.execute('CREATE TABLE IF NOT EXISTS stocks')

if __name__ == "__main__":
    main()