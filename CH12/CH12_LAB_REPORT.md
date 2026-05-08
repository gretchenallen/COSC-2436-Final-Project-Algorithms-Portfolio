# Lab Report #12 Regression

## Student Information
**Name:** Gretchen Allen
**Date:** 05/08/2026
**Algorithm Analysis:** K-Nearest Neighbors (KNN) Regression for Bakery Loaf Prediction

---

## Algorithm Understanding

**What type of problem is this algorithm solving?**
Regression problem

**How does KNN regression differ from KNN classification?**
KNN regression outputs a predicted numerical outcome based on the average of the k nearest neighbors, while knn classification places each data point in a category based on the majority class among its k nearest neighbors.

**What does the "K" in KNN represent, and why did we choose k=4 for this problem?**
K represents the number of nearby data points being considered for either classification or regression in relation to a particular data point.
K=4 is a reasonable K value for the bakery loaves problem because it provides an average that can smooth over outliers but still reflect localized patterns. 

**In your own words, explain how the model produces a prediction for a new day.**
After inputting today's conditions (the features for this scenario) the model will calculate the distance between today's data point and all historical data points using Euclidian distance. The model then identifies the K nearest neighbors based on the calculated distances and takes the average of their values for number of loaves sold. This average is the prediction for the number of loaves that should be baked today.


---

## Implementation Questions

**Why do we separate the DataFrame into features (X) and target (y) before training?**
A clear distinction between input variables, or features (X), and and output or target that the model is trying to predict (y) is needed for many machine learning models.

**Why must the input to `model.predict()` be a 2D array (e.g., `[[4, 1, 0]]`) instead of a 1D array (`[4, 1, 0]`)?**
A feature set (X) must be saved in two dimensions so that both the data point itself along with any relevant features of that data point may be represented in the same place.

**What does `.fit(X, y)` actually do for a KNN model? (Hint: it's different from most other ML algorithms.)**
Unlike many machine learning models, KNN is a "lazy learner", meaning it simply stores the data it collects for later use. .fit() is the method used for accomplishing this. 

**Why do we use `.values` when extracting columns from the DataFrame?**
This is what converts DataFrame columns into numpy arrays, which is a format required by many machine learning libraries.

---

## Extension: Choosing K

**What would happen if we set k=1? What are the risks?**
If K=1 then only the nearest neighbor is considered in any predictions, so the model becomes overly sensitive to noise and outliers. This leads to large prediction errors since no anomolies are averaged out.

**What would happen if we set k=20 (the size of the entire dataset)? What does the model become?**
Every prediction would just be the global average of all given datapoints. This effectively discards the benefits of local-based decision-making that KNN provides, since the model will become insensitive to any changes in the input features.

**How would you decide what value of k is best for a given dataset?**
There are different techniques that can be used to achieve this, such as cross-validation which will evaluate performance across different values of k, or the calculation of error metrics (i.e. Mean Squared Error or Root Mean Squared Error) for different k values to find the one with the lowest error.

---

## Extension: Distance and Feature Scaling

**KNN uses distance to find "nearest" neighbors. Our features have very different ranges: weather is 1–5, but weekend_holiday and game_on are 0/1. Why could this be a problem?**
Since the weather has a larger range, it may dominate the distance calculation and over-shadow the contribution of the other two features. This imbalance can lead to biased predictions and reduce model accuracy.

**Give an example of two days where the weather feature would unfairly dominate the distance calculation.**
Day 1:
Weather: 5
Weekend/Holiday: 1
Game On: 0
Day 2:
Weather: 3
Weekend/Holiday: 1
Game On: 0
If you compare these days using Euclidean distance without scaling:
Weather difference: 5 - 3 = 2
Weekend/Holiday difference: 1 - 1 = 0
Game On difference: 0 - 0 = 0
The distance between these points would be dominated by the weather difference, even though the other features are identical.

**How would you modify the data preparation step to fix this? (Hint: look up "feature scaling" or "StandardScaler".)**
To fix this problem, you can use a method of feature scaling such as StandardScaler from scikt-learn. StandardScaler standardizes features by removing the mean and scaling to unit variance.

---

## Reflection Questions

**What is a limitation of KNN regression? Provide a scenario where it would make a poor prediction.**
KNN struggles with imbalanced datasets, where some outcomes are much less frequent than others. For example, with the bakery/loaves problem there could be a day when the weather was absolutely terrible, it was not a weekend or holiday, and there was no game, but a record number of loaves were sold because the power was out in the whole town. The model would not have been able to predict this outcome and that day would become an outlier in the set of data points which may skew future predictions.

**Our dataset only has 20 days of data. How might the predictions change if we had 2,000 days of data instead?**
More data points will improve the model's accuracy in making predictions since the effect of any outliers are buffered, therefore making the model more reliable. 

**What other features (beyond weather, weekend/holiday, and game day) could the bakery collect to improve predictions?**
More specific information on each of the currently tracked features could be very helpful, such as tracking the specific temperature each day, the actual day of the week, or which specific holiday it is. 

**KNN is sometimes called a "lazy learning" algorithm because it does almost no work during training. What is the tradeoff at prediction time?**
[Your explanation — slower predictions, must compare against every training point]

**The autograder expects a prediction of approximately 70.5 loaves for today's conditions. Manually look at the dataset and identify which 4 historical days you think the model is averaging. Do their loaf counts average to 70.5?**
[Your analysis]

**Why might a bakery prefer a slightly inaccurate ML prediction over a human guess for daily loaf counts?**
[Your explanation — consistency, scalability, data-driven decisions, reduced waste]

**If the bakery wanted to MINIMIZE waste (unsold loaves) rather than just predict accurately, how might you change the approach?**
[Your explanation — e.g., predict slightly under, use a different loss function, factor in cost of waste vs. lost sales]
