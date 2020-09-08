# Question 5 lasso regression part D

#Importing the essential libraries

library(glmnet)
library(MASS)

# Now we will generate matrix from x and y variables:
# Separate the X's and Y's as matrices
insure_Train_X = as.matrix(insuranceTrain[, -1])   # Take out "CRIM", column 1
insure_Train_Y = as.matrix(insuranceTrain[, 1])    # Take only "CRIM", column 1

insure_Test_X= as.matrix(insuranceTest[, -1])   # Take out "CRIM", column 1
insure_Test_Y = as.matrix(insuranceTest[, 1])    # Take only "CRIM", column 1


lRange = seq(0, 5, .1)
insure_Lasso = glmnet(insure_Train_X, insure_Train_Y, alpha=1, lambda=lRange)

# Get a plot of th variable sizes based on lambda.  
plot(insure_Lasso, xvar="lambda")

insure_Lasso  


# The cross validation 
insure_Lasso1 = cv.glmnet(insure_Train_X, insure_Train_Y, alpha=1, nfolds = 7)
insure_Lasso1$lambda.min
insure_Lasso1$lambda.1se

plot(insure_Lasso1)

# Test set RMSE 
insure_lassoPred = predict(insure_Lasso1, insure_Test_X, s="lambda.1se")
rmse_insure_Lasso = sqrt(mean((insure_lassoPred - insure_Test_Y)^2))
rmse_insure_Lasso  


# Teaining set RMSE
insure_lassoPred2 = predict(insure_Lasso1, insure_Train_X, s="lambda.1se")
rmse_insure_Lasso2 = sqrt(mean((insure_lassoPred2 - insure_Train_Y)^2))
rmse_insure_Lasso2


# Part e Question 5 code
# We have to plot the residual plot for prdcivted vs the fitted vlaues
Residual_plot = insure_lassoPred - insuranceTest$newpol
Residual_plot
plot(insure_lassoPred,Residual_plot)


