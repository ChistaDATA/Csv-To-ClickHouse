# Csv-To-ClickHouse
Insert data to ClickHouse from CSV file via Python


Edit Following Rows and run the python script
<pre id="example"><code class="language-lang"  style="color: #333; background: #f8f8f8;"> 
conn = clickhouse_driver.Client(host='localhost', port=9000)
 
with open('data.csv', 'r') as f:

query = f"INSERT INTO table ({columns}) VALUES "
</code></pre>

<pre id="example"><code class="language-lang"  style="color: #333; background: #f8f8f8;"> 
python uploadFile.py

or

python3 uploadFile.py
</code></pre>
