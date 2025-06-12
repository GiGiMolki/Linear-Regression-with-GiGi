# 📘 01 — Introduction to Simple Linear Regression

## 🎯 Objective
To understand what Simple Linear Regression (SLR) is, how it works, and where it is used.

---

## 📌 What is Simple Linear Regression?

**Simple Linear Regression** is a statistical method that models the relationship between:

- A **dependent variable** (target/output) `y`
- And a **single independent variable** (feature/input) `x`

The model assumes this relationship is **linear**, i.e., follows the form:

\[
y = mx + c
\]

Where:
- \( y \): Dependent variable (what you're predicting)
- \( x \): Independent variable (input feature)
- \( m \): Slope of the line (shows how much y changes when x increases)
- \( c \): Intercept (value of y when x = 0)

---

## 🔍 Example Use-Cases

| Domain        | Use-Case                              |
|---------------|----------------------------------------|
| Education     | Predict marks based on study hours     |
| Finance       | Predict stock price from market index  |
| Agriculture   | Predict crop yield from rainfall       |
| Sports        | Predict runs scored from batting time  |
| Retail        | Predict sales from advertising budget  |

---

## 🧠 Intuition: What Does the Line Do?

The regression line aims to **minimize the error** between the **actual values** and the **predicted values**.

This error is measured using **residuals**:


Residual = y_i - hat{y}_i


The goal is to minimize the **Sum of Squared Residuals (SSR)**:


SSR = sum (y_i - hat{y}_i)^2


---

## 🧮 Deriving the Best Fit Line (Least Squares Method)

Let the dataset have \( n \) points: \( (x_1, y_1), ..., (x_n, y_n) \)

We estimate: 
![Alt Text](/Simple%20Linear%20Regression%20/images/image1.png)

**Formulas:**
- Slope \( m \):
\[
m = \frac{n \sum x y - \sum x \sum y}{n \sum x^2 - (\sum x)^2}
\]

- Intercept \( c \):
\[
c = \bar{y} - m \bar{x}
\]

![Alt Text](/Simple%20Linear%20Regression%20/images/image2.png)


Where:
- \( \bar{x} \) and \( \bar{y} \) are the means of `x` and `y`

---

## ✅ Assumptions of Linear Regression

1. **Linearity**: The relationship between `x` and `y` is linear.
2. **Independence**: Observations are independent.
3. **Homoscedasticity**: Constant variance of residuals.
4. **Normality of errors**: Residuals are normally distributed.
5. **No multicollinearity**: (Not applicable in simple regression, but crucial in multiple regression)

---

## 📈 Geometric Interpretation

- The regression line splits the space of `y` values such that the **distance from each point to the line is minimized vertically** (not orthogonally).
- This makes it a **projection onto a 1D subspace** in higher dimensions.

---

## 💡 Advantages

- Easy to implement and interpret
- Useful as a baseline model
- Good for understanding basic predictive relationships

---

## ⚠️ Limitations

- Assumes linearity even when real-world data is non-linear
- Sensitive to **outliers**
- Doesn’t work well with **collinearity** or **multivariate influences**

---

## 📦 Summary

| Component       | Description                          |
|------------------|--------------------------------------|
| Model Type       | Parametric, supervised               |
| Target Type      | Continuous                           |
| Number of Features | Single independent variable       |
| Key Metric       | R-squared, MSE, MAE, RMSE            |
| Learning Method  | Least Squares Minimization           |

---
