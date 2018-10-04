#representing the list of crimes by crime id and total number in tabular form

crime_table=open("Crime.csv")
list1=[]
list2=[]
d1=dict()
d2=dict()

for line in crime_table:
 line=line.strip()
 l=line.split(',')
 list1.append(l[-1]) #it appends crime name to the list
 list2.append(l[-2]) #it appends crime id to the list
list2.remove('RUCR') #removing header from crime id's
list1.remove('RUCR_EXT_D') #removing header from crime names
# print(list2)

#to get the count of total crimes occured with same crime_name
"""for item in list1:
 if(item not in d1):
  d1[item]=1
 else:
  d1[item]=d1[item]+1 
# print(d1[item])"""

#to get the count of total crimes occured with the same crime_id
for item in list2:
 if(item not in d2):
  d2[item]=1
 else:
  d2[item]=d2[item]+1
 #print(d[item])

pair=zip(list1,list2)
#print(tuple(pair)) """it prints crime_id and crime_name pair"""

#to print the table that contains crime_id and crime_count
print("Crime_ID",end=' '*18)
print("Total_Crime_Count",end='\n')
for k,v in d2.items():
		print(k,end=' '*(26-len(k)))
		print(v,end='\n')


