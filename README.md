# Schapi
Python 기반 School API

## How to use
~~~
pip install schapi
~~~

~~~
from schapi import SchoolAPI, DAEJEON
api = SchoolAPI(DAEJEON, 'G100000170')

print(api.get_by_date(2017, 9, 27))
print(api.get_monthly(2017, 9))
~~~
