from bs4 import BeautifulSoup
import requests

# Retrieve and view a webpage using requests
URL = "https://en.wikipedia.org/wiki/List_of_people_killed_for_being_transgender"


def main():
    page = requests.get(URL)
    # print(page.text)

    soup = BeautifulSoup(page.content, "html.parser")
    # print(soup.prettify())
    # exit(0)

    # list comprehension
    scraped_data = [x.get_text() for x in soup.find_all('li') if x.get_text().startswith('19')
                    or x.get_text().startswith('20')]
    for data in scraped_data:
        print(data)


if __name__ == '__main__':
    main()
