import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# โหลดข้อมูลจาก csv
df = pd.read_csv("E:\VSCODE\Python_practice\MachineLearning\data.csv")
print("ข้อมูลตัวอย่าง:\n", df.head())

# เตรียมข้อมูล
X = df[['sleep_hours', 'study_hours']]
y = df['score']

# แบ่งข้อมูล train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# สร้างโมเดล
model = LinearRegression()
model.fit(X_train, y_train)

# ทำนาย
y_pred = model.predict(X_test)

# ประเมินผล
print("\nMean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# แสดงกราฟความสัมพันธ์
plt.scatter(y_test, y_pred)
plt.xlabel("คะแนนจริง")
plt.ylabel("คะแนนที่พยากรณ์")
plt.title("เปรียบเทียบคะแนนจริงกับที่พยากรณ์")
plt.grid(True)
plt.show()
