from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

_url = 'http://{0}/sts_sci_md00_001.do?schulCode={1}&schulCrseScCode=4&schulKndScScore=04&schYm={2}{3:0>2}'

SEOUL = 'stu.sen.go.kr'
BUSAN = 'stu.pen.go.kr'
DAEGU = 'stu.dge.go.kr'
INCHEON = 'stu.ice.go.kr'
GWANGJU = 'stu.gen.go.kr'
DAEJEON = 'stu.dje.go.kr'
ULSAN= 'stu.use.go.kr'
SEJONG = 'stu.sje.go.kr'
GYEONGGI = 'stu.cbe.go.kr'
KANGWON = 'stu.kwe.go.kr'
CHUNGBUK = 'stu.cbe.go.kr'
CHUNGNAM = 'stu.cne.go.kr'
JEONBUK = 'stu.jbe.go.kr'
JEONNAM = 'stu.jne.go.kr'
GYEONGBUK = 'stu.gbe.go.kr'
GYEONGNAM = 'stu.gne.go.kr'
JEJU = 'stu.jje.go.kr'


class SchoolAPI:
    def __init__(self, region, school_code):
        self.region = region
        self.school_code = school_code

        self.menus = []
        self.current_year = 0
        self.current_month = 0
        # 파싱되기 전 대기

    def get_by_date(self, year, month, day):
        self._validate(year, month)

        return self.menus[day - 1]

    def get_monthly(self, year, month):
        self._validate(year, month)

        return self.menus

    def _validate(self, year, month):
        # 파싱 전 값 검증
        if not self.menus or (self.current_year != year or self.current_month != month):
            self._parse(year, month)

    def _parse(self, year, month):
        self.current_year = year
        self.current_month = month

        resp = urlopen(_url.format(self.region, self.school_code, year, month))
        soup = BeautifulSoup(resp, 'html.parser')
        monthly_menu = [td.text for td in soup.find(class_='tbl_type3 tbl_calendar').find_all('td') if td.text != ' ']

        for data in monthly_menu:
            if len(data) > 1 and data != '자료가 없습니다':
                day = int(re.findall('\d+', data)[0])
                daily_menus = re.findall('[가-힇]+', data)

                menu_dict = dict()
                if '조식' in daily_menus:
                    if '중식' in daily_menus:
                        menu_dict['breakfast'] = daily_menus[1: daily_menus.index('중식')]
                    elif '석식' in daily_menus:
                        menu_dict['breakfast'] = daily_menus[1: daily_menus.index('석식')]
                    else:
                        menu_dict['breakfast'] = daily_menus[1:]
                else:
                    menu_dict['breakfast'] = '급식이 없습니다'

                if '중식' in daily_menus:
                    if '석식' in daily_menus:
                        menu_dict['lunch'] = daily_menus[daily_menus.index('중식') + 1: daily_menus.index('석식')]
                    else:
                        menu_dict['lunch'] = daily_menus[daily_menus.index('중식') + 1:]
                else:
                    menu_dict['lunch'] = '급식이 없습니다'

                if '석식' in daily_menus:
                    menu_dict['dinner'] = daily_menus[daily_menus.index('석식') + 1:]
                else:
                    menu_dict['dinner'] = '급식이 없습니다'

                self.menus.append({day: menu_dict})


if __name__ == '__main__':
    print(SchoolAPI(DAEJEON, 'G100000170').get_by_date(2016, 9, 20))
