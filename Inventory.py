import json
import time 


with open('Test.json') as f:
    inventory__ = json.load(f)

TotalOrders = 0
PendingOrders = 0
InTransit = 0
Deliverd = 0

def message():
    print("\nWhat do you want to do? (Enter a number from below!)","\n\n","1/ View Orders\n","2/ Insert Orders\n","3/ Update Orders\n","4/ Delete Orders\n\n Press Ctrl C to stop the program")

def Insert():
    #Enter tracking number 
    GetAnswer = input("Do you want to add a New Order? ")
    if GetAnswer == "yes" or "Yes" or "YES":
        TotalOrders =+ 1

        Getname = input("Enter customer name: ")
        GetTrackingNo = input("Enter tracking number: ")
        
        now = time.ctime()
        GetDestantion = input("enter the destination of the order: ")

        GetStatus = input("What is the status of the order? ")
        if GetStatus == "Deliverd":
            Deliverd =+ 1
        elif GetStatus == "In Transit" or "InTransit":
            InTransit =+ 1
        else:
            print("Unable to get order status, STATUS: NA")
            GetStatus = "NA" # Need to double check that 
        NewOrder = {Getname:{'TrackingNumber':GetTrackingNo,'DataAndTime':now,'Destination':GetDestantion, 'Status':GetStatus}}
        inventory__.update(NewOrder)
        with open('Test.json', 'w') as f:
            j = json.dump(inventory__,f)       
    else:
        pass

def Update():
    UpdateOrder = input("Do you want to update an order? ")
    if UpdateOrder == "Yes" or "yes":
        GetTrackingNumber = str(input("What is the tracking number of the order? "))
        for p_id, p_info in inventory__.items():
            for key in p_info:
                if GetTrackingNumber == p_info[key]:
                    print ("Found: ", p_id, "\n", p_info )
                    GetChange = input("what do you want to change? ")
                    if GetChange == "Destination":
                        GetNewDes = input("What destitination you want to update to? ")
                        inventory__[p_id]["Destination"] = str(GetNewDes)
                    if GetChange == "Status":
                        GetNewStatus = input("What Status you want to update the order to? ")
                        inventory__[p_id]["Status"] = str(GetNewStatus)
                    if GetChange == "Name":
                        print("you will have to delete the old customer name and add a new one with the same infomation")
                        Keepgoing = input("what to continue? ")
                        if Keepgoing == "yes" or "Yes":
                            Delete()
                            Insert()
                    with open('Test.json', 'w') as f:
                        j = json.dump(inventory__,f)                 


def Delete():
    GetAnswer = input("Do you want to delete order? ")
    if GetAnswer == "Yes" or "yes":
        GetTrackNumber = input("what is the tracking number? ")
        for p_id, p_info in inventory__.items():
            for key in p_info:
                if GetTrackNumber == p_info[key]:
                    print ("Found: ", p_id, "\n", p_info )
                    Confirm = input("Are you sure you want to delete? ")
                    if Confirm == "yes" or "Yes":
                        continue
        inventory__.pop(p_id)
        with open('Test.json', 'w') as f:
            j = json.dump(inventory__,f) 
        print ("Order has been deleted successfully! ")


def View():
    for p_id, p_info in inventory__.items():
        print("Name: ", p_id)
        for key in p_info:
            print("\t\t",key + ":",p_info[key])


if __name__ == "__main__":
    print ("Hello! This is a simple tracking app\n")
    print ("Here, you will be able to view, insert, update, and delete\n")
    print ("So, let's get started\n")
    message()
    while True:    
        GetAnswer = input()
        if GetAnswer == "1":
            View()
            message()
        elif GetAnswer == "2":
            Insert()
            message()
        elif GetAnswer == "3":
            Update()
            message()
        elif GetAnswer == "4":
            Delete()
            message()
        else:
            print ("Invalid entry! Please try again")