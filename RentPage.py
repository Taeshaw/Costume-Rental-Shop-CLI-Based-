import datetime
import random

#This function reads the text file and keeps it in a list after opening it.
def file_content_here():
    file = open("stock.txt","r")
    data = file.readlines()
    file.close()
    return data

#The file was placed in an empty dictionary by this function.
data = {}
def dictionary_content_here(file_content):
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
    return main_data
    

#This function verifies the costume ID.
def valid_id_here():
    file_content = file_content_here()
    main_data = dictionary_content_here(file_content)

    valid_data = False

    while  valid_data == False:
        print_costume()
        while True:
            try:
                ID = int(input("\n Enter The Costume ID You Desire To Rent -------->  "))
                break
            except:
                print("")
                print("!!Improper Input!!")
                print("")
        if ID > 0 and ID <= 7:
            valid_data = True
            return ID
        else:
            print("*"*45)
            print("\tPlease present a legitimate costume ID !!!")
            print("*"*45,"\n")


dress_name = []
pricing_in_total = []
branding_name = []

def valid_quantity_here(ID):
    file_content = file_content_here()
    main_data = dictionary_content_here(file_content)
    while True:
        try:
            print("")
            quantity_1 = int(input("Enter The Amount of Costumes You Want To Rent ---------->  "))
            break
        except:
            print("")
            print("!!Improper Input!!")
            print("")
    if 0 < quantity_1 <= int(main_data[ID][3]):
        main_data[ID][3] = str(int(main_data[ID][3])-quantity_1)
        print(main_data)
        file = open("stock.txt","w")
        for key,value in data.items():
            string = ",".join(value)
            file.write(string)
            file.write("\n")
        file.close()
        Cos_Name = main_data[ID][0]
        branding = main_data[ID][1]
        cost = main_data[ID][2]
        total_price = float(main_data[ID][2].replace("$","")) * quantity_1
        qty = quantity_1
        pricing_in_total.append(total_price)
        dress_name.append(Cos_Name)
        branding_name.append(branding)
        print("")
        ask = input("Want To Rent Any Other Coustumes? (yes/no)").lower()
        print("")
        if ask == "yes":
            purchasesmade()
        else:
             invoice()
    elif quantity_1 > int(main_data[ID][3]):
        print("")
        print("*"*65)
        print("\t!1Requested Amount of Stock Not Available At The Moment!!")
        print("*"*65)
    elif quantity_1 <= 0:
        print("\n","*"*30)
        print("\t!!Improper Input!!")
        print("*"*31)
    return quantity_1

def purchasesmade():
    file_content = file_content_here()
    main_data = dictionary_content_here(file_content)
    ID = valid_id_here()
    quantity_1 = valid_quantity_here(ID)
    

billinvoice = []
#This function generates bill.
def invoice():
    print("")
    name = (input("Enter Your Name-----> "))
    phone = (input("Enter Your Mobile Number-----> "))
    dateformat = datetime.datetime.now()
    datecurrent = dateformat.strftime('%Y-%m-%d %A')
    print("")
    print("*"*53)
    print("\t\tCostume Details - Bill")
    print("*"*53)
    print("\tName of Customer: ",name)
    print("\tMobile Number of Customer: ",phone)
    print("\tDate of Rent: ",datecurrent)
    print("-"*70)
    print("\tCostume Name: ", dress_name)#,Cos_Name)
    print("\tBrand: ", branding_name)#,brand)
    print("\tTotal Amount: $", totalmoney())#,total_price)
    print("-"*70)

    rentline = "<<<<<<----------Rent Bill--------------->>>>>>"
    productline = "<<<<<-------Product Details------------->>>>>>"
    justdash = "-----------------------------------------------"
    filevarrandom = random.randint(1,100)
    filevar1 = name+str(filevarrandom)+".txt"
    
    billinvoice.append(rentline)
    billinvoice.append("Customer Name: "+name)
    billinvoice.append("Customer Phone: "+phone)
    billinvoice.append("Date Of Rent: "+datecurrent)
    billinvoice.append(productline)
    billinvoice.append("Costume Name: "+str(dress_name))
    billinvoice.append("Brand Name: "+str(branding_name))
    billinvoice.append("Total Amount: $"+str(totalmoney()))
    billinvoice.append(justdash)
    file = open(filevar1,"w")
    for i in billinvoice:
        file.write(f"{i}\n")
    file.close

ion = []
def totalmoney():
    sum1 = 0
    for p in range(len(pricing_in_total)):
        ion = pricing_in_total[p]
        sum1 += ion
    return sum1
