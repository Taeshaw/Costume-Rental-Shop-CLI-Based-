def view():
    print("\n\t\t\tNow we are viewing the costumes and its details.\n")

#This function reads the text file and keeps it in a list after opening it.
def file_content_here():
    file = open("stock.txt","r")
    data = file.readlines()
    file.close()
    #print(data)
    return data

#The file was placed in an empty dictionary by this function.
def dictionary_content_here(file_content):
    data = {}
    for index in range(len(file_content)):
        data[index+1] = file_content[index].replace("\n","").split(",")
    #print(data)
    return data

#The dictionary is printed using this function in a tabular manner.
def print_costume():
    file_content = file_content_here()
    main_data = dictionary_content_here(file_content)
    print("-"*105)
    print("ID","\t","Costume Name","\t","Brand","\t\t","Price","\t","Quantity")
    print("-"*105)
    for key,value in main_data.items():
        print(key,"\t",value[0],"\t",value[1],"\t",value[2],"\t",value[3])
    print("-"*105)