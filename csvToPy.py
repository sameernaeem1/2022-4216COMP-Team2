import csv 


with open ('Dataset.csv','r') as csvToPy: 
    csv_reader = csv.reader(csvToPy) 
    next(csvToPy)
    for line in csv_reader:
       print(line) 
 
   
   
#with open ('Dataset.csv','w') as csvToPy:
    # for x in team_lines:
      #Line=csvToPy.write(x+'th Team\n')
     # print(Line)  
