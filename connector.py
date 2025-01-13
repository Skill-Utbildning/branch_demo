import psycopg2

def connect_to_db():
    try:
        connection = psycopg2.connect(
            user="your_username",
            password="your_password",
            host="localhost",
            port="5433",
            database="your_database"
        )
        print("Connection to database established successfully")
        return connection
    except Exception as error:
        print(f"Error connecting to database: {error}")
        return None

# Example usage
if __name__ == "__main__":
    conn = connect_to_db()
    if conn:
        conn.close()