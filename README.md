# Comparison of Daily COVID19 cases spatial prediction models based on features' importance and analysis of related mobility restriction measures taken by the Government of India

### The Team
Poojan Vachharajani,
Mohit Chaurasiya,
Arnav Gupta,
Vinamra Harkar

Supervision & Support: Prof. Luo Wei, National University of Singapore

### Introduction
This project implements various models to predict daily COVID-19 cases primarily using spatial data provided by Facebook's (Meta's) Data For Good program. Various Machine learning and Deep learning models are compared on the basis of the accuracy of predicted values. This project also justifies the importance of several features such as daily COVID testing statistics and daily vaccination statistics. We intent to evaluate union and state governments' policy decisions around mobility restrictions and lockdowns based on our COVID-19 spread prediction results and found a strong significance of features like daily testing and vaccination statistics for better performance.

### Data
Population Movement and Population Density data was taken from Facebook (Meta) Data For Good Portal (https://dataforgood.facebook.com/) and the COVID-19 data was taken from (https://www.covid19india.org/)

### Results

| Model                    | Feature/s                  | RMSE    |
| :-----------------       | :------------------------- | -------:|
| Linear Regression        | Spatial                    | 6350.93 |
| Linear Regression        | Spatial+Vaccinations       | 7426.58 |
| Linear Regression        | Spatial+Tests              | 8528.57 |
| Linear Regression        | Spatial+Vaccinations+Tests | 7735.01 |
| Logistic Regression      | Spatial                    | 1383.73 |
| Logistic Regression      | Spatial+Vaccinations       | 1324.25 |
| Logistic Regression      | Spatial+Tests              | 1383.73 |
| Logistic Regression      | Spatial+Vaccinations+Tests | 3370.27 |
| Random Forest Regression | Spatial                    | 1765.45 |
| Random Forest Regression | Spatial+Vaccinations       | 2227.77 |
| Random Forest Regression | Spatial+Tests              | 1583.89 |
| Random Forest Regression | Spatial+Vaccinations+Tests | 2414.82 |
| RNN with LSTM            | Spatial                    | 1242.15 |
| RNN with LSTM            | Spatial+Vaccinations       | 1343.72 |
| RNN with LSTM            | Spatial+Tests              | 899.97  |
| RNN with LSTM            | Spatial+Vaccinations+Tests | 1039.67 |

### Summary
• RNN LSTM models, best with Tests as an additi onal feature

• Logistic Regression models, best with Vaccination as an additional feature

• Random Forest Regression models, best with Tests as an additi onal feature 

• Linear Regression models (benchmarking)

