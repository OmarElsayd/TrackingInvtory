import numpy as np
import json
import time 


with open('Test.json') as f:
    inventory__ = json.load(f)

TotalOrders = 0
PendingOrders = 0
InTransit = 0
Deliverd = 0



def Insert():
    #Enter tracking number 
    GetAnswer = input("Do you want to add a New Order? ")
    if GetAnswer == "yes" or "Yes" or "YES":
        TotalOrders =+ 1

        Getname = input("Enter customer name: ")
        GetTrackingNo = input("Enter tracking number: ")
        
        now = time.ctime()
        GetDestantion = input("enter the destination of the order: ")

        GetStatus = input("What is the status of the order?")
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
                    print(p_id)
    pass

def Delete():
    pass

def View():
    pass


Update()