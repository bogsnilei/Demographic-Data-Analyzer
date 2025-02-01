import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read raw data
    data = pd.read_csv('adult.data.csv')

    #Count people count for every race
    Race_count = data['race'].value_counts()
    print("Every people each", Race_count, '\n')

    # Calculate the average age of men
    averageMenAge = round(data[data['sex'] == 'Male']['age'].mean(), 2)
    print("Average age of men: ", averageMenAge, '\n')

    # Calculate the percentage of people with a Bachelor's degree
    BachelorsPercnt = round(data[data['education'] == 'Bachelors'].shape[0] / data.shape[0] * 100, 2)
    print("Percentage of people with a Bachelor's degree: ", BachelorsPercnt, "%", '\n')

    # Filter data
    q1 = data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    q2 = data['salary'] == '>50K'

    #Percentage of people with advanced education make more than 50K
    HigherEducation = round((q1 & q2).sum() / q1.sum() * 100, 2)
    print('Percentage of people with Higher Education making >50k Salary: ', HigherEducation, '%')
    #Percentage of people without advanced education make more than 50K
    wOHigherEducation = round((~q1 & q2).sum() / q1.sum() * 100, 2)
    print('Percentage of people without Higehr Education making >50k Salary: ', wOHigherEducation, '%', '\n')

    #Minimum hours per week
    minWorkHrs = data['hours-per-week'].min()
    print("Minimum hours per week: ", minWorkHrs, 'hour(s)', '\n')

    #Percentage of people working the minimum hours per week have a salary of >50K
    minHrsWkWorkersNum = data[data['hours-per-week'] == minWorkHrs].shape[0]
    minHrsWkWorkersPercnt = round(data[(data['hours-per-week'] == minWorkHrs) & (data['salary'] == '>50K')].shape[0] / minHrsWkWorkersNum * 100, 2)

    print("Percentage of people working the minimum hours per week have a salary of >50K: ", minHrsWkWorkersPercnt, '%', '\n')

    #What country has the highest percentage of people that earn >50K?
    highestCountry = data['native-country'].value_counts() 
    countrySalary = data[data['salary'] == '>50K']['native-country'].value_counts()
    HighestCountrySalary = countrySalary.idxmax()
    HighestCountrySalaryPercnt = round(countrySalary.max() / highestCountry.max() * 100, 2)

    print('Workers Count in : ', highestCountry.idxmax(), 'is', highestCountry.max()) 
    print('Workers with >50k Salary', countrySalary.max(), 'people')
    print('Highest percentage of people that earn >50K: ', HighestCountrySalaryPercnt, '%', '\n')

    #Identify the most popular occupation for those who earn >50K in India.

    IndiaSalary = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]['occupation'].value_counts()
    MostPopularOccupation = IndiaSalary.idxmax()
    print('Most popular occupation for those who earn >50K in India: ', MostPopularOccupation, '\n')

    




