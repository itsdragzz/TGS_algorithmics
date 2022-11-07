def create_groups(file):
    import numpy as np
    #open csv file

    def a(file): #open csv file
        import csv
        with open(file, 'r') as f:
            reader = csv.reader(f)
            #create list of lists
            data = list(reader)
            #remove header
            data.pop(0)
        return data 

    data = np.array(a(file))
    len_arr = len(data[0])

    max_ = max(map(max, data[0]))

    



    print(max_)
    






    
create_groups('Challenge/preferences.csv')




'''
    Inputs:
    file: name of the csv
    Outputs: a list of lists, where each sublist contains the name of the five students which are going to share a tent
    '''



