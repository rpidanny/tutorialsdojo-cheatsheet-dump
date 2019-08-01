from tutorialsdojo import TutorialsDojo

def main():
    td = TutorialsDojo()
    for group in td.get_groups():
        print(' [+] {}'.format(group['title']))
        for topic in td.get_topics(group):
            print('    - {} ({})'.format(topic['title'], topic['url']))
            content = td.get_content(topic)
            # print(content)
            td.dump_content(content)
        print('\n')

if __name__ == "__main__":
    main()
