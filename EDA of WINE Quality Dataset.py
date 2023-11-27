#EDA of WINE Quality Dataset
#Data Adjustment
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import seaborn as sns

# Specifying the file path
file_path = r'E:\Study Materials\Masters Data Science\1-1\Introduction to Python\Assisgnment\wine-quality white.csv'

# Loading the CSV file into a DataFrame
df = pd.read_csv(file_path)
print(df.head())

# according to the instruction of the assignment append new rows.
# my id=05, Thus X=0.05 and it will be added to the values of the new rows.
X = 0.05
r1 = np.round([7.8 + X, 0.88 + X, 0 + X, 1.9, 0.09 + X, 25 + X, 67 + X, .991 + X, 3.22, 0.68 + X, 9.8 + X, 5], 2)
r2 = np.round([7.2 + X, 0.83 + X, 0.01 + X, 2.2, 0.19 + X, 15 + X, 60 + X, .996 + X, 3.52, 0.55 + X, 9.6 + X, 6], 2)
r3 = np.round([7.9 + X, 0.89 + X, 0.01 + X, 1.7, 0.08 + X, 22 + X, 57 + X, .997 + X, 3.26, 0.64 + X, 9.8 + X, 2], 2)
r4 = np.round([7.7 + X, 0.86 + X, 0.02 + X, 2.3, 0.07 + X, 11 + X, 38 + X, .994 + X, 3.12, 0.08 + X, 9.4 + X, 3], 2)
dataSeries = [pd.Series(r1, index=df.columns), pd.Series(r2, index=df.columns),
              pd.Series(r3, index=df.columns), pd.Series(r4, index=df.columns)]

df2 = pd.concat([df, pd.DataFrame(dataSeries)], ignore_index=True)
print(df2)

#### Modifying quality column as per assignment
#### reallocating the quality of wine as 1: 0 to 5 (Bad quality) and 2: 6 to 10 (Good quality).
df2[[df2[['quality']] <= 5.0]]=1
df2[[df2[['quality']] > 5.0]]=2
df2['quality'] = df2['quality'].map({1:'Bad', 2:'Good'})
print (df2)

# Univariate Analysis - Histograms for Each Variable
plt.figure(figsize=(16, 12))

# Histogram for Fixed Acidity
plt.subplot(3, 4, 1)
sns.histplot(data=df2, x='fixed acidity', bins=20, kde=True)
plt.title('Histogram of Fixed Acidity')

# Histogram for Volatile Acidity
plt.subplot(3, 4, 2)
sns.histplot(data=df2, x='volatile acidity', bins=20, kde=True)
plt.title('Histogram of Volatile Acidity')

# Histogram for Citric Acid
plt.subplot(3, 4, 3)
sns.histplot(data=df2, x='citric acid', bins=20, kde=True)
plt.title('Histogram of Citric Acid')

# Histogram for Residual Sugar
plt.subplot(3, 4, 4)
sns.histplot(data=df2, x='residual sugar', bins=20, kde=True)
plt.title('Histogram of Residual Sugar')

# Histogram for Chlorides
plt.subplot(3, 4, 5)
sns.histplot(data=df2, x='chlorides', bins=20, kde=True)
plt.title('Histogram of Chlorides')

# Histogram for Free Sulfur Dioxide
plt.subplot(3, 4, 6)
sns.histplot(data=df2, x='free sulfur dioxide', bins=20, kde=True)
plt.title('Histogram of Free Sulfur Dioxide')

# Histogram for Total Sulfur Dioxide
plt.subplot(3, 4, 7)
sns.histplot(data=df2, x='total sulfur dioxide', bins=20, kde=True)
plt.title('Histogram of Total Sulfur Dioxide')

# Histogram for Density
plt.subplot(3, 4, 8)
sns.histplot(data=df2, x='density', bins=20, kde=True)
plt.title('Histogram of Density')

# Histogram for pH
plt.subplot(3, 4, 9)
sns.histplot(data=df2, x='pH', bins=20, kde=True)
plt.title('Histogram of pH')

# Histogram for Sulphates
plt.subplot(3, 4, 10)
sns.histplot(data=df2, x='sulphates', bins=20, kde=True)
plt.title('Histogram of Sulphates')

# Histogram for Alcohol
plt.subplot(3, 4, 11)
sns.histplot(data=df2, x='alcohol', bins=20, kde=True)
plt.title('Histogram of Alcohol')

plt.tight_layout()
plt.show()

# Univariate Analysis - Box Plots for Each Variable
plt.figure(figsize=(12, 8))
for column in df2.columns[:-1]:  # Exclude 'quality' column
    plt.subplot(3, 4, df.columns.get_loc(column) + 1)
    sns.boxplot(data=df, y=column)
    plt.title(f'Box Plot of {column}')
plt.tight_layout()
plt.show()


## Bivariate Analysis - Scatter Plots for Selected Variables Pairs

# Scatter Plot: Fixed Acidity vs Volatile Acidity
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df2, x='fixed acidity', y='volatile acidity', hue='quality', alpha=0.7)
plt.title('Scatter Plot: Fixed Acidity vs Volatile Acidity')
plt.xlabel('Fixed Acidity')
plt.ylabel('Volatile Acidity')
plt.legend()
plt.show()


# Scatter Plot: Fixed Acidity vs Citric Acid
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df2, x='fixed acidity', y='citric acid', hue='quality', alpha=0.7)
plt.title('Scatter Plot: Fixed Acidity vs Citric Acid')
plt.xlabel('Fixed Acidity')
plt.ylabel('Citric Acid')
plt.legend()
plt.show()

# Scatter Plot: Fixed Acidity vs Residual Sugar
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df2, x='fixed acidity', y='residual sugar', hue='quality', alpha=0.7)
plt.title('Scatter Plot: Fixed Acidity vs Residual Sugar')
plt.xlabel('Fixed Acidity')
plt.ylabel('Residual Sugar')
plt.legend()
plt.show()

# Scatter Plot: Fixed Acidity vs Alcohol
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df2, x='fixed acidity', y='alcohol', hue='quality', alpha=0.7)
plt.title('Scatter Plot: Fixed Acidity vs Alcohol')
plt.xlabel('Fixed Acidity')
plt.ylabel('Alcohol')
plt.legend()
plt.show()

# Scatter Plot: Volatile Acidity vs Citric Acid
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df2, x='volatile acidity', y='citric acid', hue='quality', alpha=0.7)
plt.title('Scatter Plot: Volatile Acidity vs Citric Acid')
plt.xlabel('Volatile Acidity')
plt.ylabel('Citric Acid')
plt.legend()


# Scatter Plot: Volatile Acidity vs Residual Sugar
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df2, x='volatile acidity', y='residual sugar', hue='quality', alpha=0.7)
plt.title('Scatter Plot: Volatile Acidity vs Residual Sugar')
plt.xlabel('Volatile Acidity')
plt.ylabel('Residual Sugar')
plt.legend()
plt.show()

# Scatter Plot: Volatile Acidity vs Alcohol
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df2, x='volatile acidity', y='alcohol', hue='quality', alpha=0.7)
plt.title('Scatter Plot: Volatile Acidity vs Alcohol')
plt.xlabel('Volatile Acidity')
plt.ylabel('Alcohol')
plt.legend()
plt.show()

# Scatter Plot: Citric Acid vs Residual Sugar
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df2, x='citric acid', y='residual sugar', hue='quality', alpha=0.7)
plt.title('Scatter Plot: Citric Acid vs Residual Sugar')
plt.xlabel('Citric Acid')
plt.ylabel('Residual Sugar')
plt.legend()
plt.show()

# Scatter Plot: Citric Acid vs Alcohol
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df2, x='citric acid', y='alcohol', hue='quality', alpha=0.7)
plt.title('Scatter Plot: Citric Acid vs Alcohol')
plt.xlabel('Citric Acid')
plt.ylabel('Alcohol')
plt.legend()
plt.show()

# Scatter Plot: Residual Sugar vs Alcohol
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df2, x='residual sugar', y='alcohol', hue='quality', alpha=0.7)
plt.title('Scatter Plot: Residual Sugar vs Alcohol')
plt.xlabel('Residual Sugar')
plt.ylabel('Alcohol')
plt.legend()
plt.show()

# Remove the 'quality' column temporarily
quality_column = df2['quality']
df2 = df2.drop(columns=['quality'])

# Correlation Heatmap
correlation_matrix = df2.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()
# Add back the 'quality' column
df2['quality'] = quality_column

# Box Plot for Wine Quality vs. Alcohol Content
plt.figure(figsize=(8, 6))
sns.boxplot(x='quality', y='alcohol', data=df2)
plt.title('Wine Quality vs. Alcohol Content')
plt.xlabel('Wine Quality')
plt.ylabel('Alcohol Content')
plt.show()

# Scatter Plot for Alcohol Content vs. Volatile Acidity
plt.figure(figsize=(8, 6))
sns.scatterplot(x='alcohol', y='volatile acidity', data=df2, hue='quality', palette={'Good': 'g', 'Bad': 'r'})
plt.title('Alcohol Content vs. Volatile Acidity with Wine Quality Hue')
plt.xlabel('Alcohol Content')
plt.ylabel('Volatile Acidity')
plt.legend(title='Wine Quality')
plt.show()

# Selecting variables for pair plots
selected_columns = ['alcohol', 'volatile acidity', 'citric acid', 'chlorides', 'sulphates']

## Pair Plots with Hue for Wine Quality
sns.pairplot(df2[selected_columns + ['quality']], hue='quality', palette={'Good': 'g', 'Bad': 'r'})
plt.suptitle('Pair Plots with Hue for Selected Variables and Wine Quality', y=1.02)
plt.show()


