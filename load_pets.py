import sqlite3

# Connect to the pets database
conn = sqlite3.connect("pets.db")
cursor = conn.cursor()

# Data to insert into the tables
people = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
]

pets = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]

person_pet = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
]

# Insert data into person table
cursor.executemany("INSERT INTO person (id, first_name, last_name, age) VALUES (?, ?, ?, ?)", people)

# Insert data into pet table
cursor.executemany("INSERT INTO pet (id, name, breed, age, dead) VALUES (?, ?, ?, ?, ?)", pets)

# Insert data into person_pet table
cursor.executemany("INSERT INTO person_pet (person_id, pet_id) VALUES (?, ?)", person_pet)

# Commit and close the connection
conn.commit()
conn.close()

print("Data loaded successfully!")

if __name__ == "__main__":
    print("Running load_pets.py")
