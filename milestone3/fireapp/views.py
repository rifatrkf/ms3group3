from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import pyrebase

# Remember the code we copied from Firebase.
#This can be copied by clicking on the settings icon > project settings, then scroll down in your firebase dashboard
config={
  	"apiKey": "AIzaSyDfrt6PeEWijZn-ynT5G-xxsQ43F30VJBw",
  	"authDomain": "milestone-3-65172.firebaseapp.com",
  	"databaseURL": "https://milestone-3-65172-default-rtdb.asia-southeast1.firebasedatabase.app",
  	"projectId": "milestone-3-65172",
  	"storageBucket": "milestone-3-65172.appspot.com",
  	"messagingSenderId": "425687551292",
  	"appId": "1:425687551292:web:fdb0f616c227af8ea06239",
  	"measurementId": "G-VKXXDV1JWW"
}

#here we are doing firebase authentication
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()


def index(request):
        #accessing our firebase data and storing it in a variable
        motion = database.child('DB object name').child('key1').get().val()
        
    
        context = {
            'motion':motion
        }
        return render(request, 'index.html', context)
