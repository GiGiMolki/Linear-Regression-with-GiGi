# 05 — Mathematics Behind Simple Linear Regression

In this notebook, we will:
- Understand the goal of SLR
- Derive the formula for slope and intercept
- Learn the concept of cost function (MSE)
- Arrive at the Normal Equation using calculus

## 🎯 Goal of Simple Linear Regression

To find the best-fitting straight line for a set of data points:

![Alt Text](/Simple%20Linear%20Regression%20/images/image3.png)


Where:
- hat{y} = predicted output
- theta_0 = intercept
- theta_1 = slope

## 🧠 Deriving Optimal θ₀ and θ₁

The model should minimize the total squared error:

![Alt Text](/Simple%20Linear%20Regression%20/images/image4.png)

## 🧠 Deriving Optimal θ₀ and θ₁

Remember, when we derive the Error equation with theta_0 and set its result to zero, it will give us the optimum value of theta_0 that will bring the Error to minimum/maximum.

![Alt Text](/Simple%20Linear%20Regression%20/images/image5.png)

Since we get the theta_0 value, we will substitute it to find the optimum theta_1:
![Alt Text](/Simple%20Linear%20Regression%20/images/image6.png)

## 📏 Geometric Meaning

- **θ₁** represents the **rate of change** — how much y changes for one unit increase in x.
- **θ₀** is the point where the line crosses the y-axis (when x = 0).

This line minimizes the squared vertical distances between actual y-values and predicted hat{y}.

## 🧾 Matrix Form: Normal Equation

We can write the problem in **matrix form**:

Let:

![Alt Text](/Simple%20Linear%20Regression%20/images/image7.png)


This is the **Normal Equation**.

## 📌 Why Not Always Use the Normal Equation?

- Pros:
  - No need to tune learning rate
  - Gives exact solution for small datasets

- Cons:
  - Very expensive for large datasets (O(n³))
  - Doesn’t scale well

That’s why **Gradient Descent** is often used instead.