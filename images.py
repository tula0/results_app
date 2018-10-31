import json
iport falcon
class Resource(object):
    def on_get(self,req,resp):
        doc={
            'images':[
                {
                'href':'/images/1eaf6ef1-7f2d-4ecc-a8d5.png'
            }
            ]
        }
        
        #Create a json iplementation of the resource
        resp.body= json.dump(doc, ensure_ascii=False)
        
        #The following line can be omitted because 200 is the default status returned by the fraework, but 
        #it is included here to illustrate how this can be overridden as needed.
        
        resp.status= falcon.HTTP_200

#install a web server that understands the WSGI protocol.
#Resources are represented by python classes.Resources include one or more HTTP methods that the resource-class ipleents
#so on_get() and other HTTP verbs e.g put(), post(), head() take paraeters req(request) and resp(response), but 
#route templates may add additional parameters.

