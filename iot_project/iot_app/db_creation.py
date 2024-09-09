# from sqlalchemy import create_engine
# from  models import Base, DeviceEvent  # replace 'your_module_name' with the actual module name

# # Create an SQLite engine
# engine = create_engine('sqlite:///iot_data.db')

# # Create all tables in the engine. This is equivalent to "makemigrations" and "migrate" in Django.
# Base.metadata.create_all(engine)

# from sqlalchemy import inspect

# inspector = inspect(engine)
# print(inspector.get_table_names())

# from sqlalchemy import create_engine

# engine = create_engine('sqlite:///iot_data.db')
# connection = engine.connect()

# result = connection.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = result.fetchall()

# print(tables)  # This should include 'device_events'
# connection.close()
from sqlalchemy import create_engine, text

# Create an engine to connect to the SQLite database
engine = create_engine('sqlite:///iot_data.db')

# Establish a connection
connection = engine.connect()

# Use the text() function to wrap your raw SQL query
result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))

# Fetch and print the results
tables = result.fetchall()
print(tables)  # This should include 'device_events'

# Close the connection
connection.close()
