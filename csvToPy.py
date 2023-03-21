import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("Dataset.csv")


# get a list of all team names
team_names = df['Team'].unique().tolist()


## UI 
1
def Userinterface():
 while True:
    print("-----Premier League Season's 2009 to 2022-----")
    print()
    userinput= input("0:Display the whole team in whole season\n1:Display the status of each team in whole season\n2:Display a team\n3:Display team number\n4:Compare Teams\n5:Display the asending order rank of each teams in whole seasons\n6:Display the rank and point of that particular team\n7:\n8:\nq:Quit\nChoose an option:")
    if userinput == '0':
        print(df)

    elif userinput=='q':
       ## quit
       break
    
    elif userinput=='1':
       ##display the status of teams in whole seasons### 
      for index, row in df.iterrows():  
       print(index,row)

    elif userinput=='2':
##display the status of that particular team### 
      print("Select a team:")
      for i, team in enumerate(team_names):
         print(f"{i+1}. {team}")
      selected_team_index = int(input("Enter the number of the team you want to select: ")) - 1
      selected_team = team_names[selected_team_index]
      selected_team_data = df[df['Team'] == selected_team]
      print(selected_team_data)

    elif userinput=='3':
       ##only shows the unique team##
       for i, team in enumerate(team_names):
         print(f"{i+1}. {team}")

    elif userinput=='4':
         for i, team in enumerate(team_names):
             print(f"{i+1}. {team}")
         ui4=int(input('Choose a team:'))-1
         df1=df.iloc[int(ui4)]
         print("The team you have picked is:")
         print(df1['Team'])
      

         
         ui42=int(input('Choose another team:'))-1
         #print(df.iloc[int(ui42)])
         df2=df.iloc[int(ui42)]
         print("The team you have picked is:")
         print(df2['Team'])
         dff=df1.compare(df2)
         print(dff)



    elif userinput=='5':
      ## print the whole teams in ascending order of rank.
      print(df.sort_values((['Rank','Points']), ascending=True))


  ## Ask the user to input a keyword to display the value
    elif userinput=='6':
       for i, team in enumerate(team_names):
         print(f"{i+1}. {team}")
       chosen_team_index = int(input("Enter the number of the team you want to select: ")) - 1
       chosen_team = team_names[chosen_team_index]
       print(f"Team:{chosen_team}")
       chosen_team_df=df[df['Team'] == chosen_team]
       user_keyword=input("Enter a keyword to search for the component of the team:(eg Points, rank or wins)")
       chosen_columns=[col for col in chosen_team_df.columns if user_keyword.lower() in col.lower()]
       print(chosen_team_df[chosen_columns])
       if  user_keyword =='wins':
        totalnum=chosen_team_df[chosen_columns].sum()
        print(f"{chosen_team}  get {totalnum} ")
       elif user_keyword=='rank':
        print(f"{chosen_team} got different {user_keyword} in different season for {len(chosen_team_df) } times")
       elif user_keyword=='points':
        totalpoints=chosen_team_df[chosen_columns].sum()
        print(f"{chosen_team} got total {totalpoints} points")


    elif userinput=='7':
      for i, team in enumerate(team_names):
        print(f"{i+1}.{team}")
      chosen_team_index = int(input("Enter the number of the team you want to select: ")) - 1
      chosen_team = team_names[chosen_team_index]
      print(f"Team:{chosen_team}")
      chosen_team_df=df[df['Team'] == chosen_team]
      user_keyword=input("Enter a keyword to search for the component of the team:(eg Points, rank or wins)")
      chosen_columns=[col for col in chosen_team_df.columns if user_keyword.lower() in col.lower()] 
      selected_comp=chosen_team_df[chosen_columns].iloc[0]
       ## 
      plt.bar(["comp1"],[selected_comp.values[0]])
      plt.title(f"{chosen_team} {user_keyword}")
      plt.show()



    elif userinput=='8':
         for i, team in enumerate(team_names):
             print(f"{i+1}. {team}")
         ui4=int(input('choose the team:'))-1
         print(df.iloc[int(ui4)])
         df1=df.iloc[int(ui4)]
         ui42=int(input('choose another team:'))-1
         print(df.iloc[int(ui42)])
         df2=df.iloc[int(ui42)]
         dff=df1.compare(df2)
         print(dff)

           




    


## api workflow
Userinterface()


## components
## sort the list in an specific order 
#df.sort_values((['Rank','Points']), ascending=False)
## specify the conditon to find the specific one, rank 1 teams in the past decade
#rank1=df.loc[df['Rank']==1]
#print(rank1)
## iterate through each row
#for index, row in df.iterrows():  ## it list all team at same time, we can use this function to ask which team are they interested in.
#print(index,row ['Team'])

## the rank of arsenal is 3 , which means that permit us to allocate the specific location (R,C)
#print(df.iloc[3,4])

## access unique element
#print(df.head(4)[['Team','Games','Season']])

## use iloc function to modify the associated array
#df.iloc[3,1]

