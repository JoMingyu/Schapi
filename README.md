# Schapi
Python 기반 School API

## How to use
### PyPI
~~~
pip install schapi
~~~

~~~
from schapi import SchoolAPI, DAEJEON
api = SchoolAPI(DAEJEON, 'G100000170')

print(api.get_by_date(2017, 9, 27))
print(api.get_monthly(2017, 9))
~~~

### Schapi Server
아래의 Swagger 문서를 확인하시기 바랍니다. 서버 주소는 52.79.134.200:4520입니다.
<http://petstore.swagger.io/?url=http://52.79.134.200:4520/api/swagger.json>
