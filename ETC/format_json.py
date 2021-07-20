String = 'string'
Boolean = 'bollean'
Number = 'number'
Object = 'object'

"""
주석의 용어 정리

range = 범위
len = 길이
() 열린 구간 기호
[] 닫힌 구간 기호
    ex) len[0,100] = 0~100, 100포함 하는 수
    ex) len[0, 101) = 정수형의 경우     :len[0, 101) = 0~100
                      정수형이 아닐 경우 :len[0, 101) = 0~100.999999...
|(파이프라인) = (B|A) => A일때 B

"""


def format_json_____(key=''):
    key = \
        {
            'slug': String,  # 상품 고유 슬러그
            'type': 'tangible' or 'downloadable' or 'ticket' or 'custom',  # 필수 항목
            'available': Boolean,  # 상품 구매 가능 여부
            'bundled': Boolean,  # 상품 추가 구매 품목 여부
            'vendor': String,  # 상품이 소속된 입점사
            'brand': String or None,  # 상품이 소속된 브랜드
            'collections':
                [
                    String
                ],  # 상품이 소속된 콜렉션 목록 # unique # ls_len[,10]
            'catalogs':  # 상품 카탈로그 목록
                [
                    {
                        'title':
                            {
                                '{lang}': String or None  # 카탈로그 제목 # {lang}len[0, 100]
                            },
                        'description':
                            {
                                '{lang}': String or None  # 카탈로그 설명 # {lang}len[0,10000]
                            },
                        'image': String or None  # 카탈로그 이미지
                    }
                ],
            'thumbnail': String or None,  # 상품 썸네일
            'name':
                {
                    '{lang}': String or None  # 상품의 이름 # 필수
                },
            'summary':
                {
                    '{lang}': String or None  # 상품의 요약 설명
                },
            'description':
                {
                    '{lang}': String or None  # 상품에 대한 설명 # {lang}len[0, 50000]
                },
            'notices':
                [
                    {
                        'slug': String,  # 알림성 컨텐츠 슬러그 # 한국의 상품 고시 정보는 "legal-KR_"로 시작하는 슬러그로 예약 사용
                        'title':
                            {
                                '{lang}': String or None  # 알림성 컨텐츠 제목 # {lang}len[0, 100]
                            },
                        'items':  # 알림성 컨텐츠 세부 목록
                            [
                                {
                                    'title':
                                        {
                                            '{lang}': String or None  # 세부 목록의 제목 # {lang}len[0, 100]
                                        },
                                    'description':
                                        {
                                            '{lang}': String or None  # 세부 컨텐츠의 설명 # {lang}len[0, 10000]
                                        }
                                }
                            ]
                    }
                ],
            'price':  # 상품의 가격 설정 정보 # 필수
                {
                    'original': Number,  # 상품의 정가 # len[0,]
                    'type': String or 'fixed' or 'dynamic'  # 필수 # fixed=고정가격 # dynamic=동적가격
                },
            'discount':  # 상품 할인 정보
                {
                    'type': 'percentage' or 'fixed' or None,  # 필수 # 상품의 할인 방식
                    'value': Number or None  # (필수, None | type==None)
                    # (필수, range[0,], 초과불허 | type=='fixed')
                    # (필수, range[1,100], Integer | type=='percentage')
                },
            'taxCategories':  # 상품이 소속된 세금 카테고리 목록 # unique # len[,10]
                [
                    String
                ],
            'shipping':  # 상품 배송 설정 # 필수 # '' or 'tangible'
                {
                    'methods':
                        [
                            String  # 상품이 지원하는 배송 방식 목록
                        ],
                    'calculation': String or 'bundled' or 'separated' or None  # 상품의 계산 방식 # 필수
                },
            'options':  # 상품의 옵션 len[,5]
                [
                    {
                        'name':
                            {
                                '{lang}': String or None  # 옵션 이름 # {lang}len[0,50]
                            },
                        'priority': Number,  # 옵션의 정렬 순서 # Integer_len[0,4]
                        'variations':  # 옵션의 선택지 목록 # len[,120]
                            [
                                {
                                    'value':
                                        {
                                            '{lang}': String or None  # 옵션의 선택지 값 # {lang]len[0,150]
                                        },
                                    'priority': Number  # 옵션 선택지의 정렬 순서 # Integer_ran[0,119]
                                }
                            ]
                    }
                ],
            'bundles':  # 상품의 추가 구매 옵션 목록 # len[,30]
                [
                    {
                        'required': Boolean,  # 상품의 추가 구매 여부
                        'name':
                            {
                                '{lang}': String or None  # 추가 구매 옵션의 이름 # {lang}len[0,100]
                            },
                        'items':  # 추가 구매 옵션의 품목
                            [
                                {
                                    'product': String,  # 추가 구매 옵션 품목의 상품 # 필수
                                    'variant': String  # 추가 구매 옵션 품목의 세부 품목                                    }
                                }
                            ]
                    }
                ],
            'model_name': {},  # varchar(50)
            'weight': {},  # varchar(50)
            'dimension': {},  # varchar(50)
            'payload': {},  # float
            'reach': {},  # float
            'autonomous': {},  # boolean
            'warranty': {},  # integer
            'related_doc_url_1': {},  # varchar(255)
            'related_doc_url_2': {},  # varchar(255)
            'related_doc_url_3': {},  # varchar(255)
            'related_doc_url_4': {},  # varchar(255)
            'related_doc_url_5': {},  # varchar(255)
            'related_doc_url_6': {},  # varchar(255)
            'meta': Object  # 상품의 커스텀 정보
        }
    return key


def format_json(key='') -> object:
    key = \
        {
            'slug': '',
            'type': 'custom',
            'available': '',
            'bundled': '',
            'vendor': '',
            'brand': '',
            'collections': [],
            'catalogs':
                [
                    {
                        'title': {},
                        'description': {},
                        'image': ''
                    }
                ],
            'thumbnail': '',
            'name': {},
            'summary': {},
            'description': {},
            'notices': [{'slug': '',
                         'title': {},
                         'items': [{
                             'title': {},
                             'description': {}}]}],
            'price':
                {
                    'original': '',
                    'type': ''
                },
            'discount':
                {
                    'type': '',
                    'value': ''
                },
            'taxCategories':
                [],
            'shipping':
                {
                    'methods': [],
                    'calculation': ''
                },
            'options':
                [
                    {
                        'name': {},
                        'priority': '',
                        'variations':
                            [
                                {
                                    'value': {},
                                    'priority': ''
                                }
                            ]
                    }
                ],
            'bundles':
                [
                    {
                        'required': '',
                        'name': {},
                        'items':
                            [
                                {
                                    'product': '',
                                    'variant': ''
                                }
                            ]
                    }
                ],
            'model_name': {},  # varchar(50)
            'weight': {},  # varchar(50)
            'dimension': {},  # varchar(50)
            'payload': {},  # float
            'reach': {},  # float
            'autonomous': {},  # boolean
            'warranty': {},  # integer
            'related_doc_url_1': {},  # varchar(255)
            'related_doc_url_2': {},  # varchar(255)
            'related_doc_url_3': {},  # varchar(255)
            'related_doc_url_4': {},  # varchar(255)
            'related_doc_url_5': {},  # varchar(255)
            'related_doc_url_6': {},  # varchar(255)
            'meta': Object  # 상품의 커스텀 정보
        }
    return key
