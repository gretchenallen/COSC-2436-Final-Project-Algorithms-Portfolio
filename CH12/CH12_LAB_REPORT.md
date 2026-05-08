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
KNN regression outputs a predicted 

**What does the "K" in KNN represent, and why did we choose k=4 for this problem?**
[Your answer]

**In your own words, explain how the model produces a prediction for a new day.**
[Your explanation — should mention finding the k closest historical days and averaging their loaf counts]

---

## Implementation Questions

**Why do we separate the DataFrame into features (X) and target (y) before training?**
[Your explanation]

**Why must the input to `model.predict()` be a 2D array (e.g., `[[4, 1, 0]]`) instead of a 1D array (`[4, 1, 0]`)?**
[Your explanation]

**What does `.fit(X, y)` actually do for a KNN model? (Hint: it's different from most other ML algorithms.)**
[Your explanation — KNN is a "lazy learner" that mostly just stores the data]

**Why do we use `.values` when extracting columns from the DataFrame?**
[Your explanation]

---

## Extension: Choosing K

**What would happen if we set k=1? What are the risks?**
[Your explanation — overfitting, sensitive to noise]

**What would happen if we set k=20 (the size of the entire dataset)? What does the model become?**
[Your explanation — every prediction would be the global average]

**How would you decide what value of k is best for a given dataset?**
[Your explanation — cross-validation, error metrics on a validation set]

---

## Extension: Distance and Feature Scaling

**KNN uses distance to find "nearest" neighbors. Our features have very different ranges: weather is 1–5, but weekend_holiday and game_on are 0/1. Why could this be a problem?**
[Your explanation — features with larger ranges dominate the distance calculation]

**Give an example of two days where the weather feature would unfairly dominate the distance calculation.**
[Your example]

**How would you modify the data preparation step to fix this? (Hint: look up "feature scaling" or "StandardScaler".)**
[Your explanation]

---

## Reflection Questions

**What is a limitation of KNN regression? Provide a scenario where it would make a poor prediction.**
[Your explanation — e.g., predicting a day with conditions far outside any historical data]

**Our dataset only has 20 days of data. How might the predictions change if we had 2,000 days of data instead?**
[Your explanation]

**What other features (beyond weather, weekend/holiday, and game day) could the bakery collect to improve predictions?**
[Your answer — e.g., temperature, season, local events, day of week, social media buzz]

**KNN is sometimes called a "lazy learning" algorithm because it does almost no work during training. What is the tradeoff at prediction time?**
[Your explanation — slower predictions, must compare against every training point]

**The autograder expects a prediction of approximately 70.5 loaves for today's conditions. Manually look at the dataset and identify which 4 historical days you think the model is averaging. Do their loaf counts average to 70.5?**
[Your analysis]

**Why might a bakery prefer a slightly inaccurate ML prediction over a human guess for daily loaf counts?**
[Your explanation — consistency, scalability, data-driven decisions, reduced waste]

**If the bakery wanted to MINIMIZE waste (unsold loaves) rather than just predict accurately, how might you change the approach?**
[Your explanation — e.g., predict slightly under, use a different loss function, factor in cost of waste vs. lost sales]
