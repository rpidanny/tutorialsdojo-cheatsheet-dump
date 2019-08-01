from tutorialsdojo import TutorialsDojo

def main():
    td = TutorialsDojo()
    # for group in td.get_groups():
    #     print(' [+] {}'.format(group['title']))
    #     for topic in td.get_topics(group):
    #         print('    - {} ({})'.format(topic['title'], topic['url']))
    #     print('\n')

    print(td.get_content({'url': 'https://tutorialsdojo.com/aws-billing-and-cost-management/'}))

if __name__ == "__main__":
    main()
