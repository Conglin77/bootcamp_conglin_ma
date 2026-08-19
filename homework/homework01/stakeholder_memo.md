# Stakeholder Memo: SSE Index 5-Day Return Prediction

**To:** Portfolio Manager  
**From:** Data Science Intern / Bootcamp Student  
**Date:** August 2026  
**Subject:** Project Plan for Predicting Short-Term A-Share Trends  

---

### What is the problem?
The stock market is incredibly volatile right now. We often make holding or selling decisions based on intuitions or delayed news. I want to build a data-driven tool that help us made more valid and reliable decisions.
### What are we going to do?
I am building a machine learning model to predict the **5-day return** of the Shanghai Stock Exchange (SSE) Composite Index. 
Instead of trying to predict the exact price perfectly, the goal is to get a reliable warning signal. For example, if the model predicts a sharp drop over the next 5 days, we can decide to reduce our stock positions or hold more cash.

### How will we measure success?
We will focus on two main things:
1. **Directional Accuracy:** Does the model correctly guess whether the market will go up or down?
2. **RMSE:** How big is the error when predicting the actual percentage change?

### What are the main risks to this project?
The biggest risk is that the Chinese market is heavily influenced by policy news, which isn't captured in historical price data. Also, I need to be careful not to let the model "memorize" the past data (overfitting), so I will test it strictly on time periods it hasn't seen before.