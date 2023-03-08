import csv
import clickhouse_driver
 
# Connect to the database
conn = clickhouse_driver.Client(host='localhost', port=9000)
 
# Read the CSV file
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    columns = ','.join(header)
    query = f"INSERT INTO table ({columns}) VALUES "
    values = []
    for row in reader:
        values.append(f"({','.join(['\'{}\''.format(v) for v in row])})")
    query += ','.join(values)
 
# Insert the data into the database
conn.execute(query)
 
