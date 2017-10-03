from flask_restful_swagger_2 import swagger, Resource, request
from db.models.school_data import SchoolModel
from schapi import SchoolAPI


class Meal(Resource):
    @swagger.doc({
        'tags': ['급식'],
        'description': '학교 코드를 이용한 급식 조회',

        'parameters': [
            {
                'name': 'code',
                'description': '학교 코드',
                'in': 'path',
                'type': 'String'
            },
            {
                'name': 'date',
                'description': '조회할 날짜',
                'in': 'query',
                'type': 'Date(YYYY-MM-DD)'
            }
        ],

        'responses': {
            '200': {
                'description': '급식 조회 성공(데이터 있음)',
                'examples': {
                    'application/json': {
                        "breakfast": "['시래기된장국', '돼지고기산적', '매운맛당면김말이', '케찹', '석박지', '도시락김', '보리밥']",
                        "lunch": "['감자탕', '순대야채볶음', '콩나물잡채', '배추김치', '보리밥', '파인애플']",
                        "dinner": "['김치알밥', '유부된장국', '배추겉절이', '파래돌김자반', '단호박부꾸미', '초코맛아이스크림']"
                    }
                }
            },
            '204': {
                'description': '급식 조회 실패(데이터 없음)'
            }
        }
    })
    def get(self):
        code = request.args.get('code')
        year, month, day = request.args.get('date').split('-')

        web_url = SchoolModel.objects(code=code).first().web_url

        return SchoolAPI(web_url, code).get_by_date(int(year), int(month), int(day))
