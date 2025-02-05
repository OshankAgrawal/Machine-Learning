import numpy as np
import pandas as pd
from itertools import product

csv_file_data=pd.read_csv('Data.csv')
#print(csv_file_data)

def create_sementical_distinct_hypothesis(data):
    # Extract the examples of the DataSet
    examples=np.array(data)[:,:-1]
    # print(examples)

    number_of_features=len(examples[0])
    #print(number_of_features)

    # Transpose the examples so that it is easy to make the set of the values of feature
    feature_transpose=np.transpose(examples)
    # print(feature_transpose)

    # Declare a 2D Array which store all the features set
    feature=[[]]*number_of_features
    # print(feature)

    # Iterations which make the sets of features value and also convert them into the 2D Array
    for i in range(len(feature_transpose)):
        my_set=set()
        for j in range(len(feature_transpose[0])):
            my_set.add(feature_transpose[i][j])
        # print(my_set)
        feature[i]=list(my_set)
    # print(feature)

    # Append the general condition in all the feature vectors
    for i in range(len(feature)):
        feature[i].append('?')
    # print(feature)

    # Create the Sementical Distinct Hypothesis
    sementical_distinct_hypothesis=list(product(*feature))
    # print(sementical_distinct_hypothesis)
    # print(len(sementical_distinct_hypothesis))

    # Return the Sementical Distinct Hypothesis
    return sementical_distinct_hypothesis

def compare_feature_Vector(arr1,arr2):
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

def check_hypothesis(hypothesis,instance,target):
    # Check Hypothesis is consistent or not
    # If consistent return True otherwise return False
    for i,val in enumerate(instance):
        if compare_feature_Vector(hypothesis,val):
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

def create_version_space(csv_file_data):
    semantical_distinct=create_sementical_distinct_hypothesis(csv_file_data)

    data=np.array(csv_file_data)[:,:-1]
    # print(data)

    target=np.array(csv_file_data)[:,-1]
    # print(target)

    # It appends all the consistent hypothesis to the Version Space
    version_space=[]
    for i in semantical_distinct:
        if check_hypothesis(i,data,target):
            version_space.append(i)
    return version_space

version_space=create_version_space(csv_file_data)
print(version_space)