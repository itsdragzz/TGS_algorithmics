def create_groups(file):


    import csv
    import math
    import numpy as np
    import random

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

    for i in range(len(data)):
        del data[i][0]        

    
    remove_data_ = [list( map(int,i) ) for i in data] #converts string to int of the data
    #print(remove_data_ )

    data_of_max = []

    for i in range(len(remove_data_)):
        #print(i)
        inlist = remove_data_[i]
        max_value = int(max(inlist)) #had error where max valye was only 1 less than max value
        index_value = [index for index in range(len(inlist)) if inlist[index] == max_value]
        data_of_max.insert(i, index_value)

    #print(data_of_max)

    

    #data_of_max[0].index(3)

    #print(name_list[0])
    #print(data_of_max)
    out = []
    pos = 0
    #per_tent = int(len(name_list)/5)

    n = 0 #people who ranked the first name


    while n < 2:
        
        index_of_max = [] # 5 per tent 
        #print(name_list)
        #print(len(name_list))
        #print("")
        #print(data_of_max)


        for x in data_of_max:
            
            for y in x:
                #print(x, y)
                if y == n:

                    if name_list == []:
                        n = 3
                        break

                    if len(name_list) <= 5:
                        
                        #print("yes", index_of_max)
                        index_of_max.append(name_list) 

                        index_of_max = name_list
                        #print("it is", name_list )

                        name_list = []
                        n = 3
                        break


                    else:
                    
                        while len(index_of_max) <= 3:
                            print(x)
                            list_ = data_of_max.index(x) #finds the index of the list which contains n
                            print(list_)
                            index_of_max.append(name_list[list_]) #adds the name to list 
                            name_list.remove(name_list[list_])

                #n = n + 1

        if name_list == []:
            #print(index_of_max)
            out.insert(pos, index_of_max)
            break

        else:
            index_of_max.append(name_list[n])
            name_list.remove(name_list[n])
            out.insert(pos, index_of_max)

        #print(index_of_max)
    
    print(len(out))
    print(out)

    return out


'''AHASHD

#------------------- from 1d to 2d array -----------------------------
    random.shuffle(name_list)
    liston = np.array(name_list)
    #print(liston )
    #per_tent = int(len(data)/5)
    out = np.reshape(liston, (-1, 5))
    print(out)

'''



    #name = name_list[i]
    #print(data_of_max)
    #print(name_list[0])



    #max__ = np.amax(data)
    #print(max__)
    #print(data)


    
    
    
#create_groups('C:\Users\Kelvin\Documents\GitHub\TGS_algorithmics\Challenge\preferences.csv')
#create_groups('Challenge/p2.csv')
create_groups('Challenge/preferences.csv')
