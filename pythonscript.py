import mysql.connector
import pandas as pd
import openpyxl

# Connect to the MySQL server
cnx = mysql.connector.connect(user='root',
                              password='password',
                              host='host')

cursor = cnx.cursor()

# Execute a SELECT statement
query = "SELECT * FROM [Input Your Table name here]"
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Iterate over the results and print them
for row in results:
    print(row)

# Convert the results to a pandas DataFrame
df = pd.DataFrame(results)

df.to_excel('C:\\Put\\YourPath\\Here' + 'NameYourFileHere.xlsx', index=False)


# Close the cursor and connection
cursor.close()
cnx.close()
