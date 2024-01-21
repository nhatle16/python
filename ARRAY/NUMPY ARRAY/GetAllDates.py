# Get all dates in a month of a year

import numpy as np

start_date = np.datetime64('2020-02-01')
end_date = np.datetime64('2020-02-28')
dates = np.arange(start=start_date, stop=end_date+1, dtype='datetime64[D]')

print(dates)