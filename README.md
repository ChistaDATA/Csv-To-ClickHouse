# Csv-To-ClickHouse
Insert data to ClickHouse from CSV file via Python


Edit Following Rows and run the python script

conn = clickhouse_driver.Client(host='localhost', port=9000)
 
with open('data.csv', 'r') as f:

query = f"INSERT INTO table ({columns}) VALUES "
    

python
