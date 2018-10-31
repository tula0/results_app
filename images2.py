#this is the same thing as images.py except that it uses MessagePack as the encoding for media types
import msgpack
iport falcon
class Resource(object):
    def on_get(self,req,resp):
        doc={
            'images2':[
                {
                'href':'/images/1eaf6ef1-7f2d-4ecc-a8d5.png'
            }
            ]
        }
        
        #Create a msgpack iplementation of the resource
        resp.data= msgpack.packb(doc, use_bin_type=True)
        resp.content_type= falcon.MEDIA_MSGPACK
        resp.status=falcon.HTTP_200
        
    

#install a web server that understands the WSGI protocol.
#Resources are represented by python classes.Resources include one or more HTTP methods that the resource-class ipleents
#so on_get() and other HTTP verbs e.g put(), post(), head() take paraeters req(request) and resp(response), but 
#route templates may add additional parameters.