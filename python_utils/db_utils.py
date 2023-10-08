import sqlite3


# Create a class for managing SQLite database connections
class SQLiteConnection:
    def __init__(self, db_path):
        # Initialize the class with the path to the SQLite database file
        self.db_path = db_path
        self.connection = None  # Initialize connection to None
        self.cursor = None  # Initialize cursor to None

    # Define a context manager method for entering a 'with' block
    def __enter__(self):
        try:
            # Attempt to connect to the SQLite database using the provided path
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()  # Create a cursor for executing SQL queries
            return self.cursor  # Return the cursor to be used within the 'with' block

        except sqlite3.Error as e:
            print(f"Error connecting to SQLite database: {e}")
            return None

    # Define a context manager method for exiting a 'with' block
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # If an exception occurred within the 'with' block, print an error message
            print(f'an error occurred: {exc_val}')
            self.connection.rollback()  # Rollback any uncommitted changes in case of an error
        else:
            self.connection.commit()  # Commit the changes if no exception occurred

        self.cursor.close()  # Close the cursor
        self.connection.close()  # Close the database connection
