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

28.35%	Glucose<br>
17.26%	BMI<br>
16.37%	Age<br>
13.57%	DiabetesPedigreeFunction<br>
9.26%	BloodPressure<br>
8.04%	Insulin<br>
7.14%	SkinThickness<br>


For the next 5 combinations, we removed the feature with lowest importance. Here are the results with their corresponding scores:

Score: 0.958

29.70%	Glucose<br>
18.15%	BMI<br>
17.47%	Age<br>
14.95%	DiabetesPedigreeFunction<br>
10.52%	BloodPressure<br>
9.21%	Insulin<br>


Score: 0.962

32.42%	Glucose<br>
20.90%	BMI<br>
18.50%	Age<br>
17.00%	DiabetesPedigreeFunction<br>
11.17%	BloodPressure<br>


Score: 0.966

36.41%	Glucose<br>
23.83%	BMI<br>
20.12%	Age<br>
19.64%	DiabetesPedigreeFunction<br>


Score: 0.962

42.23%	Glucose<br>
32.72%	BMI<br>
25.06%	Age<br>


Score: 0.966

52.23%	Glucose<br>
47.77%	BMI<br>


Next, we ran the classifier with only Glucose, and only with BMI. We chose Glucose because according to this model it always had the highest feature importance. We also ran BMI alone because it was always second highest. BMI is easily known information for any individual since it is a simple calculation based on height and weight. The score for Glucose alone was 0.754 and the score for BMI alone was 0.742. 

Lastly, we decided to run a model with Age and BMI. Again, our reasoning behind this decision is that this is readily known information for any individual. Here are the score and feature importance for this combination. 


Score: 0.924

66.43%	BMI<br>
33.57%	Age<br>


<h3> II.	Diabetes – Recognition Tester </h3>

The second machine learning model we ran was a Diabetes recognition tester that used sklearn to split the model into training and testing samples. Our dataset contained 2,000 records in total. The training sample contained 1,500 records and the testing sample contained 500 records. From that split we used sklearn to run a logistic regression. This model was used to predict an outcome based on the different combinations of features. An outcome that returns a ‘0’ means the individual is predicted to have low diabetes risk. Conversely, an outcome that returns a ‘1’ means the individual is predicted to have high diabetes risk. 


We ran the recognition model for 9 different combinations of features. When we included all the features, the model was able to predict the outcome correctly 78.8% of the time or 394 out of 500 records from the testing sample.  Here are results from the 8 other combinations.

76.6% "Age","Glucose","DiabetesPedigreeFunction","BloodPressure","SkinThickness","BMI"<br>
383 out of 500 correct predictions

76.6% "Age","Glucose","DiabetesPedigreeFunction","SkinThickness","BMI"<br>
383 out of 500 correct predictions

77.4% "Age","Glucose","DiabetesPedigreeFunction","BMI"<br>
387 out of 500 correct predictions

77.2% "Age","Glucose","BMI"<br>
386 out of 500 correct predictions

70.0% "Age","BMI"<br>
350 out of 500 correct predictions

76.4% "Glucose","BMI"<br>
382 out of 500 correct predictions

74.0% "Glucose"<br>
370 out of 500 correct predictions

69.2% "BMI"<br>
346 out of 500 correct predictions

We decided to use the ‘complete’ model that contained all the features for the diabetes predictor on our website since it was able to predict the outcomes most accurately.  



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
