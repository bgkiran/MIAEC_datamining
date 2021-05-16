#importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error 
from math import sqrt


#Reading missing data file
missing_data = pd.read_excel(r'D:\Bupa_AG_10_OUTput.xlsx',header=None)

#Reading non-missing data file
complete_data = pd.read_excel(r'D:\Bupa.xlsx',header=None)


#seperating numerical and categorical columns from non-missing data file
numeric = complete_data.select_dtypes(exclude=["bool_","object_"])
catagorical = complete_data.select_dtypes(exclude=["number","bool_"])
    
#seperating numerical and categorical columns from missing data file
numeric_imputed = missing_data.select_dtypes(exclude=["bool_","object_"])
catagorical_imputed = missing_data.select_dtypes(exclude=["number","bool_"])
    

#calculating AE For categorical columns
if (catagorical.size !=0):
        catagorical1 = np.ravel(catagorical)
        catagorical_imputed1 = np.ravel(catagorical_imputed)
    
        sum=0
        
        for i in range(len(catagorical1)):
            if catagorical1[i] == catagorical_imputed1[i]:
                sum=sum+1;
            #print(i)  
        #print(sum)
        print("AE : ",sum/len(catagorical1))
        
    #calculating root mean sqaure error For numerical columns
if (numeric.size!=0):
        numeric1 = np.ravel(numeric)
        numeric_imputed1 = np.ravel(numeric_imputed)
    
    
        rmse = sqrt(mean_squared_error(numeric1, numeric_imputed1))
    
        print("Root Mean Squared Error : ",rmse)
        #print("Frobenius norm and the condition number:")
        #print(np.linalg.norm(rmse) / np.linalg.norm(numeric1))
        
        
        
        result =(np.linalg.norm((numeric_imputed - numeric),'fro'))  / (np.linalg.norm(numeric,'fro'))
        print("Normalized Root Mean Squared Error : ",result)
        #numpy_numeric_imputed1 = numeric_imputed1.to_numpy()
else:
    print("No missing value in the data")
    #self_created_missing_data=missing_data
    #for col in self_created_missing_data.columns:
        #self_created_missing_data.loc[self_created_missing_data.sample(frac=0.1).index, col] = pd.np.nan

   #print("Total Missing values radomly generated in the data : ", self_created_missing_data.isnull().sum().sum())


    #imputation-of-missing-values
   # df = self_created_missing_data.apply(lambda x:x.fillna(x.value_counts().index[0]))
    #df.to_csv('imputed_data.csv',index=False,header=False)

    #print(df.select_dtypes(exclude=["number","bool_","object_"]))

    #seperating numerical and categorical columns from non-missing data file
    #numeric = complete_data.select_dtypes(exclude=["bool_","object_"])
   # catagorical = complete_data.select_dtypes(exclude=["number","bool_"])

    #seperating numerical and categorical columns from missing data file
   # numeric_imputed = df.select_dtypes(exclude=["bool_","object_"])
   # catagorical_imputed = df.select_dtypes(exclude=["number","bool_"])



    #calculating AE For categorical columns
    #if (catagorical.size !=0):
       # catagorical1 = np.ravel(catagorical)
       # catagorical_imputed1 = np.ravel(catagorical_imputed)

       # sum=0

       # for i in range(len(catagorical1)):
          #  if catagorical1[i] == catagorical_imputed1[i]:
           #     sum=sum+1;
            #print(i)
        #print(sum)
      #  print("AE : ",sum/len(catagorical1))

    #calculating root mean sqaure error For numerical columns
    #if (numeric.size!=0):
      #  numeric1 = np.ravel(numeric)
      #  numeric_imputed1 = np.ravel(numeric_imputed)


      #  rmse = sqrt(mean_squared_error(numeric1, numeric_imputed1))

      #  print("Root Mean Squared Error : ",rmse)
      #  result =(np.linalg.norm((numeric_imputed - numeric),'fro'))  / (np.linalg.norm(numeric,'fro'))
     #   print("Normalized Root Mean Squared Error : ",result)





'''
from sklearn.metrics import mean_squared_error
import numpy as np
from math import sqrt

numeric1 = np.ravel(numeric)
numeric_imputed1 = np.ravel(numeric_imputed)




rmse = sqrt(mean_squared_error(numeric1, numeric_imputed1))

print(rmse)


catagorical1 = np.ravel(catagorical)
catagorical_imputed1 = np.ravel(catagorical_imputed)

sum=0
print(len(catagorical1))
for i in range(len(catagorical1)):
    
    if catagorical1[i] == catagorical_imputed1[i]:
    
        sum=sum+1;
        #print(i)
        
print(sum)


print(sum/len(catagorical1))
'''




