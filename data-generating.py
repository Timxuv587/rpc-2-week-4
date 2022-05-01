# This is a sample Python script.
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#Set up the student that need class recommendation
#Our goal is to predict his preference for other courses that he never took


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    course_info = pd.read_csv('Northwestern_course_information.csv')
    #Fill in the empty value with 0
    course_info.describe()
    size = np.array((20,50,100,200))
    course_info["class size"] = np.random.choice(size, size=len(course_info))
    print(course_info.head())
    course_df = pd.read_csv('ratings.csv')
    rate = np.array((np.nan,np.nan,np.nan,np.nan,1,2,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6))
    new_row = np.random.choice(rate, (10,len(course_df.columns)-1))
    print(new_row)
    arr = np.arange(34,44).reshape(10,1)
    added=np.concatenate((arr, new_row), axis=1)
    added_df = pd.DataFrame(added,columns=course_df.columns)
    print(added_df)
    course_df = course_df.append(added_df)
    print(course_df)



