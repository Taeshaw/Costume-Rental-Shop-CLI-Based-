import ViewPage
import RentPage
import ReturnPage

def main():
    print("+" * 50)
    print("\t\tWelcome To The Costume Rental Application")
    print("+" * 50)
    a = ""
    looping = False
    while looping == False:
        loopingother = True
        while loopingother == True:
            try:
                a = input("\nSelect The Number According To Your Need ----->\
                          \n(1) || Press 1 To See All The Details About The Costumes.\
                          \n(2) || Press 2 To Rent Your Desired Costume.\
                          \n(3) || Press 3 To Return Any Costume You Have Rented.\
                          \n(4) || Press 4 In Order To Exit Out Of Appliccation.\
                          \nEnter The Desired Number: ")
                loopingother = False
            except:
                print("Number Out Of Bounds! Only Provided Numbers Allowed.")
            if a == "1":
                ViewPage.print_costume()
            elif a == "2":
                RentPage.purchasesmade()
            elif a == "3":
                ReturnPage.returnvaluestomain()
            elif a == "4":
                b = input("\nDo you really want to quit?? (Yes/No): ").lower()
                if b == "yes":
                    print("\n","*"*55)
                    print("\tThank You For Visiting The Application. Feel Free To Return When Desired")
                    print("*"*55)
                    print("")
                    looping = True
            else:
                print("\n","*"*65)
                print("\t\t\tNumber Press Out Of Bounds\
                       \n\tPlease choose the value based on the available options.")
                print(" ","*"*65)

main()
