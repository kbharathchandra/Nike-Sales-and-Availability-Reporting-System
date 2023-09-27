import csv

def readCSV(filename):
  list1=[]
  with open(filename, "r",newline='', encoding="utf-8") as f:
    
       
    reader1=csv.reader(f)
    header1=next(reader1)
    

    for line in reader1:
        dict2 = {}
        for i in range(0,len(header1)):
            dict2[header1[i]]=line[i]
        list1.append(dict2)
    return list1  

def writeCSV(myFile,listOfDict):
  keysList1 = list(listOfDict[0].keys())   
  myFile=open(myFile,"w")
  writer1 = csv.writer(myFile)
  writer1.writerow(keysList1)
  for dict in listOfDict:
    writer1.writerow(dict.values())
  myFile.close()


def keepOnly(listOfDict,key,value):
    
    l=[]
    for i in listOfDict:
        if (key in i and value == i[key]):
            l.append(i)
    return l


def discardOnly(listOfDict,key,value):
    l=[]
    
    
    for i in listOfDict:
        if (key in i and value == i[key]):
            l.append(i)
    
    for i in l:
        listOfDict.remove(i)
    return listOfDict

  
def filterRange(listOfDict,key,low,high):
    
    l=[]
    for i in listOfDict:
        if (key in i and low <= i[key] < high):
            l.append(i)
            
    return l

def duration(d1, d2):


  diff = d2 - d1

  return diff.days

def open_year(dictionary):
  for i in dictionary:
    if i=='OPEN DATE':
      
    
      return dictionary[i][6:10]

def departments(list_of_dictionaries):
  deps_list = []
  for i in list_of_dictionaries:
    if i["SUBJECT"] in deps_list:
      pass
    else:
     deps_list.append(i["SUBJECT"]) 
  deps_list.sort()
  return deps_list
  
def filterYear(list_of_dictionaries, low, high):
  a=[]
  for i in list_of_dictionaries:
     if int(low) <= int(open_year(i)) <int(high):
       a.append(i)
  return a
list_of_dict_1=readCSV("Nike_data.csv")      

def data_by_subject(a):
  g=[]
  year_start=int(a["year_start"])
  year_end=int(a["year_end"])
  b=[]
  for i in range(year_start,year_end+1):
    b.append(i)
    yearcoloum=-1
  for every_year in b:
    e={}
    f=[]
    yearcoloum=yearcoloum+1
    c= filterYear(ALL_DATA,every_year,every_year+1)
    Total=len(c)
    presentyeardepartment=departments(c)
    if len(presentyeardepartment)==0:
      continue
    for i in presentyeardepartment:
      lodofdepartment=keepOnly(c,"SUBJECT",i)
      departmentcount=len(lodofdepartment)
      calculatedpercentage=int(100*round(departmentcount/Total,2))
      f.append(calculatedpercentage)
      e["values"]=f
      e["labels"]=presentyeardepartment                       
      e["domain"]={"column": yearcoloum }
      e["name"]=str(every_year)
      e["hole"]=.4
      e["type"]='pie'
    g.append(e)
  return g
ALL_DATA=readCSV("Nike_data.csv")

def avilability_(a):
  g=[]
  year_start=int(a["year_start"])
  year_end=int(a["year_end"])
  b=[year_start]
  for i in range(year_start,year_end+1):
    b.append(i)
    yearcoloum=-1
  for every_year in b:
    e={}
    availability=[]
    size=[]
    unavailability=[]
    
    c= filterYear(ALL_DATA,every_year,every_year+1)
    Total=len(c)
    presentyeardepartment=departments(c)
    if len(presentyeardepartment)==0:
      continue
    for i in presentyeardepartment:
      lodofdepartment=keepOnly(c,"SUBJECT",i)
      availabilityofstock=keepOnly(lodofdepartment,"availability","InStock")
      unavailabilityofstock=keepOnly(lodofdepartment,"availability","OutOfStock")
      departmentcount=len(lodofdepartment)
      availabilitycount=len(availabilityofstock)
      unavailabilitycount=len(unavailabilityofstock)
      calculatedpercentage=int(100*round(availabilitycount/departmentcount,2))
      
      availability.append(calculatedpercentage)
      size.append(10*calculatedpercentage)
      unavailability.append(unavailabilitycount)
      e["y"]=availability
      e["x"]=presentyeardepartment  
      e["mode"]="markers"
      e["marker"]={"size":size,
                  'sizemode':'area'}
      e["text"]=str(every_year)
    g.append(e)
  return g  
    