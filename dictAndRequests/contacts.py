contacts = {
    "number":4,
    "students":
        [
            {"name":"Harry Potter", "email":"harry@example.com"},
            {"name":"Hermione Granger", "email":"hermione@example.com"},
            {"name":"Ron Weasley", "email":"ron@example.com"}
        ]
        
}

students = contacts.get('students')
for student in students:
    print(student.get('email'))





