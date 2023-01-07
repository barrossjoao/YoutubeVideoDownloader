from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Ocorreu um erro ao baixar o vídeo")
    print("Download completo!")


link = input("Coloque o link do vídeo: ")
Download(link)