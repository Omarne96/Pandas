


      ###############################################################
      ##                                                           ##
      ## Here you are going to learn Pandas Framework For Beginners##
      ##               https://github.com/Omarne96                 ##
      ##                  Instagram : Omar_ne16                    ##
      ###############################################################

'''
        First of all you have to install Pandas framework
        Go to your Terminal and type this commands :
        pip install pandas
        if you have any error check the pip update or use pip3 instead of pip
'''

## Then import the pandas library
import pandas as pd
import re                                           ## this RE is regex you will learn it below


## Now, read the csv file with read_csv() fucntion:

df=pd.read_csv("data_file.txt",delimiter="\t")      ## Delimiter="\t" to separate columns
''' 
        You can read a file from URL too with read_csv("https://URL") 
        Or you can read a table like read_table("https://URL")
'''

  ########################################################################################
  ##  if you want to read an xlsx file  you have to install it : pip3 install xlrd      ##
  ##  if you want to write on an xlsx file you have to install it : pip3 install xlwt   ##
  ########################################################################################


df=pd.read_excel('data_file.xlsx')      ## Read the excel file
df.head(3)                              ## Print n first elements
df.tail(3)                              ## print n last elemets


## Read each Column :
######################
df.columns                              ## will gives you title of columns and dtype
df['Name'][0:5]                         ## or df.Name  will gives you n mumbers of names
df[['Name','Type 1','HP']]              ## will gives you many columns as you typed


## Read ech row :
#################
df.iloc[0:4]                            ## will gives you n rows 

'''
    for index, row in df.iterrows():    ## this will gives you all names in file
	    print(index, row['Name'])
'''


## Read a specific position :
#############################
df.iloc[2,1]                            ## will gives you a spesicif position
df.loc[df['Type 1'] == "Fire"]          ## will gives you all rows equals Fire type in your data.


## Sorting/Describing:
#####################
df.describe()                                 ## Give you details of your numerical columns 
df.Attack.describe()                          ## Give you details of Attack row
df.Attack.value_counts()                      ## Give you number of all attacks you have

df.sort_values("Name",ascending=True)         ## This will sort names From A to Z
df.sort_values("Name",ascending=False)        ## This will sort names From Z to A
df.sort_values(['Name','HP'],ascending=[1,0]) ## This will sort names from a to z and hp from the last to first


''' --------------------------------------------------------------------------------------'''

## Making Changes to the data:
##############################

df['Total']=df['Attack']+df['Defense']+df['Speed']+df['Sp. Def']+df['Sp. Atk']+df['HP']
## This make new column in your data which is the total of some columns

df=df.drop(columns=['Total'])                  ## This will Delete a columns

## add new columns of total again :
df['Total']=df.iloc[:,4:10].sum(axis=1)        ## axis=1 to make horizontal sum

## Reorder columns in your data 
cols=list(df.columns)                          ## put it in a list
df=df[cols[0:4]+[cols[-1]]+cols[4:12]]         ## This reorder it as you want 


# Save your file:
#################

##df.to_csv("modified.csv",index=False)
df.to_csv("modified.txt",index=False,sep="\t")

            #############################################################
            ##   to Save as exel file you have to install openpyxl :   ##
            ##   pip install openpyxl                                  ##
            #############################################################

## Save it as excel file:
#########################
df.to_excel("modified.xlsx",index=False)   ##index=false to remove the first column of index


## Filtring Data:
#################
new_df=df.loc[(df['Type 1']=="Grass") & (df["Type 2"]=="Poison")&(df["HP"]>70)]

###new_df=new_df.reset_index(drop=True, inplace=True)   

new_df.to_csv("new_df.txt",index=False,sep="\t")
# We create new dataframe content only this conditions


'''---------------------------------------------------------------------------------------'''


## Search in word ( STRINGS ):
##############################

ok=df.loc[df['Name'].str.contains("Mega")]       ## Select all names contains string Mega

## You can search by regular expressions:
#########################################  
            ## NOTE  :    You have to import re  
'''sere=df.loc[df["Type 1"].str.contains("Fire|Grass",regex=True)]'''

##### Flags to ignore the cases:
sere=df.loc[df["Type 1"].str.contains("fire|grass",flags=re.I,regex=True)] 

##### This will gives you the all names who start with pi:
sere=df.loc[df["Name"].str.contains("^pi[a-z]*",flags=re.I,regex=True)]

##Remove U and change a to s in Name column :
ok.Name.str.replace('u','').str.replace('a','s') 



## Condition Changes :
######################

#### If type=='fire' make it 'okok' :
df.loc[df["Type 1"]=='Fire',"Type 1"]="okok" 

#### Change 2 parameters in one time :
df.loc[df["Total"]>500,['Generation','Legendary']]=['tets 1','test 2'] 



## Aggregate statistics (Groupby) :
###################################

## Read the file again to reinitialize the first values ( without changes ):
ok=pd.read_csv("data_file.txt",delimiter="\t")

ans=ok.groupby(['Type 1']).mean().sort_values('Attack',ascending=False) 
           ## sort the average from the highest attack to the low


ans2=df.groupby('Name').Attack.agg(['min','max','count','mean']) 
          ##  agg(['','']) you can use man functions 






## Working with large amounts of data :
#######################################

''' for df in pd.read_csv('data_file.txt',delimiter='\t',chunksize=10):
	print("-*-*-*-*-*-*-*-*-**")
	print(df)
'''
            ## the chinkzise will print the first line every n rows 



''' L code hada tan mafhamtoch '''
new_dfrm=pd.DataFrame(columns=df.columns)
for df in pd.read_csv('data_file.csv',chunksize=3):
	results=df.groupby(['Type 1']).count()

	new_dfrm=pd.concat([new_dfrm,results])
''' L code hada tan mafhamtoch '''




## Change the data type:
#########################

df=pd.read_csv('data_file.csv')
df['Attack']=df.Attack.astype(float)
df.dtypes                                       ## Print it to see type of attack columns

## Or you can change it before you read the file like this example:
###################################################################
df=pd.read_csv('data_file.csv',dtype={'Attack':float})












   



































            #################################################################
            ## ----------------------------------------------------------- ##
            ##                     For Any Questions :                     ##
            ##       https://https://github.com/Omarne96/Pandas            ##
            ##                   Instagram : Omar_ne16                     ##
            ## ----------------------------------------------------------- ##
            #################################################################

                            ##            Enjoy              ##          

            #################################################################
            ## ------------------- Database Source : ----------------------##
            ##            link of the database we are woring on            ##
            ##            https://www.kaggle.com/abcsds/pokemon            ##
            ## ----------------------------------------------------------- ##
            #################################################################
