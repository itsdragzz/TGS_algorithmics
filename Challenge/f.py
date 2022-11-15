




def create_groups(file):
    import csv
    def find_i(list, line, it):
        for idx, value in enumerate(line):
            if value == str(it):
                list.append(idx - 1)
        return(list)


    tent_values = []
    with open(file, 'r') as file:
        csvreader = csv.reader(file)
        rows = list(csvreader)
        del(rows[0])
        new_rows = rows[0 : int(len(rows)/5) ]
        i_list = [i for i in range(len(new_rows), len(rows[0])- 1)]
        i = 0
    
    for line in new_rows:
        values = []
        it = 10


        while len(values) != 4 and it > 0:
            find_i(values, line, it)
            values = [i for i in values if i in i_list]
            values = values[0:4]
            it -= 1
            values.append(i)

        i_list = [i for i in i_list if i not in values]

        a = [rows[i][0] for i in values]
        tent_values.append(a)
        i += 1

    return(tent_values) #output is a list of names in groups of five
    

print(create_groups("Challenge/preferences.csv"))
