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
Python, Tableau, Jupyter Notebook, Google Geocode API, MS Excel, MS PPT

## Datasets:
   * [Diabetes ML](https://www.kaggle.com/johndasilva/diabetes/data)
   * [WHO World Figures](https://www.who.int/diabetes/facts/world_figures/en/index5.html)
   * [Treatment Centers](/resources/data/DPRP_Results_Full_RegistryAug_05_2020.csv)

## ETL
All the data and jupyter notebooks used for this project can be found in the [resources](/resources) folder.

<h3>Diabetes ML</h3>
This dataset from frankfurt patients was already clean so no intense ETL was done outside of making sure there was enough data to process machine learning models. 

<h3>WHO World Figures</h3>
The WHO website didn't have a readily available csv so this information from the website needed to be pulled. There was an error on the website that prevented us from getting the diabetes data from Europe. In order to get that information,....

<h3>Treatment_Cleaning Notebook</h3>
This notebook contains the cleaning for the DRPR treatment centers csv in preparation for Tableau. This csv didn't contain the latitude and longitude needed to map out the treatment centers. The first step was importing the dependencies needed to make an API call with Google Geocode. After getting the data and adding the coordinates to the dataframe, a new csv was exported. The exported csv was then used to clean up any missing coordinates, renaming and reorganizing columns to fit the Tableau hierarchy, editing NaNs for missing websites and second address lines, and splitting up the type of patients that the clinic provides care for. A new csv was then exported to be used in Tableau.
<br>
<br>
The next section goes into the ETL and model testing for the best model to use for our website.

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


<h3>III.	Tensor Flow Model</h3>
Finally, we also ran a Tensor Flow model that utilized several imports from sklearn and keras including train test split again, min max scaler, label encoder, sequential, and to_categorical among others.  We split the data in training and testing, compiled the model, scaled the model, and fit the model. 


We were able to obtain a model accuracy of 78.39% and the model loss was 43.95%. Using the tensor flow model, we obtained a diabetes risk score between 0 and 1 as opposed to only 0’s and 1’s. Our analytical capabilities were greatly increased from this output as shown by the scatter plots in our tableau analysis. 


Here are some insights that we can garner:<br>
There were 99 test results with score less than 0.1 and 97 had an actual outcome of 0.  Only 2.02% of individuals with a score less than 0.1 had an actual outcome of 1 which represents a high risk of diabetes.<br>
There were 159 test results with score less than 0.2 and 153 had an actual outcome of 0. Only 3.77% of individuals with a score less than 0.2 had an actual outcome of 1.<br>
There were 200 test results with score less than 0.3 and 185 had an actual outcome of 0. Only 7.5% of individuals with a score less than 0.3 had an actual outcome of 1.<br>
There were 236 test results with score less than 0.4 and 216 had an actual outcome of 0. Only 8.47% of individuals with a score less than 0.4 had an actual outcome of 1.<br>
There were 281 test results with score less than 0.5 and 246 had an actual outcome of 0. Only 12.46% of individuals with a score less than 0.1 had an actual outcome of 1. As your score increases, the likelihood a high risk for diabetes increases, but even as the score approaches 0.5, the ratio is still only 12.46%.<br>

Next, we’ll take a look from the other perspective. <br>
There were 59 test results with score greater than 0.9 and 51 had an actual outcome of 1.  86.44% of individuals with a score more than 0.9 had an actual outcome of 1 which represents a high risk of diabetes. It’s safe to say that if your score is above 0.9, your risk of diabetes is very high.<br>
There were 98 test results with score greater than 0.8 and 77 had an actual outcome of 1. The percentage drops to 78.57%, which still means the probability of diabetes remains high/very high.<br>
Furthermore, there were 141 test results with score greater than 0.7 and 100 had an actual outcome of 1 or 70.92% which still remains high.<br>
Lastly, the results for over 0.6 and over 0.5 are 113/176 or 64.20% and 128/219 or 58.45%<br>

![Dark Blue Diabetes Picture with Red iPad](/static/assets/img/TensorImage.PNG)


## Findings/...what to find on the website??

World Map 2000 & 2030 (tableau visuals)

About the Test Subjects(tableau visuals)

## Limitations
At the time of this project, WHO had a website error that prevented us from pulling data from Europe and a few other countries. After finding most of that data, we came to the conclusion that some areas that data may not have been collected from some of those places.

Our dataset for the machinie learning aspect only contained data from the Frankfurt population. Despite diabetes being a well known chronic condition, datasets from other regions were not available at this time.

In the future, we would be interested in obtaining additional demographic information of the people living with diabetes. Government organizations and philanthopic groups didn't provide that type of information for public use.

## Resources

* Images were provided by unsplash, CDC, and Jordon Cheung(the readme.md image).

* Additional information about diabetes was provided by CDC, WebMD, NIH, and Mayo Clinic.
