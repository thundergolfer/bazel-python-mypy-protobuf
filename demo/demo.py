from proto import person_pb2 as person_api  # type: ignore
from google.protobuf.json_format import MessageToJson
from typing import Union

Person = Union[person_api.Person]


def greet_person(person: Person):
    print(f"Hello {person.name}")


def build_person() -> Person:
    person = person_api.Person()
    person.id = "foo"
    person.name = "bar"
    return person


def run():
    person = build_person()
    greet_person(person)
    return MessageToJson(person)


if __name__ == "__main__":
    print("Running demo code...")
    print(run())
