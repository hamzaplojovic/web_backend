import httpx
from termcolor import colored
import time

test_courses = []

headers = {
    'accept': 'application/json',
}
for x in range(10):
    test_courses.append({ 
    "name": f"string{str(x)}",
    "desc": "string",
    "date": "string"
})

def read_all_items():
    r = httpx.get("https://centarnit.deta.dev/courses/")
    for x in range(len(r.json())):
        print(f"Approved courses: {colored(str(x), 'green')}", end="\r")
        time.sleep(0.1)
    print()


def create_courses():
    for x in test_courses:
        httpx.post("https://centarnit.deta.dev/courses/", json=x, headers=headers)
    return f"Courses created: {colored('status: 200', 'green')}"

def change_courses():
    for x in test_courses:
        x["desc"] = "test"
        httpx.put("https://centarnit.deta.dev/courses/"+x["name"], json=x, headers=headers)
    return f"Courses changed: {colored('status: 200', 'green')}"

def find_courses_by_name():
    for x in test_courses:
        httpx.get("https://centarnit.deta.dev/courses/"+x["name"])
    return f"Courses found: {colored('status: 200', 'green')}"


def delete_courses():
    for x in test_courses:
        httpx.delete("https://centarnit.deta.dev/courses/"+x["name"])
    return f"Courses deleted: {colored('status: 200', 'red')}"


usernames = "\n"+"\n".join([x["name"] for x in test_courses])

def main():
    print(f"Testing for: {colored(usernames, 'green')}")
    print()
    read_all_items()
    print(create_courses())
    print(change_courses())
    print(find_courses_by_name())
    print(delete_courses())
    print()

if __name__ == "__main__":
    main()