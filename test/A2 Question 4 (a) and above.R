# Question 4 Assignment 2

# Importing the libraries
library(psych)     # Has a much better scatterplot matrix function
library(corrplot)  # A nice correlation matrix visualization
library(car)       # Misc statistical methods
library(QuantPsyc) # Misc statistical methods
library(leaps)     # Gives forward, backward and stepwise
library(lm.beta)   # Gives us standardized coefficients

# Now we will rerun the linear regression model foR CRIM 
# using training data

house_training = read.csv(file.choose())
options(max.print = 9999)    # This operation allows us 
# to print the total number of 
# rows if max limit warning appears
house_training

head(house_training)    # To evaluate if all the columns and data is imported correctly

house_training <- lm(CRIM ~. , data = house_training)

summary(house_training)

rmse_house_train = sqrt(mean(house_training$residuals^2))
rmse_house_train

# -------------------------------------------------------------------------------------------------

# Importing the test data for generating the model

house_testing = read.csv(file.choose())
options(max.print = 9999)
house_testing
head(house_testing)

# Performing the linear regression with the testing data
house_testing <- lm(CRIM ~. , data = house_testing)

summary(house_testing)

rmse_house_Test = sqrt(mean(house_testing$residuals^2))
rmse_house_Test

#----------------------------------------------------------------------------------------------------

# cross validation on 4 b
# First let us import library glmnet for regression operation
# We will also create a range for the house training and testing dataset
# So that the cross validation and regression operation can be performed

library(glmnet)
set.seed(245)
houseTrain_X = as.matrix(house_training[, -1])   # We will remove the variable "CRIM", column 1
houseTrain_Y = as.matrix(house_training[, 1])    # We will take "CRIM", column 1

houseTest_X = as.matrix(house_testing[, -1])   # We will remove the variable "CRIM", column 1
houseTest_Y = as.matrix(house_testing[, 1])    # We will take "CRIM", column 1

lRange = seq(0, 3, .1)    # Setting up a range for lambda
lRange

# Simple ridge regression
house_Ridge_train = glmnet(houseTrain_X, houseTrain_Y, alpha=0, lambda=lRange)
plot(house_Ridge_train, xvar="lambda")

house_Ridge_train     # Lists the lambdas along with the R^2, (%Dev)

# The cross-validated version helps us with lambda selection!
#
# Note, we need to reduce the number of folds, or we get an error
# warning of a very small number of test samples in each fold
cross_house_train = cv.glmnet(houseTrain_X, houseTrain_Y, alpha=0, nfolds=7)
cross_house_train$lambda.min   
cross_house_train$lambda.1se
plot(cross_house_train)
summary(cross_house_train)

Predict_ridge = predict(cross_house_train, houseTest_X, s="lambda.1se")
rmse_ridge = sqrt(mean((Predict_ridge - houseTest_Y)^2))
rmse_ridge
rmse_house_Test

Predict_ridge = predict(cross_house_train, houseTrain_X, s="lambda.1se")
rmse_ridge = sqrt(mean((Predict_ridge - houseTrain_Y)^2))
rmse_ridge
rmse_house_train


# R squared
summary(house)   
cross_house_train= glmnet(houseTrain_X, houseTrain_Y, alpha=0, lambda=5.09)
cross_house_train
cross_house_test= glmnet(houseTest_X, houseTest_Y, alpha = 0, lambda = 5.09)
cross_house_test


#--------------------------------No NEED----------------------------------------------
cross_house_train1 = cv.glmnet(houseTrain_X, houseTrain_Y, alpha=0, grouped=F)
cross_house_train$lambda.min   
cross_house_train$lambda.1se


# Test set no.
cross_house_test = cv.glmnet(houseTest_X, houseTest_Y, alpha=0, nfolds=7)
cross_house_test$lambda.min   
cross_house_test$lambda.1se
plot(cross_house_test)