import pandas as pd
import glob
import os
import json
class SearchResult:
    def __init__(self, tags):
        self.tags = tags
        self.extensions=[]
        self.totalResultsFound=[]
        self.countItenByext=[]
        print("inside main function")
    
    def returnResult(self):
        #calling class methos inside methods
        Data=[]
        imageData=self.SearchImages()
        textData=self.SearchText()
        srtData=self.SearchSrt()
        jsonData=self.SearchJson()
        csvData=self.SearchCsv()
        excelData=self.SearchExcel()


        if imageData[0]:
            self.totalResultsFound.extend(imageData[0])
            Data.append(imageData)

        if textData[0]:
            self.totalResultsFound.extend(textData[0])
            Data.append(textData)

        if srtData[0]:
            self.totalResultsFound.extend(srtData[0])
            Data.append(srtData)

        if jsonData[0]:
            self.totalResultsFound.extend(jsonData[0])
            Data.append(jsonData)

        if csvData[0]:
            self.totalResultsFound.extend(csvData[0])
            Data.append(csvData)

        if excelData[0]:
            self.totalResultsFound.extend(excelData[0])
            Data.append(excelData)

        self.countItenByext.extend(Data)

        return Data
    
    def returnExtensions(self):
        return self.extensions
    # search tag in image dir with image name
    def SearchImages(self):
        imageFolder=os.path.join(os.getcwd(),'static/Sampleimage')
        image_list=os.listdir(imageFolder)
        # search tags in a image names
        print("matching result")
        res = [i for i in image_list if self.tags.lower() in i.lower()]

        ext=".jpg"
        if res:
            self.extensions.append('.jpg')
        return res,ext

    # return total result
    def Totalresults(self):

        dataDict=[]
        for item in self.countItenByext:
            # print(item)
            dataDict.append({"y":len(item[0]),"label":item[1]})
        return self.totalResultsFound,dataDict




    # search data in text files
    def SearchText(self):
        textList=[]
        textFolder=os.path.join(os.getcwd(),'static/SampleText')
        for name in glob.glob(textFolder+"/*.txt"): 
            
            #first search tags in filename
            execute=1
            filename=name.replace(textFolder+"/",'').lower()
            if self.tags.lower() in filename:
                execute=0
                textList.append(filename)

            #search tag inside remaning file content
            if execute:
                with open(name) as f:
                    if self.tags.lower() in f.read().lower():
                        textList.append(filename)     
                
        if textList:
            self.extensions.append('.txt')

        return (textList,".txt")

    # search data in text files
    def SearchSrt(self):
        textList=[]
        textFolder=os.path.join(os.getcwd(),'static/SampleText')
        for name in glob.glob(textFolder+"/*.srt"): 
            
            #first search tags in filename
            execute=1
            filename=name.replace(textFolder+"/",'').lower()
            if self.tags.lower() in filename:
                execute=0
                textList.append(filename)

            #search tag inside remaning file content
            if execute:
                with open(name) as f:
                    if self.tags.lower() in f.read().lower():
                        textList.append(filename)     

        if textList:
            self.extensions.append('.srt')
                        
        return (textList,".srt")


    def SearchJson(self):
        textList=[]
        textFolder=os.path.join(os.getcwd(),'static/SampleText')
        for name in glob.glob(textFolder+"/*.json"): 
            
            #first search tags in filename
            execute=1
            filename=name.replace(textFolder+"/",'').lower()
            if self.tags.lower() in filename:
                execute=0
                textList.append(filename)

            #search tag inside remaning file content
            if execute:
                with open(name) as f:
                    data = str(json.load(f))
                    if self.tags.lower() in data.lower():
                        textList.append(filename)     
        if textList:
            self.extensions.append('.json')
                         
        return (textList,".json")

    def SearchCsv(self):
        textList=[]
        textFolder=os.path.join(os.getcwd(),'static/SampleText')
        for name in glob.glob(textFolder+"/*.csv"): 
            
            #first search tags in filename
            execute=1
            filename=name.replace(textFolder+"/",'').lower()
            if self.tags.lower() in filename:
                execute=0
                textList.append(filename)

            #search tag inside remaning file content
            if execute:
                with open(name) as f:
                    if self.tags.lower() in f.read().lower():
                        textList.append(filename)     

        if textList:
            self.extensions.append('.csv')
                        
        return (textList,".csv")

    def SearchExcel(self):
        textList=[]
        textFolder=os.path.join(os.getcwd(),'static/SampleText')
        for name in glob.glob(textFolder+"/*.xlsx"): 
            
            #first search tags in filename
            execute=1
            filename=name.replace(textFolder+"/",'').lower()
            if self.tags.lower() in filename:
                execute=0
                textList.append(filename)

            #search tag inside remaning file content
            if execute:
                df=pd.read_excel(name)
                for index,row in df.iterrows():
                    rowList=row.to_list()
                    files=[i for i in rowList if type(i)==str and self.tags.lower() in i.lower()]
                    if files:
                         textList.append(filename)
                         break;

        if textList:
            self.extensions.append('.xlsx')
                        
        return (textList,".xlsx")







