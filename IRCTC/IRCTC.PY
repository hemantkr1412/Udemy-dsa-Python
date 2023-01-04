from tabnanny import check
import requests


class IRCTC:
    def __init__(self):
        self.input=input("""
        1. Check PNR Status
        2. Check Train Schedule
        3.Live Train Status                     
        """)
        
        if self.input=='1':
            self.pnr_status()
            
        elif self.input=='2':
            self.check_train()
            
        elif self.input=='3':
            self.live_train_status()
        
        else:
            print("Please Enter valid Number")
            
            
            
    def pnr_status(self):
        pnr_number=input("Enter Your PNR Number")
        
        

        url = "https://irctc1.p.rapidapi.com/api/v2/getPNRStatus"

        querystring ={'pnrNumber':pnr_number}

        headers = {
            "X-RapidAPI-Key": "9b071a0cd4msh19aeb327ca62637p19cbe1jsn256480bd6aca",
            "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        result=response.json()
        
        data = result["data"]

        class1= data['class']
        train_name=data["train_name"]
        train_number=data["train_number"]
        quota=data["quota"]
        date=data["date"]
        
        chart_prepared=data["chart_prepared"]
        booking_berth_number=data['passenger'][0]["bookingBerthNo"]
        booking_status=data['passenger'][0]["bookingStatus"]
        current_berth_no=data['passenger'][0]["currentBerthNo"]
        cuurent_status=data['passenger'][0]["currentStatus"]
        psg_age=data['passenger'][0]["passengerAge"]
        if chart_prepared:
            chart_prepared="Yes"
        else:
            chart_prepared="No"
        
        # print("Class | Train Name | Train No. | Quota | Date      | Chert Prepared(True/False) | Booking Berth No/Booking Waiting List | Current Berth No./Current WaitingList | Booking Status | Current Booking Status")
        print(class1,train_name,train_number,quota,date,chart_prepared,booking_berth_number,current_berth_no,booking_status,cuurent_status)
        
       
        
        
        
        
        
        
        
        
        
        
    def check_train(self):
        train_number=input("Enter a Train Number")
        url = "https://irctc1.p.rapidapi.com/api/v1/getTrainSchedule"

        querystring = {"trainNo":train_number}

        headers = {
            "X-RapidAPI-Key": "9b071a0cd4msh19aeb327ca62637p19cbe1jsn256480bd6aca",
            "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data=response.json()
        data=data['data']
        route=data['route']
        for i in route:
            
            print(f"{i['state_name']}|| {i['distance_from_source']}||{i['stop']}||{i['platform_number']} || {i['station_name']} || ")
                
    def live_train_status(self):
        train_number=input("Enter a Train Number")
        url = "https://irctc1.p.rapidapi.com/api/v1/liveTrainStatus"

        querystring = {"trainNo":train_number}

        headers = {
            "X-RapidAPI-Key": "9b071a0cd4msh19aeb327ca62637p19cbe1jsn256480bd6aca",
            "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        result=response.json()
        if result["data"]["success"]==True:
            data=result['data']
            previous_stations=data["previous_stations"]
            print("Previous stations")
            for i in previous_stations:
                print(i["station_name"])
            current_station=data["current_station_name"]
            print("cuurent_station -" ,current_station)
            print("Delay -- ",data["delay"])   
            upcoming_stations=data["upcoming_stations"]
            for i in upcoming_stations:
                print(i["station_name"])
        else:
            print("Train Status for this train is unavailable at the moment. Please retry in a while.")
        
        
       
       
        
obj1=IRCTC()
        