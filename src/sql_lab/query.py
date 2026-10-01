import os
import logging
import mysql.connector

def get_connection():
    """
    Read environment variables and return a MySQL database connection.
    """
    DBHOST = os.environ.get("DBHOST")
    DBUSER = os.environ.get("DBUSER")
    DBPASS = os.environ.get("DBPASS")
    DBNAME = os.environ.get("DBNAME")
    return mysql.connector.connect(
        host=DBHOST,
        database=DBNAME,
        user=DBUSER,
        password=DBPASS
    )
def get_data_by_group(value):
    """
    Returns all rows where specified value matches filter column group
    """
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM `mock` WHERE `group` = %s"
        cursor.execute(query, (value,))
        results = cursor.fetchall()
        return results
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
def plot_counts(groupby):
    """
    Counts rows per value of provided column, returns list of dictionaries containing category and counts
    """
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = f"SELECT {groupby}, COUNT(*) as count FROM `mock` GROUP BY {groupby}"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
def main():
    data = get_data_by_group("Chronic Illness")
    print('First 3 rows of data for group Chronic Illness')
    for row in data[:3]:
        print(row)
    location_counts = plot_counts('location')
    print('Row counts by location')
    for row in location_counts:
        print(f"Location: {row['location']} | Count: {row['count']}")

if __name__ == "__main__":
    main()