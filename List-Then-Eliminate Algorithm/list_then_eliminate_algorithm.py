import numpy as np
import pandas as pd

def create_version_space(f1,f2):
    f1.append('?')
    f2.append('?')

    # Create Semantical Distinct Hypothesis Space
    semantical_distinct=[]
    for i in f1:
        for j in f2:
            semantical_distinct.append([i,j])

    new_item=['$']*2
    semantical_distinct.append(new_item)

    return semantical_distinct

def compare_feature_vector(arr1,arr2):
     # Check the corresponding feature value is acceptable or not
    # if acceptable return True otherwise return False
    length=len(arr1)
    for i in range(length):
        if arr1[i]==arr2[i]:
            pass
        elif arr1[i]=='?':
            pass
        else:
            return False
    return True

def check_hypothesis(hypothesis,data,target):
    # Check Hypothesis is consistent or not
    # If consistent return True otherwise return False
    for i,val in enumerate(data):
        if compare_feature_vector(hypothesis,val):
            if target[i]=='Yes':
                pass
            else:
                return False
        else:
            if target[i]=='No':
                pass
            else:
                return False
    return True

def eliminate_hypothesis(semantical_distinct,data,target):
    # It appends all the consistent hypothesis to the Version Space
    version_space=[]
    for i in semantical_distinct:
        if check_hypothesis(i,data,target):
            version_space.append(i)
    return version_space


f1=['A','B','C']
f2=['X','Y','Z']
version_space=create_version_space(f1,f2)
# print("Version Space:- ",version_space)

csv_file_data=pd.read_csv('Data.csv')
#print(csv_file_data)

data=np.array(csv_file_data)[:,:-1]
#print(data)

target=np.array(csv_file_data)[:,-1]
#print(target)

eliminated_version_space=eliminate_hypothesis(version_space,data,target)

print(eliminated_version_space)


