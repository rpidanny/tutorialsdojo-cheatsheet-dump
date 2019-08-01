from tutorialsdojo import TutorialsDojo

def main():
    td = TutorialsDojo()
    for course in td.get_courses():
        print(course)


if __name__ == "__main__":
    main()
