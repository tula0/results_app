import falcon
from .images import Resource #import the Resources class we just created.
import .images2

api= application= falcon.API()#create a WSGI app and aliases it as api.
#theoretically, this callable app can be hosted in any web server that understands WSGI

images= Resource()#it seems the images are returned
api.add_route('/images',images)

images2= images2.Resource() #images to serverd as msgpack type
api.add_route('/images2',images2)

#--------------------------------------------------------Starting  a Server------------------------------------------
#so in the folder where app.py and images.py are contained, start a server e.g
#Before that, do "pip install waitress" ,"pip install httpie", "npm install http-server"
#On the cmd do either:  $http-server or waitress-serve --port=8000 look:app


#On another terminal try querying the running server
#$http localhost:8000/images or curl -v localhost:8000 ##this gives a 200 OK message and json-encoded images resource
#$http localhost:8000/images2 for the msgpack type of images
