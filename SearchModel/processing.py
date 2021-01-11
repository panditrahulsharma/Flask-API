['BMW X6 SUV 2012',
 'Cadillac Escalade EXT Crew Cab 2007',
 'Dodge Charger SRT-8 2009',
 'Jeep Patriot SUV 2012',
 'HUMMER H2 SUT Crew Cab 2009',
 'Plymouth Neon Coupe 1999',
 'Suzuki SX4 Sedan 2012',
 'Acura RL Sedan 2012',
 'Audi S5 Convertible 2012',
 'Mercedes-Benz 300-Class Convertible 1993',
 'Bentley Mulsanne Sedan 2011',
 'Toyota 4Runner SUV 2012',
 'Ferrari 458 Italia Coupe 2012',
 'Lamborghini Gallardo LP 570-4 Superleggera 2012',
 'Tesla Model S Sedan 2012',
 'Aston Martin V8 Vantage Convertible 2012',
 'Honda Accord Coupe 2012',
 'Ford Mustang Convertible 2007',
 'Hyundai Sonata Sedan 2012']


import os
import shutil
import pandas as pd
import numpy as np



for folder in folders:
    print(folder)

#create a text files with random name
for i in range(0,len(folders)):
    print(folders[i])
    f = open("{}.txt".format(i), "a")
    f.write("Now the file has more content!")
    f.write("car class {}".format(folders[i]))
    f.close()
    

#create json file
import json

for i in range(0,len(folders)):
    data = {}
    data['people'] = []
    data['people'].append({
        'name': 'Scott',
        'website': 'stackabuse.com',
        'from': 'Nebraska'
    })
    data['people'].append({
        'name': 'Larry',
        'website': 'google.com',
        'from': 'Michigan'
    })
    data['people'].append({
        'name': 'Tim',
        'website': 'apple.com',
        'from': 'Alabama'
    })
    
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile,indent=3)    






for i in range(0,len(folders)):
    # dictionary of data  
    dct = {'ID': {0: 23, 1: 43, 2: 12,  
                  3: 13, 4: 67, 5: 89,  
                  6: 90, 7: 56, 8: 34},  
          'Name': {0: 'Ram', 1: folders[i],  
                   2: 'Yash', 3: 'Aman',  
                   4: 'Arjun', 5: 'Aditya',  
                   6: 'Divya', 7: 'Chalsea',  
                   8: 'Akash' },  
          'Marks': {0: 89, 1: 97, 2: 45, 3: 78,  
                    4: 56, 5: 76, 6: 100, 7: 87,  
                    8: 81},  
          'Grade': {0: 'B', 1: 'A', 2: 'F', 3: 'C',  
                    4: 'E', 5: 'C', 6: 'A', 7: 'B',  
                    8: 'B'}  
        }  
      
    # forming dataframe 
    data = pd.DataFrame(dct)  
      
    # storing into the excel file 
    data.to_excel("{}.xlsx".format(i))