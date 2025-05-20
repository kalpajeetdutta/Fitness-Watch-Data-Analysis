import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("fitness_activity.csv")

# Data Preprocessing
df.describe()
df.info()
df.isnull()
print(df.isnull().sum())

# Visualization 1: Histogram of Total Distance
plt.figure(figsize=(8, 6))
sns.histplot(df['Total_Distance'], bins=20, kde=True)
plt.xlabel('Total Distance')
plt.ylabel('Frequency')
plt.title('Histogram of Total Distance')
plt.tight_layout()
plt.show()

# Visualization 2: Scatter Plot of Very Active Minutes vs. Calories Burned
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Very_Active_Minutes', y='Calories_Burned', data=df)
plt.xlabel('Very Active Minutes')
plt.ylabel('Calories Burned')
plt.title('Very Active Minutes vs. Calories Burned')
plt.tight_layout()
plt.show()

# Visualization 3: Bar Plot of Total Distance vs. Tracker Distance
plt.figure(figsize=(8, 6))
df[['Total_Distance', 'Tracker_Distance']].sum().plot(kind='bar', color=['skyblue', 'lightgreen'])
plt.xlabel('Distance Type')
plt.ylabel('Total Distance')
plt.title('Total Distance vs. Tracker Distance')
plt.tight_layout()
plt.show()

# Visualization 4: Pie Chart of Activity Distribution
activity_columns = ['Very_Active_Minutes', 'Fairly_Active_Minutes', 'Lightly_Active_Minutes', 'Sedentary_Minutes']
activities_total = df[activity_columns].sum()
plt.figure(figsize=(8, 8))
plt.pie(activities_total, labels=activities_total.index, autopct='%1.2f%%', startangle=140)
plt.title('Activity Distribution')
plt.tight_layout()
plt.show()

# Visualization 5: Pairplot of Selected Features
selected_features = ['Steps', 'Total_Distance', 'Very_Active_Minutes', 'Calories_Burned']
sns.pairplot(df[selected_features])
plt.tight_layout()
plt.show()

