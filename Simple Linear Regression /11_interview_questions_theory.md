# 🎯 11 - Interview Questions: Simple Linear Regression (SLR)

This notebook covers the most commonly asked **Simple Linear Regression** questions in interviews and tech assessments — with theory and explanations.

---

## 1. What is Simple Linear Regression?

Simple Linear Regression is a statistical method used to model the relationship between a single independent variable (X) and a dependent variable (Y) by fitting a straight line (Y = θ₀ + θ₁X).

---

## 2. What are the assumptions of Linear Regression?

- Linearity
- Homoscedasticity (equal variance)
- Independence of errors
- Normality of errors
- No multicollinearity (for MLR)

---

## 3. What is the cost function used in Linear Regression?

Mean Squared Error (MSE):  
\[
J(\theta) = \frac{1}{n} \sum_{i=1}^{n}(y_i - \hat{y}_i)^2
\]

---

## 4. How do we minimize the cost function?

Using **Gradient Descent** or **Normal Equation** (closed-form solution).

---

## 5. What is Gradient Descent in the context of Linear Regression?

It's an optimization algorithm used to minimize the MSE by updating parameters (θ₀, θ₁) in the opposite direction of the gradient of the cost function.

---

## 6. How does learning rate (α) affect training?

- Too small → slow convergence
- Too large → overshooting or divergence
- Optimal α → fast, stable convergence

---

## 7. Can SLR be solved without Gradient Descent?

Yes, using the **Normal Equation**:
\[
\theta = (X^T X)^{-1} X^T y
\]

But it's computationally expensive for large datasets.

---

## 8. What do slope and intercept mean?

- Intercept (θ₀): predicted Y when X = 0
- Slope (θ₁): the average change in Y for one unit change in X

---

## 9. What are evaluation metrics for regression?

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)

---

## 10. What is R-squared?

It measures how well the model explains variance in the target variable:
\[
R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
\]

R² = 1: perfect fit,  
R² = 0: no explanatory power

---

## 11. What is underfitting and overfitting?

- Underfitting: model too simple → high bias
- Overfitting: model too complex → high variance

---

## 12. What causes high bias?

- Ignoring important features
- Linear model for non-linear data

---

## 13. What causes high variance?

- Model learns noise
- Too complex model for small dataset

---

## 14. What is the Bias-Variance trade-off?

It’s the balance between underfitting (high bias) and overfitting (high variance). A good model minimizes both.

---

## 15. Can Linear Regression be used for classification?

Not directly. Use **Logistic Regression** for binary classification. SLR assumes continuous output.

---

## 16. When does Linear Regression fail?

- Non-linear data
- Outliers
- Correlated features (MLR)
- Violation of assumptions

---

## 17. Is scaling required in Linear Regression?

Not necessary for basic regression, but **yes** if using **regularization (Lasso, Ridge)** or **Gradient Descent**.

---

## 18. What’s the difference between MSE and RMSE?

RMSE is the square root of MSE, bringing error back to the same unit as the target variable.

---

## 19. What’s multicollinearity?

In **Multiple Linear Regression**, if features are highly correlated, it affects stability and interpretability of coefficients.

---

## 20. Real-world use cases?

- Predicting house prices
- Sales forecasting
- Demand estimation
- Time trend modeling