# This is a sample Python script.
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#Set up the student that need class recommendation
#Our goal is to predict his preference for other courses that he never took
input =  {"COMP_SCI110": 5,
         "ECON201":4,
         "ECON310":3,
         "EARTH101":6
         }

k = 5


#class 1 class are name of class

def compare_schedule(course_info, recommendation, target):
    for sample in recommendation:
        if(compare_time(course_info,sample[:-3],sample[-3:],target[:-3],target[-3:])):
            return 0
    return 1

def compare_time(course_info, dept1, num1,dept2, num2):
    time1 = course_info[course_info['dept/pgm']==dept1][course_info['number']==str(num1)].reset_index()
    time2 = course_info[course_info['dept/pgm']==dept2][course_info['number']==str(num2)].reset_index()
    #print(str(time1) + " " + str(time2))
    if(time1["date"].equals(time2["date"]) or
            (time1["date"].equals("MoWeFr") and time2["date"].equals("MoWe")) or
            (time2["date"].equals("MoWeFr") and time1["date"].equals("MoWe"))):
        start = [pd.to_datetime(time1["start time"]),pd.to_datetime(time2["start time"])]
        end = [pd.to_datetime(time1["end time"]),pd.to_datetime(time2["end time"])]
        #print(np.max(start))
        if( np.max(start) <= np.min(end)):
            return 0
        return 1
#

def compare_schedule(course_info, recommendation, target):
    for sample in recommendation:

        if(compare_time(course_info, sample[:-3], sample[-3:], target[:-3], target[-3:]) == 0):
            return 0
    return 1



def make_recommendation(rate_df, k, x):
    model = NearestNeighbors(n_neighbors=k,metric='euclidean')

    #filter the data, leave only the class that the student has rated
    filtered_df = rate_df.loc[:,x.index]

    model.fit(filtered_df)
    distance,result = model.kneighbors([x.array])
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    recommendations = []
    distributions = ['II', 'III']
    course_info = pd.read_csv('Northwestern_course_information_new.csv')

    # print(course_info)
    course_info['ClassName'] = course_info['dept/pgm'].astype(str) + course_info['number'].astype(str)



    #class_names = course_subset['ClassName']
    # x = pd.Series(input)
    # results = make_recommendation(course_info, k, x)
    # prediction = course_info.iloc[results[0], 1:].sum() / k
    # print(compare_time(course_info, "COMP_SCI", 101, "COMP_SCI", 110))

    rate_df = pd.read_csv('ratings_new.csv')
    # Fill in the empty value with 0
    rate_df = rate_df.fillna(0)
    x = pd.Series(input)
    results = make_recommendation(rate_df, k, x)
    main_prediction = rate_df.iloc[results[0], 1:].sum() / k
    main_recommendation = main_prediction[~main_prediction.index.isin(x.index)].sort_values(ascending=False)
    # prediction.


    len_courses = 4
    distros = [0,0,"II", "III"]
    #print(prediction.index[5])
    for j in range(len_courses):
        i = 0
        if distros[j] == 0:
            predictions = main_recommendation
        else:
            # filtering case
            # filter the courses by the distribution  I want
            course_subset = course_info[course_info['area'] == distros[j]]
            class_names = course_subset['ClassName']
            predictions = main_recommendation.filter(items=class_names)
        while(compare_schedule(course_info, recommendations, predictions.index[i]) == 0 or predictions.index[i] in recommendations):
            i += 1
        recommendations.append(predictions.index[i])
        print(recommendations)
    print(recommendations)

    # print(prediction)

