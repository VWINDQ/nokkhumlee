from sklearn.linear_model import LogisticRegression

# ข้อมูล: [ชั่วโมงนอน, ชั่วโมงอ่านหนังสือ]
X = [[5, 1], [6, 2], [7, 3], [8, 4], [9, 5]]
y = [0, 0, 1, 1, 1]

# Create a logistic regression model
model = LogisticRegression()
model.fit(X, y)

# ทำนายผลสำหรับนักเรียนที่นอน 1 ชั่วโมงและอ่านหนังสือ 5 ชั่วโมง
prediction = model.predict([[1, 5]])
print("ผลลัพธ์:", "ผ่าน" if prediction[0] == 1 else "ไม่ผ่าน")