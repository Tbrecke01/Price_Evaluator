# dependencies
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from collections import Counter


# import data
df = pd.read_csv('cleaned.csv')

# Create features dataframe
price_df = pd.DataFrame({'id': df['id'],
#                          'Year': pd.DatetimeIndex(pd.to_datetime(df['prices_dateSeen'])).year,
                         'Quarter': pd.DatetimeIndex(pd.to_datetime(df['prices_dateSeen'])).quarter,
                         'Month': pd.DatetimeIndex(pd.to_datetime(df['prices_dateSeen'])).month,
#                          'Day': pd.DatetimeIndex(pd.to_datetime(df['prices_dateSeen'])).day,
                         'prices_amountMin': df['prices_amountMin'],
                         'prices_merchant': df['prices_merchant'],
                         'isSale': df['prices_isSale']
                        })
price_df.dropna(inplace=True)

# Determine the number of unique values in each column
# price_df.nunique()

# value counts on merchant data -- NOTE - NEED TO RE-RUN THIS WITH CLEAN MERCHANT DATA
merchants = price_df['prices_merchant'].value_counts()

# Keep top volume merchants and replace the rest with 'other'
replace_merchants = list(merchants[merchants < 500].index)
for m in replace_merchants:
    price_df.prices_merchant = price_df.prices_merchant.replace(m, 'Other')

# Check value counts again
# price_df['prices_merchant'].value_counts()

# Create X dataframe
X_text = price_df.drop('isSale', axis=1)

# Encode merchant data
encoder = LabelEncoder()
X = X_text.copy()
X['prices_merchant'] = encoder.fit_transform(X['prices_merchant'])
X['id'] = encoder.fit_transform(X['id'])

# Create y dataframe
y = price_df['isSale']

# Check y classes
# y.value_counts()

# Splitting into Train and Test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# Creating StandardScaler instance
scaler = StandardScaler()

# Fitting Standard Scaler
X_scaler = scaler.fit(X_train)

# Scaling data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)

# check shape of training/testing data sets
# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)

# # create the model
rf_model = RandomForestClassifier(n_estimators=128, random_state=27)

# fit model to scaled training data
rf_model = rf_model.fit(X_train_scaled, y_train)

# # Making predictions using the testing data
predictions = rf_model.predict(X_test_scaled)
predictions

# Calculating the confusion matrix
cm = confusion_matrix(y_test, predictions)
cm_df = pd.DataFrame(
    cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"]
)

# Calculating the accuracy score
acc_score = accuracy_score(y_test, predictions)

# Displaying results
print("Confusion Matrix")
display(cm_df)
print(f"Accuracy Score : {acc_score}")
print("Classification Report")
print(classification_report(y_test, predictions))

# Use RandomOverSampler to obtain more "True" samples to train our model.
# Reason: 'isSale' appears to be "FALSE" more often than "TRUE"
ros = RandomOverSampler(random_state=1)
X_resampled, y_resampled = ros.fit_resample(X_train, y_train)
Counter(y_resampled)

# Creating StandardScaler instance
scaler = StandardScaler()

# Fitting Standard Scaler
X_scaler = scaler.fit(X_resampled)

# Scaling data
X_train_scaled = X_scaler.transform(X_resampled)
X_test_scaled = X_scaler.transform(X_test)

# # create the model
rf_model = RandomForestClassifier(n_estimators=128, random_state=27)

# fit model to scaled training data
rf_model = rf_model.fit(X_train_scaled, y_resampled)

# # Making predictions using the testing data
predictions = rf_model.predict(X_test_scaled)
predictions

# Calculating the confusion matrix
cm = confusion_matrix(y_test, predictions)
cm_df = pd.DataFrame(
    cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"]
)

# Calculating the accuracy score
acc_score = accuracy_score(y_test, predictions)

# Displaying results
print("Confusion Matrix")
display(cm_df)
print(f"Accuracy Score : {acc_score}")
print("Classification Report")
print(classification_report(y_test, predictions))


