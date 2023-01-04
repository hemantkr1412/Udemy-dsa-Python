from tracemalloc import start
from urllib import request
import requests
from datetime import datetime

def checkmadicare(upprlimit,lowerlimit):
    count=0
    
    for i in range(1,11):
        url=f"https://jsonmock.hackerrank.com/api/medical_records?page={i}"
        data=requests.request('GET',url)
        data=data.json()
        data=data['data']
        for i in range(len(data)):
            if data[i]['vitals']['bloodPressureDiastole']<=upprlimit and data[i]['vitals']['bloodPressureDiastole']>=lowerlimit:
                count=count+1
    return count

result=checkmadicare(120,90)
print(result)
