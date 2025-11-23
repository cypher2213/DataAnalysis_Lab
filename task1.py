import pandas as pd

students = {
    "Vitaly_Prikhodko": ["вул. Шевченка 1", 11, [10,12,2,5]],
    "Dmytro_Kropyvnytskyi": ["вул. Лесі Українки 3", 8, [10,2,5,7,8,11]],
    "Mikhail_Romanenko": ["вул. Франка 7", 7, [11,2,5,7,8,9]],
    "Maxim_Derizemlya": ["вул. Грушевського 2", 6, [9,2,3,5,]],
    "Victoria_Zhuk": ["вул. Центральна 4", 9, [10,11,12,12,12,12,12]],
    "Andrey_Kuryanov": ["вул. Садова 9", 5, [10,10,10,10]],
    "Oksana_Dubovets": ["вул. Вишнева 6", 7, [11,11,12,2,5,12]],
    "Nikita_Stroganov": ["вул. Миру 8", 6, [5,5,6,7,8,12]],
    "Karina_Nikolaenko": ["вул. Квіткова 10", 2, [2,2,2,2,2]],
    "Eugenia_Dron": ["вул. Коцюбинського 5", 10, [4,5,7,8,12]],
    "Artem_Polishchuk": ["вул. Березова 11", 8, [6,7,8,12,12]],
    "Iryna_Savchenko": ["вул. Молодіжна 14", 9, [5,7,8,4,3,2,6]],
    "Bohdan_Kryvonos": ["вул. Паркова 3", 11, [12,12,12,12,12]],
    "Sofia_Melnyk": ["вул. Сонячна 12", 9, [12,12,12,2,2,2,12]],
    "Oleksandr_Tymchuk": ["вул. Дніпровська 22", 3, [2,2,2,2,2]]
}

#=============================================DATASET TRANSFORM==========================================

df = pd.DataFrame.from_dict(students,orient="index",columns=["adress","course","grades"]) # перевод словника у датасет
df = df.reset_index().rename(columns={"index": "name"}) # додавання колонки "name"

print("=" *50)
print(df.head(3))
print("=" *50)
print(df.dtypes)
print("=" *50)
print(df.shape)
print("=" *50)
print(df.describe())

#=====================================STUDENTS SORTING=============================================================

df["average_grade"] = df["grades"].apply(lambda g: round(sum(g) / len(g))) # розраховуємо середній грейд студентів

#======================================GOOD STUDENTS===================================
print("="*100, "GOOD STUDENTS","="*100)
good_students = df[df["average_grade"] > 7] # визначаємо студентів які добре навчаються 
print(good_students)


#======================================SORTED BY NAME STUDENTS===================================
print("="*100, "SORTED BY NAME STUDENTS","="*100)
sorted_students = good_students.sort_values(by="name") # сортуємо студентів за ім'ям
print(sorted_students)

#======================================MIDDLESCHOOLERS===================================
print("="*100, "MIDDLESCHOOLERS","="*100)
middleschool_student = sorted_students[sorted_students["course"] < 10] # визначаємо учня середніх класів серед відсортованих
print(middleschool_student) 