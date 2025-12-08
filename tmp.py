#czas w internecie od 1970 liczony w micros np. sunset, raise w openwether
#openpyxl
#pandas - uzywa opepyxl to robienia xlsa
# format parkwed (l)

# z SQL zrzut:
#
# -- unikalne imiona
# SELECT DISTINCT first_name from employees;
# -- ; kończy wyrażenie - tak bezpiecznie
# SELECT * FROM employees WHERE first_name = "Linda";
# -- wieksze mniejsze
# SELECT * FROM jobs WHERE min_salary >=6000;
# -- laczenie warunków
# SELECT * FROM employees WHERE job_id = 1 AND hire_date >= "2020-01-01";
# -- w sql nie ma matcha , if tylko where
# SELECT * FROM employees WHERE first_name = "Alice" OR job_id = 3;
# -- uproszczony OR - stosuje sie IN !! zaprzeczenie NOT IN
# SELECT * FROM employees WHERE job_id NOT IN (1,2,3,4) ORDER BY department_id ;
# -- NOT moze być też przed where
# -- BETWEEN - wartości pomiędzy
# SELECT * FROM jobs WHERE min_salary BETWEEN 5000 AND 10000;
# -- ZADANKA
# -- 1. Wyświetl wszystkie adresy email pracowników.
# SELECT DISTINCT email FROM employees;
# -- 2. Wyświetl numer id, imię oraz nazwisko wszystkich pracowników.
# SELECT id, first_name, last_name FROM employees;
# -- 3. Wyświetl numer id oraz adres email wszystkich pracowników. Kolumnie id nadaj alias employee_id natomiast kolumnie email nadaj alias private_email.
# SELECT id AS employee_id, email AS private_email FROM employees;
# -- 4. Wyświetl imiona pracowników. Imiona nie mogą się powtarzać.
# SELECT DISTINCT first_name FROM employees;
# -- 5. Pokaż wszystkich pracowników z imieniem Tom
# SELECT * FROM employees WHERE first_name = "TOM";
# -- 6. Pokaż ilu jest pracowników z unikatowymi (bez powtórzeń) imionami oraz zmień nazwę kolumny na number_of_employees.
# SELECT DISTINCT first_name AS number_of_employees FROM employees;
# -- metoda liczenia
# SELECT COUNT(DISTINCT first_name) AS number_of_employees FROM employees;
# -- 7. Pokaż wszystkich pracowników, którzy zostali zatrudnieni od 1 stycznia  2019r.
# SELECT * FROM employees WHERE hire_date > "2019-01-01";
# -- 8. Pokaż wszystkie stanowiska pracy, gdzie płaca minimalna jest mniejsza niż 5000.
# SELECT * FROM jobs WHERE min_salary < 5000;
# -- 9. Pokaż wszystkich pracowników z imieniem Adam oraz nazwiskiem Irwin.
# SELECT * FROM employees WHERE first_name = "Adam" AND last_name = "Spencer";
# -- 10. Pokaż wszystkich pracowników z imieniem Tom lub John.
# SELECT * FROM employees WHERE first_name IN ("Tom", "John");
# -- 11.Wyświetl wszystkich pracowników, którzy posiadają nazwisko Martinez oraz urodzili się po 1 stycznia 1988.
# SELECT * FROM employees WHERE last_name = "Martinez" AND birth_date > "1998-01-01";
# -- 12.Wyświetl wszystkich pracowników, którzy nie pracują w dziale o id 3
# SELECT * FROM employees  WHERE NOT department_id =3;
# -- dodatkowe
# SELECT MAX(birth_date) AS max_val FROM employees;
# -- SELECT * FROM employees WHERE MIN(birth_date); -- zle trzeba przez group by
# -- łączenie rekordów
# SELECT CONCAT(first_name, " ", last_name) AS person FROM employees;
# SELECT * FROM employees LIMIT 5; -- wysyla pięć odpowiedzi, najświeższe
# -- order by, group by
# SELECT * FROM employees ORDER BY hire_date DESC LIMIT 1; -- najnowsza osoba
# SELECT * FROM employees ORDER BY hire_date ASC LIMIT 1; -- najstarsza osoba
# -- LIKE - czyli takie jak % symbolizuje dowolne znaki, _ - oznacza jeden znak (litera, cyfra)
#  -- znajdz rekordy któych first_name kończy się na "a"
# SELECT * FROM employees WHERE first_name LIKE "%a";
# SELECT * FROM employees WHERE email LIKE "%gmail%";
#  -- trzecia litera do r
# SELECT * FROM employees WHERE last_name LIKE "__r%";
# -- Engine DB MySQL - różnice - czym one się różnią?? - poczytać
# -- TRIGERRY jak coś w bazie się zmieni to idzie jakas akcja
