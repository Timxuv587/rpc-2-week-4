# This is a sample Python script.
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#Set up the student that need class recommendation
#Our goal is to predict his preference for other courses that he never took
input =  {"COMP_SCI349": 5,
         "ECON201":4,
         "ECON310":3,
         "EARTH101":6
         }

k = 5

def make_recommendation(course_df, k, x):
    model = NearestNeighbors(n_neighbors=k,metric='euclidean')

    #filter the data, leave only the class that the student has rated
    filtered_df = course_df.loc[:,x.index]

    model.fit(filtered_df)
    distance,result = model.kneighbors([x.array])
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    distributions = ['II', 'III']
    course_info = pd.read_csv('Northwestern_course_information.csv')
    course_info['ClassName'] = course_info['dept/pgm'].astype(str) + course_info['number'].astype(str)
    course_subset = course_info[course_info['area'].isin(distributions)]
    class_names = course_subset['ClassName']
    course_df = pd.read_csv('ratings_new.csv')
    # Fill in the empty value with 0
    course_df = course_df.fillna(0)
    x = pd.Series(input)
    results = make_recommendation(course_df, k, x)
    print(course_df.iloc[results[0], 1:])
    prediction = course_df.iloc[results[0], 1:].sum() / k
    print(class_names)
    print(prediction.filter(items=class_names))
    print(prediction.index)

