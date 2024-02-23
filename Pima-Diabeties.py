import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you have a Pima Indians Diabetes dataset CSV file
file_path = 'pima_indians_diabetes.csv'
df = pd.read_csv(file_path)
# Display basic information about the dataset
print("Basic Information:")
print(df.info())

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Histograms for each feature
df.hist(figsize=(12, 8))
plt.suptitle('Histograms of Pima Indians Diabetes Dataset Features', y=1.02)
plt.show()
# Density and contour plots
plt.figure(figsize=(12, 8))

for i, feature in enumerate(df.columns[:-1]):  # Exclude the target column
    plt.subplot(2, 3, i + 1)
    sns.kdeplot(df[feature][df['Outcome'] == 0], label='No Diabetes', shade=True)
    sns.kdeplot(df[feature][df['Outcome'] == 1], label='Diabetes', shade=True)
    plt.title(f'Density and Contour Plot of {feature}')

plt.tight_layout()
plt.show()
from mpl_toolkits.mplot3d import Axes3D

# Example: Scatter plot with three features
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['Glucose'], df['BMI'], df['Age'], c=df['Outcome'], marker='o')

ax.set_xlabel('Glucose')
ax.set_ylabel('BMI')
ax.set_zlabel('Age')

plt.title('Three-dimensional Scatter Plot')
plt.show()


