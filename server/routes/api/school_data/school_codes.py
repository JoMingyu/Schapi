from flask_restful_swagger_2 import swagger, Resource, request
from db.models.school_data import SchoolModel


class SchoolCode(Resource):
    @swagger.doc({
        'tags': ['학교'],
        'description': '학교 정보 조회',

        'parameters': [
            {
                'name': 'keyword',
                'description': '사용자의 검색 키워드(optional)',
                'in': 'query',
                'type': 'String'
            }
        ],

        'responses': {
            '200': {
                'description': '검색 성공(데이터 있음)',
                'examples': {
                    'application/json': [
                        {
                            "code": "C100000376",
                            "name": "대덕여자고등학교",
                            "region": "부산광역시"
                        },
                        {
                            "code": "G100000167",
                            "name": "대덕고등학교",
                            "region": "대전광역시"
                        },
                        {
                            "code": "G100000168",
                            "name": "대덕공업고등학교",
                            "region": "대전광역시"
                        },
                        {
                            "code": "G100000169",
                            "name": "대덕여자고등학교",
                            "region": "대전광역시"
                        },
                        {
                            "code": "G100000170",
                            "name": "대덕소프트웨어마이스터고등학교",
                            "region": "대전광역시"
                        },
                        {
                            "code": "Q100000193",
                            "name": "대덕종합고등학교",
                            "region": "전라남도"
                        }
                    ]
                }
            },
            '204': {
                'description': '검색 실패(데이터 없음)'
            }
        }
    })
    def get(self):
        data = [school for school in list(SchoolModel.objects().as_pymongo()) if request.args.get('keyword', default='') in school['name']]
        for idx in range(len(data)):
            del data[idx]['_id']
            del data[idx]['web_url']

        return data if data else '', 204
