
import yt_dlp

my_url = "https://www.youtube.com/watch?v=ZhODBFQ2-bQ"

if __name__ == '__main__':
    yt_dlp.main(argv=[my_url, "--verbose"])
