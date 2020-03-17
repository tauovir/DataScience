import json
import pickle
import numpy as np
__location = None
__data_columns = None
__model = None


def get_estimated_price(bath,balcony,bhk,t_sqft,location):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = bath
    x[1] = balcony
    x[2] = bhk
    x[3] = t_sqft
    if loc_index > 0 :
        x[loc_index] = 1
    
    return round( __model.predict([x])[0],2)
    
    
       

def get_location_names():
    load_saved_artifacts()
    return  __location

def load_saved_artifacts():
    print("Loading saved Artifacts......")
    global __data_columns
    global __location

    with open("./artifacts/columns.json") as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[4:]

    ## Now Load our Saved model
    global __model
    with open("./artifacts/priceModel.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Loading Artifact is done...")
     
if __name__ == "__main__":
    load_saved_artifacts()
    #print(get_location_name())
    print(get_estimated_price(4,1,4,2850.0, '1st Block Jayanagar'))  #bath,balcony,bhk,t_sqft,location):
    
    print(get_estimated_price(3,2,3,1630.0, '1st Block Jayanagar'))  #bath,balcony,bhk,t_sqft,location):
    


