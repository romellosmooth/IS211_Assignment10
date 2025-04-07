import sqlite3

# Connect to the pets database
def query_pets():
    conn = sqlite3.connect("pets.db")
    cursor = conn.cursor()

    while True:
        person_id = input("Enter a person's ID (or -1 to exit): ")

        if person_id == '-1':
            print("Exiting program.")
            break

        cursor.execute("SELECT * FROM person WHERE id = ?", (person_id,))
        person = cursor.fetchone()

        if person:
            first_name, last_name, age = person[1], person[2], person[3]
            print(f"{first_name} {last_name}, {age} years old")

            cursor.execute("""
                SELECT pet.name, pet.breed, pet.age, pet.dead 
                FROM pet 
                JOIN person_pet ON pet.id = person_pet.pet_id 
                WHERE person_pet.person_id = ?
            """, (person_id,))

            pets = cursor.fetchall()

            for pet in pets:
                name, breed, age, dead = pet
                status = "alive" if dead == 0 else "dead"
                print(f"{first_name} owned {name}, a {breed} that was {age} years old and is {status}.")
        else:
            print("No person found with that ID.")

    conn.close()

if __name__ == "__main__":
    query_pets()

if __name__ == "__main__":
    print("Running query_pets.py")
