import requests, bs4
s = requests.Session()

def search_by_oclc():
    oclc = str(input('Enter your OCLC number:'))
    cat = s.get("https://catalog.lib.unc.edu/?utf8=%E2%9C%93&option=catalog&op=AND&all_fields=&title=&author=&subject=&publisher=&series_statement=&isbn_issn={0}&range%5Bpublication_year_isort%5D%5Bbegin%5D=&range%5Bpublication_year_isort%5D%5Bend%5D=&sort=score+desc%2C+publication_year_isort+desc%2C+title_sort_ssort_single+asc&search_field=advanced&commit=Search".format(oclc))
    catSoup = bs4.BeautifulSoup(cat.text,'html.parser')

    try:
        elem = catSoup.select('.item-availability-misc')
        status = elem[0].getText()
        print(status)
    except IndexError:
        try:
            elem = catSoup.select('.item-available')
            status = elem[0].getText()
            print(status)
        except IndexError:
            try:
                elem = catSoup.select('.item-not-available')
                status = elem[0].getText()
                print(status)
            except IndexError:
                print('item not found')

cont = ''
while cont == '':
    search_by_oclc()
    cont = input('search again? ')







