

const inventory__= fetch('./Test.json')
    .then(results => results.json())
    .then(console.log); 

var TotalOrders = 0;
var PendingOrders = 0;
var InTransit = 0;
var Deliverd = 0;

function Insert(){
    var GetAnswer = window.prompt("<h1>Do you want to add a New Order? </h1>");
    if (GetAnswer == "yes" || "Yes" || "YES")
    {
        TotalOrders ++;

        var Getname = inpwindow.promptut("Enter customer name: ");
        var GetTrackingNo = window.prompt("Enter tracking number: ");
        
        var todayDate = new Date().toISOString().slice(0, 10);
        var GetDestantion = inpwindow.promptut("enter the destination of the order: ");

        var GetStatus = inpwindow.promptut("What is the status of the order?");
        if (GetStatus == "Deliverd")
        {
            Deliverd ++
        else if (GetStatus == "In Transit" || "InTransit") 
            InTransit ++ 1

        }
    }
}
// will continue in the future 