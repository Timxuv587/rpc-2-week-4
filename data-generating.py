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
    size = np.array((20,50,100,200))
    date = np.array(("MoWeFr","TuTh","MoWe"))
    start_time = np.array(("8:00 PM","9:00 PM","10:00 PM"))
    end_time = np.array(("9:00 PM","10:00 PM", "11:00 PM"))
    course_info["class size"] = np.random.choice(size, size=len(course_info))
    course_info["date"] = np.random.choice(date, size=len(course_info))
    course_info["start time"] = np.random.choice(start_time, size=len(course_info))
    course_info["end time"] = np.random.choice(end_time, size=len(course_info))
    print(course_info.head())
    course_info.to_csv('Northwestern_course_information_new.csv')

    course_df = pd.read_csv('ratings.csv')
    rate = np.array((np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,1,2,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6))
    new_row = np.random.choice(rate, (10,len(course_df.columns)-1))
    print(new_row)
    arr = np.arange(34,44).reshape(10,1)
    added=np.concatenate((arr, new_row), axis=1)
    added_df = pd.DataFrame(added,columns=course_df.columns)
    print(added_df)
    course_df = course_df.append(added_df)
    class_list = ["COMP_SCI349","COMP_SCI110","COMP_SCI348","COMP_SCI336","ECON301","ECON201","ECON339","ECON310","COMP_SCI150","ASTRON103","EARTH101","ANTHRO213","COG SCI110"]
    for c in class_list:
        course_df[c] = np.random.choice(rate, size=len(course_df))
    print(course_df)
    course_df.to_csv('ratings_new.csv',index=False)