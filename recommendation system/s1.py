import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# 1. Read Excel data
file_path = 'C:\\Users\\pankt\\OneDrive\\Desktop\\TradeBuddy\\user_activity.xlsx'
existing_data = pd.read_excel(file_path)

# 2. Take user input
user_categories = input("Enter categories separated by space: ")
user_price_range = input("Enter price range: ")
user_id = '123'  # Replace '123' with your user ID

# 3. Preprocess data if required

# 4. Append user input with ID
new_row = pd.DataFrame({'User': user_id, 'Product Category': user_categories, 'Price Range': user_price_range}, index=[0])
existing_data = existing_data.append(new_row, ignore_index=True)

# 5. Apply machine learning
vectorizer = TfidfVectorizer()  # or CountVectorizer()
X = vectorizer.fit_transform(existing_data['Product Category'])
model = KMeans(n_clusters=3)  # Change n_clusters as needed
model.fit(X)

# 6. Generate top categories per user
existing_data['Cluster'] = model.labels_
user_data = existing_data[existing_data['User'] == user_id]
user_vector = vectorizer.transform(user_data['Product Category'])
user_cluster = model.predict(user_vector)[0]
top_categories = existing_data[existing_data['Cluster'] == user_cluster]['Product Category'].value_counts().head(3)

# 7. Display output
print(f"Top 3 recommended categories for User {user_id}: {top_categories}")


# 8. Further processing to recommend products based on these categories
# Add logic to recommend products based on the identified top categories for the user
