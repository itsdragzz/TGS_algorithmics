def create_groups(file):


    import csv
    import math

    with open(file, 'r') as f:
        reader = csv.reader(f)
        #create list of lists
        data = list(reader)
        #remove header
        data.pop(0)

    #function is called data
    
        name_list = []
        for i in range(len(data)):
            name_list.append(data[i][0])


        def remove_data(data):
            for i in range(len(data)):
                del data[i][0]        
            #total = [int(x) for x in data]
            return data




    remove_data_ = [list( map(int,i) ) for i in remove_data(data)] #converts string to int of the data




    inlist = remove_data_[2]
    max_value = int(max(inlist)) #had error where max valye was only 1 less than max value
    index_value = [index for index in range(len(inlist)) if inlist[index] == max_value]

    print(index_value)

        




    #max__ = np.amax(data)
    #print(max__)
    #print(data)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
create_groups('Challenge/test.csv')
