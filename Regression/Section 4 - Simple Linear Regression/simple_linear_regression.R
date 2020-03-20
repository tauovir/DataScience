# Simple Linear Regression

# Importing the dataset
dataset = read.csv('Salary_Data.csv')

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)
# We do not need feature scaling because model take cares itself

#Fitting Simple Linear Regression to Training Set
regressor = lm(formula = Salary ~ YearsExperience, data = training_set)
#Predict test set result
y_prid = predict(regressor, newdata = test_set)

#Visualize Data
plot(training_set$Salary, training_set$YearsExperience,type = 'p',
     xlab = "Salary", ylab = "Experience", main = "Salary Vs Experinec")



