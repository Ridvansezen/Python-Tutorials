class Mp3Player:
    def __init__(self, extension, file_size):
        self.extension = extension
        self.file_size = file_size
        
    def play(self):
        print("Şarkı başlatıldı")
        
    def pause(self):
        print("Şarkı durduruldu.")
        
        
mp3 = Mp3Player(".mp3", "3 mb")
mp3.play()
mp3.pause()