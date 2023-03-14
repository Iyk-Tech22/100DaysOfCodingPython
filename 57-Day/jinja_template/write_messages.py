from jinja2 import Environment, FileSystemLoader

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine",  "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
    {"name": "Fritz", "score": 40},
    {"name": "Sirius", "score": 75},
]

environ = Environment(loader=FileSystemLoader("templates/"))

template = environ.get_template("message.html")

for student in students:
    filename = f"message_{student['name']}.txt"
    content = template.render(
            student,
            test_name=test_name,
            max_score=max_score
    )
    
    with open(filename, "w") as messager:
        messager.write(content)
        print(f"...wrote message to {student['name']}")

# JINJA WITH HTML TEMPLATES
template = environ.get_template("message.html")
context = {
    "students":students,
    "test_name":test_name,
    "max_score":max_score
}

with open("result_message.html", "w") as result:
    result.write(template.render(context))
    print("...wrote message to html file")


