from proto import person_pb2 as person_api
from google.protobuf.json_format import MessageToJson


def run():
    person = person_api.Person()
    person.id = "foo"
    person.name = "bar"
    return MessageToJson(person)


if __name__ == "__main__":
    print("Running demo code...")
    print(run())
