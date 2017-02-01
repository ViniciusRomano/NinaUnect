import pyrebase
import datetime
from timeNow import timeNow


config = {
        "apiKey": "AIzaSyA3CiBvheT0KHWed8u-p9PSe7NkdUdZOuU",
        "authDomain": "ejnina-bc361.firebaseapp.com",
        "databaseURL": "https://ejnina-bc361.firebaseio.com/",
        "storageBucket": "ejnina-bc361.appspot.com",
        "serviceAccount": "/home/romano/Downloads/ejNina-873cd10167de.json"
    }

class CrudNina(object):

    def __init__(self):
        #authenticate a user
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        self.user = auth.sign_in_with_email_and_password("vidromano@hotmail.com", "senha123")
        self.db = firebase.database()

    def push(self,ra,state):
        data = {}
        data['LocalTime']=str(datetime.datetime.now().strftime(" %d %b %Y %H:%M:%S ")) #format time : ' 01 Feb 2017 13:52:26'
        data['OnlineTime'] = str(timeNow().getTime().split('-')[0])
        data['State']=state

        self.db.child(str(ra)).push(data, self.user['idToken'])

    def getAll(self):
        return self.db.get(self.user['idToken']).val()
