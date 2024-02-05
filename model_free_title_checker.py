
def line_split(input_file):
    name_data = []
    with open('mfpara.txt', 'r') as para_file:
        for line in para_file:
            data = line.split()
            if len(data) == 2:
                name_data.append(data[1])
    return(name_data)

def check_same_positions(list1, list2, list3):
    if len(list1) == len(list2) == len(list3):
        for item1, item2, item3 in zip(list1, list2, list3):
            if item1 == item2 == item3:
                continue
            else:
                return False
        return True
    else:
        return False

parameters = open('mfpara.txt','r')
barnase_data = open('mfdata_barnase_no_betaine.txt','r')
model_data = open('mfmodel.txt','r')

parameter_titles = line_split(parameters)
barnase_titles = line_split(barnase_data)
model_titles = line_split(model_data)

result = check_same_positions(parameter_titles,barnase_titles,model_titles)

if result:
    print("All positions are the same in the title lists.")
else:
    print("Positions are not the same in the title lists.")