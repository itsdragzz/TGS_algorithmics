def create_groups(file):
    import numpy as np
    #open csv file

    def Open(file): #open csv file
        import csv
        with open(file, 'r') as f:
            reader = csv.reader(f)
            #create list of lists
            data = list(reader)
            #remove header
            data.pop(0)
        return data 

    data = Open(file) #open's the file

    def name_list(data):
        name_list = []
        name_loop = 0

        for i in range(len(data)):
            name_list.append(data[i][0])

        #print(len(data))
        
        #print(name_list[0])

        return name_list


    def remove_data(data):
        for i in range(len(data)):
            del data[i][0]

        
        #total = [int(x) for x in data]

        return data

    


    name_list_ = name_list(data)
    remove_data_ = [list( map(int,i) ) for i in remove_data(data)] #converts string to int of the data


    
    #corr_arrToarr 

    def largestInxValye(input_list):
        max_value = int(max(input_list)) #had error where max valye was only 1 less than max value
        index_value = [index for index in range(len(input_list)) if input_list[index] == max_value]

        
        return index_value 

    print(int(max(data[0])) + 1)
 
    print(largestInxValye(remove_data_ [0]))




    #print(name_list)

    #max__ = np.amax(data)
    #print(max__)
    #print(data)

'''
    #find max value of data                     dont know yet how to do thisq
    def max_value(data):
        max_value = 0
        for i in range(len(data)):
            if max_value < data[i][1]:
                max_value = data[i][1]
        return max_value

'''


    



    #print(max_)
    






    
create_groups('Challenge/preferences.csv')




'''
    Inputs:
    file: name of the csv
    Outputs: a list of lists, where each sublist contains the name of the five students which are going to share a tent
    '''



