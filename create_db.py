import sqlite3

# Connect to SQlite
connection=sqlite3.connect("travel_database.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

# Create Customers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone_number TEXT
    )
''')

# Create Flights table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS flights (
        flight_id INTEGER PRIMARY KEY,
        flight_number TEXT UNIQUE NOT NULL,
        departure_city TEXT NOT NULL,
        arrival_city TEXT NOT NULL
    )
''')

# Create Tours table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tours (
        tour_id INTEGER PRIMARY KEY,
        tour_name TEXT NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL
    )
''')

# Create Luggage table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS luggage (
        luggage_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        flight_id INTEGER,
        tour_id INTEGER,
        weight REAL NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (flight_id) REFERENCES flights(flight_id),
        FOREIGN KEY (tour_id) REFERENCES tours(tour_id)
    )
''')

# Insert data into Customers table
customer_data = [
    ('Alice Johnson', 'alice.johnson@email.com', '555-123-4567'),
    ('Bob Williams', 'bob.williams@email.com', '444-987-6543'),
    ('Eva Davis', 'eva.davis@email.com', '111-222-3333'),
    ('Mike Wilson', 'mike.wilson@email.com', '999-888-7777'),
    ('Sophie Turner', 'sophie.turner@email.com', '333-666-9999'),
    ('David Lee', 'david.lee@email.com', '777-555-1111'),
    ('Grace Miller', 'grace.miller@email.com', '222-444-8888'),
    ('Tom Parker', 'tom.parker@email.com', '123-789-4561'),
    ('Olivia White', 'olivia.white@email.com', '987-654-3211'),
    ('Daniel Brown', 'daniel.brown@email.com', '555-000-1111'),
]
cursor.executemany('INSERT INTO customers (name, email, phone_number) VALUES (?, ?, ?)', customer_data)

# Insert data into Flights table
flight_data = [
    ('FL789', 'CityE', 'CityF'),
    ('FL101', 'CityG', 'CityH'),
    ('FL202', 'CityI', 'CityJ'),
    ('FL303', 'CityK', 'CityL'),
    ('FL404', 'CityM', 'CityN'),
    ('FL505', 'CityO', 'CityP'),
    ('FL606', 'CityQ', 'CityR'),
    ('FL707', 'CityS', 'CityT'),
    ('FL808', 'CityU', 'CityV'),
    ('FL909', 'CityW', 'CityX'),
]
cursor.executemany('INSERT INTO flights (flight_number, departure_city, arrival_city) VALUES (?, ?, ?)', flight_data)

# Insert data into Tours table
tour_data = [
    ('Spring Adventure', '2024-04-01', '2024-04-15'),
    ('Autumn Retreat', '2024-10-01', '2024-10-15'),
    ('City Exploration', '2024-06-01', '2024-06-10'),
    ('Beach Getaway', '2024-08-01', '2024-08-10'),
    ('Mountain Expedition', '2024-09-01', '2024-09-15'),
    ('Cruise Experience', '2025-02-01', '2025-02-15'),
    ('Historical Journey', '2025-05-01', '2025-05-10'),
    ('Festival Celebration', '2025-07-01', '2025-07-10'),
    ('Wildlife Safari', '2025-11-01', '2025-11-15'),
    ('Luxury Retreat', '2025-12-01', '2025-12-10'),
]
cursor.executemany('INSERT INTO tours (tour_name, start_date, end_date) VALUES (?, ?, ?)', tour_data)

# Insert data into Luggage table
luggage_data = [
    (3, 3, 3, 18.0),
    (4, 4, 4, 25.8),
    (5, 5, 5, 12.5),
    (6, 6, 6, 30.2),
    (7, 7, 7, 14.7),
    (8, 8, 8, 22.1),
    (9, 9, 9, 16.5),
    (10, 10, 10, 19.3),
    (1, 2, 3, 23.6),
    (3, 5, 7, 17.2),
]
cursor.executemany('INSERT INTO luggage (customer_id, flight_id, tour_id, weight) VALUES (?, ?, ?, ?)', luggage_data)

# Display all the tables

print("The inserted data: ")

print("Customer table data: ")
data=cursor.execute('''Select * from customers''')
for row in data:
    print(row)

print("flights table data: ")
data=cursor.execute('''Select * from flights''')
for row in data:
    print(row)

print("tours table data: ")
data=cursor.execute('''Select * from tours''')
for row in data:
    print(row)

print("luggage table data: ")
data=cursor.execute('''Select * from luggage''')
for row in data:
    print(row)



# Commit and then close db
connection.commit()
connection.close()

print("Database created and populated successfully.")