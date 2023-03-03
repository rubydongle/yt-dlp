import urllib
import urllib.request, urllib.error
from bs4 import BeautifulSoup

site_url = "https://supersimple.com/super-simple-songs/"
head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
    "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
}


# 得到指定一个URL的网页内容
def get_html(url):
    request = urllib.request.Request(url, headers=head)
    html_content = ""
    try:
        response = urllib.request.urlopen(request)
        html_content = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html_content


songs = []


def build_song_info(song_url):
    return []

def get_youtube_link(song_url):
    html = get_html(song_url)
    # print(html)
    bs = BeautifulSoup(html, 'html.parser')
    youtube_iframe_link = bs.find('div', class_='videoWrapper').find('iframe')#.find('link', rel='canonical')
    # print(youtube_iframe_link['src'])
    # print('=====')

    html2 = get_html(youtube_iframe_link['src'])
    bbs = BeautifulSoup(html2, 'html.parser')
    youtube_link = bbs.find('head').find('link', rel="canonical")
    print(youtube_link['href'])
    print('=====')
    return youtube_link['href']
    # print(len(youtube_lkink))
    # for l in youtube_link:
    #     print(l)
    # for a_link in youtube_link:
    #     print(a_link['href'])


def build_songs_info():
    html = get_html(site_url)
    bs = BeautifulSoup(html, 'html.parser')
    contents = bs.find_all('ul', class_='all-songs')
    for link in contents[0].find_all('li'):
        # print(link)
        title = link.find('span').get_text()
        image = link.find('img')['src']
        site = link.find('a')['href']
        # print(f"title is: {link.find('span').get_text()}")
        # print(f"image is: {link.find('img')['src']}")
        # print(f"link is: {link.find('a')['href']}")
        # build_song_info(site)
        youtube_link = get_youtube_link(site)
        songs.append({'title': title, 'image': image, 'site': site, 'youtube_link': youtube_link})
        # print('=======')


if __name__ == '__main__':
    build_songs_info()
    # build_song_info(songs[0]['site'])
    print(songs)
