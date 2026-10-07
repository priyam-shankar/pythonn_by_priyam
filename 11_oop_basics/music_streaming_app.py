class song:
    total_songs = 0
    
    def __init__(self,title,artist,duration):
        self.title = title          #instance attributes
        self.artist = artist
        self.duration = duration
        song.total_songs += 1
    
    def show_info(self):
        print(f"{self.title} by {self.artist} - {self.duration}")  
          
    @classmethod
    def get_total_songs(cls):
        print(f"Total songs on platform = {cls.total_songs}")
        
    @staticmethod
    def convert_to_seconds(duration):
        minutes = int(duration)
        seconds = int((duration - minutes) * 100)
        print(f"{duration} minutes = {minutes * 60 + seconds} seconds")

s1 = song("Blinding Lights","The Weeknd",3.20)
s2 = song("Shape of You","Ed Sheeran",3.53)
s3 = song("Believer","Imagine Dragons",3.24)
s4 = song("Perfect","Ed Sheeran",4.23)

s3.show_info()
song.get_total_songs()
song.convert_to_seconds(s3.duration)
    