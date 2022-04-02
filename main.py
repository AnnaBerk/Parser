def get_html(url):
    r = requests.get(url)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('div', class_ = 'mb-5').find('h1').text
    return h1
    
def main():
    url = 'https://ru.hexlet.io/'
    print(get_data(get_html(url)))
    

if __name__ == '__main__':
    main()