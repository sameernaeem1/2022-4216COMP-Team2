import csv 


with open ('footballDataset.csv','r') as csvToPy: 
    team_lines=csvToPy.readlines()
    for line in team_lines:
     print(line.rstrip()) 
   
   
with open ('footballDataset.csv','w') as csvToPy:
     for x in team_lines:
      Line=csvToPy.write(x+'th Team\n')
      print(Line)  
