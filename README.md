# DiabetesML
![Dark Blue Diabetes Picture with Red iPad](/static/assets/img/diabetes_digital.png)

## About Us 

Team Members: Ryla Almario, Sanjive Agarwal, Andrew Lau, Mitesh Parekh, Tamala Chipeta

Our Website:

## Background
Diabetes continues to be a growing chronic disease around the world. The CDC states that [122 million Americans](https://www.cdc.gov/diabetes/library/socialmedia/infocards.html) have this chronic disease. In addition, the International Diabetes Federation(IDF) has found that 463 million individuals worldwide with a projected rise of up to [700 million people](https://www.idf.org/aboutdiabetes/what-is-diabetes/facts-figures.html) by 2045. 

Even though diabetes is a well known health condidtion, there are still a lot of misconcetions. Many believe that diabetes is connected to obesity but many studies have proven that it’s not the case! Also, diabetes type 1 & 2 aren’t the only types that you could get.

Because of this, early detection is key which is why we decided to make a quick questionnaire for you as the first step to check if you have diabetes. 

We also want to provide you with additional information about diabetes so that you can stay informed about this growing chronic illness.


## Tools and Programs
Tools: Tableau, Jupyter Notebook, MS Excel
Programs: Python

## Datasets:
   * [Diabetes ML](https://www.kaggle.com/johndasilva/diabetes/data)
   * [WHO World Figures](https://www.who.int/diabetes/facts/world_figures/en/index5.html)
   * [Treatment Centers](/resources/data/DPRP_Results_Full_RegistryAug_05_2020.csv)

## ETL???

## Machine Learning

For the Machine Learning element of our project, we ran 3 different types of models. 

<h3>I.	Random Forest Classifier</h3>

We ran a Trees model or a Random Forest Classifier. This model gave us insight on the importance of the 8 features used to determine risk of diabetes in individuals. As a reminder, the 8 features are "Age", "Glucose", "DiabetesPedigreeFunction", "BloodPressure", "Insulin", "SkinThickness", "BMI", and “Pregancies”.  

From these 8 features, we ran the Random Forest Classifier for 9 different combinations.  We started with "Age","Glucose","DiabetesPedigreeFunction","BloodPressure","Insulin","SkinThickness","BMI". It returned a score of 0.956. 

Here is the feature importance for this combination.
28.35%	Glucose

17.26%	BMI

16.37%	Age

13.57%	DiabetesPedigreeFunction

9.26%	BloodPressure

8.04%	Insulin

7.14%	SkinThickness


For the next 5 combinations, we removed the feature with lowest importance. Here are the results with their corresponding scores:

Score: 0.958

29.70%	Glucose

18.15%	BMI

17.47%	Age

14.95%	DiabetesPedigreeFunction

10.52%	BloodPressure

9.21%	Insulin


Score: 0.962

32.42%	Glucose

20.90%	BMI

18.50%	Age

17.00%	DiabetesPedigreeFunction

11.17%	BloodPressure


Score: 0.966

36.41%	Glucose

23.83%	BMI

20.12%	Age

19.64%	DiabetesPedigreeFunction


Score: 0.962

42.23%	Glucose

32.72%	BMI

25.06%	Age


Score: 0.966

52.23%	Glucose

47.77%	BMI


Next, we ran the classifier with only Glucose, and only with BMI. We chose Glucose because according to this model it always had the highest feature importance. We also ran BMI alone because it was always second highest. BMI is easily known information for any individual since it is a simple calculation based on height and weight. The score for Glucose alone was 0.754 and the score for BMI alone was 0.742. 

Lastly, we decided to run a model with Age and BMI. Again, our reasoning behind this decision is that this is readily known information for any individual. Here are the score and feature importance for this combination. 


Score: 0.924

66.43%	BMI

33.57%	Age




Behind the Prediction tests?

Accuracy(tableau visuals)


Feature Importance(tableau visuals)


## Findings/...what to find on the website??

World Map 2000 & 2030 (tableau visuals)

About the Test Subjects(tableau visuals)

## Limitations
At the time of this project, WHO had a website error that prevented us from pulling data from Europe and a few other countries. After finding most of that data, we came to the conclusion that some areas that data may not have been collected from some of those places.

Our dataset for the machinie learning aspect only contained data from the Frankfurt population. Despite diabetes being a well known chronic condition, datasets from other regions were not available at this time.

In the future, we would be interested in obtaining additional demographic information of the people living with diabetes. Government organizations and philanthopic groups didn't provide that type of information for public use.

## Resources
