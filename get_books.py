import requests



def main():
    search_word = 'docker'
    url = 'https://allitebooks.com?s={}'.format(search_word)
    get_html(url)




def get_html(url):
    try:
        user_agent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        }
        r = requests.get(url=url, headers=user_agent)
        print(r.text)
    except:
        print(r.status_code)



if __name__ == '__main__':
    main()