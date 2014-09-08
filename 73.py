

class CD:
    def __init__(self):
        pass


class cdplayer:
    def __init__(self,playlist=None,cd=None):
        self.palylist=playlist
        self.cd=cd

    def paly(self,song):
        pass

class JukeBox:
    def __init__(self,player,cds,user,ts):
        self.cdplayer=player
        self.cds=cds
        self.user=user
        self.ts=ts

class TrackSelector:
    def __init__(self,s):
        self.song=s

    def getCurrentSone(self):
        return song




