from email_templates import pretest_notify
import os
from dotenv import load_dotenv
load_dotenv()
# Path: main.py

# read user data from tsv file
import pandas as pd
df = pd.read_csv(".\\accounts.tsv", sep="\t")

# send email to each user
for index, row in df.iterrows():
    pretest_notify(row["user"], row["email"])