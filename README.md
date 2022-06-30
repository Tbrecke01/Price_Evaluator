# The “When to Buy” App
## Description 
Train a Machine Learning Model to be able to recognize whether a product’s pricing is discounted based on the date, merchant info and product id.
## Reason Selected
There’s always a lot of ‘head knowledge’ of the best times to buy a certain item (ie always Black Friday) or from where to buy it (according to my dad Best Buy is always the best) but there’s a lack of actual hard evidence for this. We wanted to get rid of the prophesizing and create a model to predict whether you’re getting a good deal on something, or whether you should wait a couple more weeks for a sale.
## Questions we Hope to Answer:
- If I buy ‘item X’ today, am I getting a good deal on it?
- What are the pricing trends for item X? Per retailer?
- What retailer should I buy item X from?
- Is one retailer generally better than the others?
- Are the best deals always on holidays?

## Communication Methods
- We will meet every Tuesday/Thursday starting at 6:00 to review changes and to go over large problems.
- Team members will update each other daily on Slack
- If assistance is needed, impropmtu meetings will be scheduled using Slack. If not all members can be present in these meetings that is acceptable.
- All team members have each others email and phone number for contact purposes as well in case of issues
- Individual member updates will be stored in their corresponding Git branch (named for each member). Review by two memebers is needed to push an update to main.

## Data ETL
We obtained [Electronic Products and Pricing Data](https://www.kaggle.com/datasets/datafiniti/electronic-products-prices?resource=download) from [kaggle.com](kaggle.com) which includes minimum selling prices (`prices_amountmin`) observed from various online merchants (`prices_merchant`) as well as the dates that those prices were observed (`prices_dateseen`), and whether the prices observed were "sale" prices (`prices_issale`) for each individual product id (`id`). 

In order to clean the data, we ______

Finally, using the `create_engine` function from `sqlalchemy`, we established a connection to our PostgreSQL RDS (hosted on AWS), where we saved our cleaned DataFrame. 


## Machine Learning Model
For the machine learning model, we chose the RandomForestClassifier to help predict whether prices seen online are "discounted / sale" prices or "standard / retail" prices. In order to train the model, 

In order to use the `pricing_merchant` data, we needed to clean the data using RegEx strings to match different variations of merchant names. Afterwards, in order to reduce the number of unique merchants, we only kept Bestbuy, Walmart and Amazon, and placed all other merchants into an 'Others' bucket. 

Additionally, we observed that our pricing data had a class imbalance with discounted prices being less common than standard prices (as expected) and therefore we utilized RandomOverSampling in our training population in order to achieve a more balanced training set.

# Technology usage for our final project
•	Data Cleaning: Pandas, Numpy, and re
•	Database: PostgreSQL RDS hosted on AWS
•	Machine Learning: Sklearn library
•	Code Editors: Jupyter Notebook / Google Colab / VScode
•	Dashboard: Streamlit, Matplotlib, Tableau, HTML, CSS , Bootstrap.
