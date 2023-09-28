import os 
import sys

file_name = '/Users/stephenshaeffer/Desktop/TimeSeriesModels/HumidityModels/humidity_station1.ipynb'

file_stats = os.stat(file_name)

print(file_stats)
print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')
