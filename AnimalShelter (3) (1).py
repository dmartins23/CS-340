from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username=None, password=None):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
         if username and password:
            self.client = MongoClient('mongodb://%s:%s@localhost:33854' % (username, password))
         else:
            self.client = MongoClient('mongodb://localhost:33854')
         self.database = self.client['project']
    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary          
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    
    # Create method to implement the D in CRUD.
    def delete(self,data):
        if data is not None:
            insert = self.database.animals.delete(data)  # data should be dictionary 
                       
        else:
            raise Exception("Nothing to delete, because data parameter is empty")


    # Create method to implement the R in CRUD.
    def read(self,criteria=None):

        # criteria is not None then this find will return all rows which matches the criteria
        if criteria:
         # {'_id':False} just omits the unique ID of each row        
            
            data = self.database.animals.find(criteria,{"_id":False})
        else:
        #if there is no search criteria then all the rows will be return  
            data = self.database.animals.find( {} , {"_id":False})

        return data
    
    
    # Create method to implement the U in CRUD.
    
    def update(self,data):
        self.database.animals.update(data,
            projection={'seq': True, '_id': False},
            upsert= True,
            return_document= ReturnDocument.AFTER
        )  
            
        if update!=0:
            return True
                 
        else:
            raise Exception("Nothing to save, because data parameter is empty")
         
