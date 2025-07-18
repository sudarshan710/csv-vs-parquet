##### CSV vs Parquet Data Format Comparisons With Compression and Integrity Checks

import pandas as pd
import os

df = pd.read_csv('snew_precincts.csv')
df.to_parquet('output.parquet', engine='pyarrow', compression='zstd')  ## Setting compression to ZSTD with pyarrow engine
df.to_parquet('output_gzip.parquet', engine='pyarrow', compression='gzip')

df2 = pd.read_parquet('output.parquet', engine='pyarrow')
df3 = pd.read_parquet('output_gzip.parquet', engine='pyarrow')

#### Print Parquet Data in Binary Format
with open("output.parquet", "rb") as f:
    print(f.read(100))

csv_file = 'snew_precincts.csv'
parquet_file = 'output.parquet'
parquet_second_file = 'output_gzip.parquet'

csv_size = os.path.getsize(csv_file)
parquet_size = os.path.getsize(parquet_file)
parquet_second_size = os.path.getsize(parquet_second_file)

print(f'\nSize of CSV file: {csv_size / 1024:.2f} KB')
print(f'Size of Parquet file (ZSTD): {parquet_size / 1024:.2f} KB \n')
print(f'Size of Parquet file (GZIP): {parquet_second_size / 1024:.2f} KB \n')

#### Reading Contents of Either Files to Check Integirty

print(df.head(), '\n')
print(df2.head(), '\n')
print(df3.head(), '\n')


#### Runtime Comparisons

import time

## csv-file

start = time.time()
csv_df = pd.read_csv('snew_precincts.csv')

len_csv = len(csv_df)
csv_df['Ballots Counted'] = pd.to_numeric(csv_df['Ballots Counted'], errors='coerce').fillna(0).astype(int)
sum_ballots_csv = csv_df['Ballots Counted'].sum()
mean_dems_by_county = csv_df.groupby('County Name')['Ballots Counted'].mean()

print('Sum: ',sum_ballots_csv)
print('Time taken for CSV-analytics: ', time.time() - start)



## parquet-file

start = time.time()
parquet_df = pd.read_parquet('output.parquet')

len_csv = len(parquet_df)
parquet_df['Ballots Counted'] = pd.to_numeric(parquet_df['Ballots Counted'], errors='coerce').fillna(0).astype(int)
sum_ballots_parquet = parquet_df['Ballots Counted'].sum()
mean_dems_by_county = parquet_df.groupby('County Name')['Ballots Counted'].mean()

print('\nSum: ', sum_ballots_parquet)
print('Time taken for Parquet-analytics: ', time.time() - start, '\n')
    
