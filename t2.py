import pandas as pd
from datetime import datetime

pd.date_range(end = datetime.today(), periods = 100).to_pydatetime().tolist()

#OR

dd = pd.date_range(start="2018-09-09",end="2020-02-02")
print(dd)