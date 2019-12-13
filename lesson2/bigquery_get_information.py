import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"


from google.cloud import bigquery


client = bigquery.Client()

dataset_refference = client.dataset('new_york', project='bigquery-public-data')
print(type(dataset_refference))

# get link to datawarehouse
datawarehouse = client.get_dataset(dataset_refference)

# list all tables in datawarehouse
print([table.table_id for table in client.list_tables(datawarehouse)])


#go inside table citibike_trips
citibike_trips = client.get_table(datawarehouse.table('citibike_trips'))
print(citibike_trips.schema)