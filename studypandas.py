''' *-*-*-*-*-*-* NOTE: *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* 
|  Before you Study Pandas framework you have to know Python Basics and Oriented object programing |
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
'''


              ################################################################
            ## *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*##
           ## */ ----------------------------------------------------------- \*##
           ## *| Here you are going to learn Pandas Framework For Beginners  |*##
           ## *| -------------=> https://github.com/Omarne96  <=------------ |*##
           ## *| ----------------=>  Instagram : Omar_ne16 <=--------------- |*##
           ## *\ ----------------------------------------------------------- /*##
            ## *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*##      
              ################################################################


'''
        First of all you have to install Pandas framework
        Go to your Terminal and type this commands :
        pip install pandas
        if you have any error check the pip update or use pip3 instead of pip
'''

## Then import the pandas library
import pandas as pd
import re                                           ## this RE is regex you will learn it below



## version=pd.show_versions()                       ## If you want to know the instaled tools versions
## Or you can use pd.__version__  which gives you the same details


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
df.iloc[4,df.columns.get_loc('Attack')] ## Will gives you the Value of position you selected



                            

## Sorting/Describing:
######################

df.describe()                                 ## Give you details of your numerical columns 
df.Attack.describe()                          ## Give you details of Attack row
##df.info()
##df.info(memory_usage="deep")                ## This will gives you details about data and memory usage
df.memory_usage(deep=True)                    ## This will gives you every colums memory usage in bytes, use deep=True to get the real numbers


df.Attack.value_counts()                      ## Give you the occurrence number of all attacks values

df.sort_values("Name",ascending=True)         ## This will sort names From A to Z
df.sort_values("Name",ascending=False)        ## This will sort names From Z to A
df.sort_values(['Name','HP'],ascending=[1,0]) ## This will sort names from a to z and hp from the last to first

df['Type 2'].unique()                         ## This ill gives you only the unique values of type 2 column


## THE Missing values :
#######################

df.isnull()                                   ## Will gives you if you have Empty cases or not (NaN)
df.notnull()                                  ## Will gives you if you have Full cases or not ~(NaN)
df.isnull().sum()                             ## This will gives you number of missing values in data file
df[df['Type 2'].isnull()]                     ## This will gives you the Nan values in Type 2


''' NOTE :The drope function has inplace parameter is False by default which means not deleted completely 
'''
df.dropna(how='any')                          ## You will delet any rows has NaN value
df.dropna(how='all')                          ## You will delet rows wich are all columns are NaN
df.dropna(subset=['Type 2'], how='any')       ## This will delet a row if 'Type 2' is NaN
df['Type 2'].value_counts(dropna=False)       ## Occurrence number for all values in Type 2 including NaN

df['Type 2'].fillna(value="okok",inplace=True)## Fill all NanN in Type 2 with 'okok'   ==> (replace it)

        #########################################################################
        ## ------------------------------------------------------------------- ##                    
        ## ------------  Updates on The New Vesion of Pandas  ---------------  ##
        ## --------------------------------------------------------------------##
        #########################################################################

## You can use isna() and notna() functions instide of isnull() and notnull() 

##Then you can use the NEW Method to drop rows or columns:

df.drop(index=[0,1,2])                         ## This will Drop row 0 and 1 and 2
df.drop(columns=['HP','Type 2'])               ## This will Drop HP nad Type 2 columns




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

##df.to_csv("modified.csv",index=False) :
df.to_csv("modified.txt",index=False,sep="\t")

            #############################################################
            ##   to Save as exel file you have to install openpyxl :   ##
            ##                  pip install openpyxl                   ##
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
sere.Name.str.replace('u','').str.replace('a','s') 



## Rename :
###########
''' inplace=True is important to work'''
dataf=pd.read_csv("data_file.csv")
dataf.rename({'Type 1':'T1','Type 2':'T2'},axis="columns",inplace=True)



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
########################

df=pd.read_csv('data_file.csv')
df['Attack']=df.Attack.astype(float)
df.dtypes                                       ## Print it to see type of attack columns

## Or you can change it before you read the file like this example:
###################################################################
df=pd.read_csv('data_file.csv',dtype={'Attack':float})




   

'''----------------------------------------------------------------------------------------------------------------------------------'''



      #############################################################################
      ## IMPORTANT NOTE :------------------------------------------------------- ##
      ## | To Make your pandas DataFrame smaller and faster : Use Categories    |##
      ##  ---------------------------------------------------------------------- ##
      #############################################################################



## Categories (Object): 
########################

## ~~ First of all check the size of your data frame and size of each column ~~ ##
test=pd.read_csv('data_file.csv')

#test.info(memory_usage="deep")                        ## The date original size is 128.7 KB
before=test.memory_usage(deep=True)                    ## For example the Name columns have 30299 Bytes here

## ~~ Lets change the Name column to category and check again ~~ ##
test["Name"]=test['Name'].astype('category')           ## This will change type of Name to categotry
test["Type 1"]=test['Type 1'].astype('category')
test["Type 2"]=test['Type 2'].astype('category')
test["HP"]=test.HP.astype('category')
test["Attack"]=test.Attack.astype('category')
test["Defense"]=test.Defense.astype('category')
test["Sp. Atk"]=test['Sp. Atk'].astype('category')
test["Sp. Def"]=test['Sp. Def'].astype('category')
test["Generation"]=test.Generation.astype('category')
test["Legendary"]=test.Legendary.astype('category')


#test.info(memory_usage="deep")                 ## Now the data size will be 96.9 KB
after=test.memory_usage(deep=True)              ## Now the name column becomes 27408 bytes, difference is 2891 bytes

test.Name.cat.codes.head()                      ## This will represent the names series as an integers (with codes)

''' Explain : if you use test.memory_usage(deep=True) you will see decreased of size in all columns
              except Names columns, the name column size will increase because of the changing to object column (integer numbers) 
              ( all strings column name change to object columns(integers)   ) and that logically if the size increased.
              
              But if you  use test.info(memory_usage="deep")  you will see the total size of data 
              decreased from 128.7 KB to 96.6 KB and that's the point
'''

    ###############################################################################################
    ## --- IMPORTANT NOTE 2 :------------------------------------------------------------------- ##
    ##| Categories do not just save the size of file, its make you faster in compilation too :D |##
    ## ----------------------------------------------------------------------------------------- ##
    ###############################################################################################



'''----------------------------------------------------------------------------------------------------------------------------------'''

























###########################################################################################
## ------------------------------------------------------------------------------------- ##
##| *-*-*-*-*-*-*-*-*-*-*-*-*- : Things i did not undertand : -*-*-*-*-*-*-*-*-*-*-*-*-*|##
##| *                                                                                  *|##
##| *                                                                                  *|##
##| *                                                                                  *|##
##| *                                                                                  *|##
##| *                                                                                  *|##
##| *                                                                                  *|##
##| *                                                                                  *|##
##| *                                                                                  *|##
##| *-*-*-.*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*|##            
## ------------------------------------------------------------------------------------- ##
###########################################################################################





            ##################################################################
            ##  ----------------------------------------------------------  ##
            ## | ./--------------- : For Any Questions : --------------\. | ##
            ## | |-------- https://github.com/Omarne96/Pandas ----------| | ##
            ## | .\ ------------- Instagram : Omar_ne16 ---------------/. | ##
            ##  ----------------------------------------------------------  ##
            ##################################################################

                           ##             Enjoy              ##          

            #################################################################
            ##  ----------------- : Database Source : -------------------  ##
            ## |          link of the database we are woring on          | ##
            ## |          https://www.kaggle.com/abcsds/pokemon          | ##
            ##  ---------------------------------------------------------  ##
            #################################################################












##################################################
## This is the result of changing to category:  ##
##################################################
'''
###################################
## Before Changing to category : ##
###################################
Index            64
#              6400
Name          30299
Type 1        27408
Type 2        22066
HP             6400
Attack         6400
Defense        6400
Sp. Atk        6400
Sp. Def        6400
Speed          6400
Generation     6400
Legendary       800
dtype: int64
#################################
## After Changing to category :##
#################################
Index            64
#              6400
Name          56485
Type 1         1802
Type 2         1802
HP             3600
Attack         5784
Defense        5720
Sp. Atk        5736
Sp. Def        3584
Speed          6400
Generation      976
Legendary       882

dtype: int64
[Finished in 6.4s]

'''            
