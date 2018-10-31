#---------This is a module to test the look:app api . Falcon does this by simulating HTTP requests--------
#Such tests can be written using one of the several python test frameworks, such as pytest package
#do : $pip install pytest

import falcon
from falcon import testing
import msgpack 
import  pytest

from look.app import api

@pytest.fixture
def client():
    return testing.TestClient(api)


#python will inject the object returned by the "client" function as additional parameter

def test_list_images(client):
    doc={
        'images':[
            {
                'href':'/images/1eafef1.png'
            }
            ]
    }
    #original guide has only the code above, but suppossiing I want to run a test on different modules, I guess I would need to
    #include the code below, though this has to be tested first
    
    doc2={
        'images2':[
            {
                'href':'/images/1eafef1.png'
            }
            ]
    }
    
    
    response1= client.simulate_get('/images')
    response2= client.simulate_get('/images2')
    result_doc1=msgpack.unpackb(response1.content,encoding='utf-8')
    result_doc2=msgpack.unpackb(response2.content,encoding='utf-8')
    
    assert result_doc1==doc1
    assert result_doc2==doc2
    
    #from the main project directory, exercise your new test by running pytest against the test directory
    #as: $pytests tests
    #if pytest reports any errors ,take a moment to  fix them up before proceeding to deploy the app
    
    
    
    
    