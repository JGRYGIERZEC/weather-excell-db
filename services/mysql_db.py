# mysql connector jest archiwalny - do skrytpów jest lepszy, sqlalchemy (z dto) jest b. zaawansowany, wraz z interfacami i klasami
# mysql lekki i szybki

import mysql.connector
from mysql.connector import Error

def create_record(data):
    try:
        conn = mysql.connector.connect(
            host="localhost", # lub "127.0.0.1",
            user="root",
            password="test",
            database="weather_db"
        )
        if not conn.is_connected():
            raise Error("Nie połączono")

        cursor = conn.cursor(dictionary=True) # z poziomu kursora wykonuje się selekty, jak bez True to będą tuple w odpowiedzi, lepiej bo nie trzeba indexowac
        # sql = """CREATE TABLE weather_db ("""

        sql = """
            INSERT INTO records
            (temp, temp_feels_like, pressure, weather_desc, clouds, place, wind, created)
            VALUES (%s, %s, %s, %s, %s, %s, %s, NOW());
            """

        variables = (
            data['temp'],
            data['temp_feels_like'],
            data['pressure'],
            data['description'],
            data['clouds'],
            data['place'],
            data['wind'],

        )

        cursor.execute(sql, variables)
        # results = cursor.fetchall() # wrzucanie zapytania do zmiennej
        conn.commit()
        print("Zapisanie do MYSQL")
        # return results


    except Error as e:
        print(e)

    finally:
        conn.close()
        cursor.close()
        # zamykanie bazy - zeby nie zamulala z niezamknietymi polczeniami

# data = get_employees()
# for x in data:
#     print(f"{x.get("first_name")} {x.get("last_name")}")

# create_record()

def get_record():
    try:
        conn = mysql.connector.connect(
            host="localhost", # lub "127.0.0.1",
            user="root",
            password="test",
            database="weather_db"
        )
        if not conn.is_connected():
            raise Error("Nie połączono")

        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM records ORDER BY created DESC LIMIT 10")
        result = cursor.fetchall()
        return result

    except Error as e:
        print(e)
    finally:
        conn.close()
        cursor.close()

# data = get_employees()
