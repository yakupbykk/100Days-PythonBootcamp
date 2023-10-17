import pytube

url=input("Video URL'sini giriniz: ")
path = ""

pytube.YouTube(url).streams.get_highest_resolution().download(path)

