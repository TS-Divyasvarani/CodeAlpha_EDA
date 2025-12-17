import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------------
# Step 1: Check if CSV exists
# ---------------------------
file_name = "quotes_dataset.csv"

if not os.path.exists(file_name):
    print("CSV file not found. Creating sample dataset...")

    data = {
        "Quote": [
            "The world as we have created it is a process of our thinking.",
            "It is our choices that show what we truly are.",
            "There are only two ways to live your life.",
            "Imperfection is beauty, madness is genius.",
            "The person who reads too much loses himself."
        ],
        "Author": [
            "Albert Einstein",
            "J.K. Rowling",
            "Albert Einstein",
            "Marilyn Monroe",
            "Jane Austen"
        ],
        "Tags": [
            "change, deep-thoughts",
            "choices, inspirational",
            "life, simplicity",
            "beauty, life",
            "books, reading"
        ]
    }

    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)
    print("Sample dataset created successfully.\n")

# ---------------------------
# Step 2: Load dataset
# ---------------------------
df = pd.read_csv(file_name)

# ---------------------------
# 1. Ask meaningful questions
# ---------------------------
print("Questions before analysis:")
print("1. How many quotes are in the dataset?")
print("2. Which author has the most quotes?")
print("3. Are there any missing values?\n")

# ---------------------------
# 2. Explore data structure
# ---------------------------
print("Dataset Information:")
print(df.info())

print("\nFirst 5 rows:")
print(df.head())

# ---------------------------
# 3. Identify patterns & trends
# ---------------------------
author_count = df["Author"].value_counts()
print("\nQuotes per Author:")
print(author_count)

# ---------------------------
# 4. Hypothesis testing (Visualization)
# ---------------------------
author_count.plot(kind="bar")
plt.title("Number of Quotes per Author")
plt.xlabel("Author")
plt.ylabel("Count")
plt.show()

# ---------------------------
# 5. Detect data issues
# ---------------------------
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())
