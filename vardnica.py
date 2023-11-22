names = [
    {
        "name": "Anna",
        "class": "10a",
        "grade": 9
    },
    {
        "name":"Oskars",
        "class": "10c",
        "grade": 10
    }
]

for student in names:
    print(f"{student['name']} ({student['class']}) {student['grade']}")
