class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    instances = [Person(p["name"], p["age"]) for p in people]

    for person_dict in people:
        person_instance = Person.people[person_dict["name"]]

        wife = person_dict.get("wife")
        husband = person_dict.get("husband")

        if wife:
            person_instance.wife = Person.people[wife]
        if husband:
            person_instance.husband = Person.people[husband]

    return instances
