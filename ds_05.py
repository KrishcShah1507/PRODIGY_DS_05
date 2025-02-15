import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Users\DELL\Desktop\ProdigyInfotech_DataScience\5\archive\NYC Accidents 2020.csv")
df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'])
print(df.head())
print(df.info())
print(df.isnull().sum())
plt.figure(figsize=(10, 6))
sns.countplot(x='BOROUGH', data=df, palette='viridis')
plt.title('Number of Accidents by Borough')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
weather_columns = [col for col in df.columns if 'WEATHER' in col.upper()]
road_columns = [col for col in df.columns if 'ROAD' in col.upper()]
if weather_columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(x=weather_columns[0], data=df, palette='viridis')
    plt.title('Number of Accidents by Weather Conditions')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Weather conditions column not found in the dataset.")
if road_columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(x=road_columns[0], data=df, palette='viridis')
    plt.title('Number of Accidents by Road Conditions')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Road conditions column not found in the dataset.")
contributing_factors = df.iloc[:, 18:23].melt(var_name='Contributing Factor', value_name='Count')
plt.figure(figsize=(12, 8))
sns.countplot(x='Contributing Factor', data=contributing_factors.dropna(), palette='viridis')
plt.title('Contributing Factors to Accidents')
plt.xticks(rotation=45)
plt.xlabel('Contributing Factors')
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 8))
sns.scatterplot(x='LONGITUDE', y='LATITUDE', data=df, alpha=0.5)
plt.title('Distribution of Accidents by Latitude and Longitude')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.tight_layout()
plt.show()
df['CRASH HOUR'] = pd.to_datetime(df['CRASH TIME']).dt.hour
plt.figure(figsize=(10, 6))
sns.countplot(x='CRASH HOUR', data=df, palette='viridis')
plt.title('Number of Accidents by Time of Day')
plt.xlabel('Hour of Day')
plt.tight_layout()
plt.show()
df['CRASH MONTH'] = df['CRASH DATE'].dt.month_name()
plt.figure(figsize=(10, 6))
sns.countplot(x='CRASH MONTH', data=df, palette='viridis', order=[
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
])
plt.title('Number of Accidents by Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
summary_stats = df.describe()
print(summary_stats)