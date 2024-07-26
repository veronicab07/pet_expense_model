
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
df = pd.read_csv('combined_data.csv')

X = df.drop('yearly_final_cost', axis=1)
y = df['yearly_final_cost']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initializing the Support Vector Classifier
svm_model = SVC(kernel='linear') # You can try other kernels like 'rbf'

# Fitting the model
svm_model.fit(X_train, y_train)

y_pred = svm_model.predict(X_test)

# Model Accuracy
print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# Classification Report
print(classification_report(y_test, y_pred))