# =====================================================
# app.py - 넷플릭스 작품 추천 웹 서비스 (Flask 백엔드)
# =====================================================
# 실행 방법:
#   1. pip install flask
#   2. python app.py
#   3. 브라우저에서 http://127.0.0.1:5000 접속
# =====================================================

from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# -------------------------------------------------------
# 더미 데이터: 넷플릭스 인기 작품 20개
# 각 항목: 제목, 장르, 평점(10점), 포스터 URL, 줄거리, 넷플릭스 링크
# -------------------------------------------------------
MOVIES = [
    {
        "title": "오징어 게임",
        "genre": "스릴러/드라마",
        "rating": 9.2,
        "poster": "https://images.unsplash.com/photo-1626814026160-2237a95fc5a0?w=400&h=600&fit=crop",
        "synopsis": "456억 원의 상금을 걸고 목숨을 건 서바이벌 게임에 참가한 사람들의 이야기.",
        "link": "https://www.netflix.com/title/81040344"
    },
    {
        "title": "기생충",
        "genre": "블랙코미디/드라마",
        "rating": 9.5,
        "poster": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=400&h=600&fit=crop",
        "synopsis": "전원 백수인 기택네 가족이 부유한 박 사장 가족에게 기생하며 벌어지는 사건.",
        "link": "https://www.netflix.com/title/81243606"
    },
    {
        "title": "더 글로리",
        "genre": "복수/드라마",
        "rating": 8.8,
        "poster": "https://images.unsplash.com/photo-1509347528160-9a9e33742cdb?w=400&h=600&fit=crop",
        "synopsis": "학창 시절 폭력 피해자가 완벽한 복수를 위해 인생 전체를 건 이야기.",
        "link": "https://www.netflix.com/title/81425066"
    },
    {
        "title": "나르코스",
        "genre": "범죄/실화",
        "rating": 8.8,
        "poster": "https://images.unsplash.com/photo-1612036782180-6f0b6cd846fe?w=400&h=600&fit=crop",
        "synopsis": "콜롬비아 마약왕 파블로 에스코바르의 흥망성쇠를 다룬 실화 기반 드라마.",
        "link": "https://www.netflix.com/title/80025172"
    },
    {
        "title": "기묘한 이야기",
        "genre": "SF/공포",
        "rating": 8.7,
        "poster": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=400&h=600&fit=crop",
        "synopsis": "소년이 사라진 작은 마을에서 초자연적 현상과 맞닥뜨리는 아이들의 이야기.",
        "link": "https://www.netflix.com/title/80057281"
    },
    {
        "title": "종이의 집",
        "genre": "범죄/액션",
        "rating": 8.6,
        "poster": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=400&h=600&fit=crop",
        "synopsis": "교수라 불리는 천재 범죄자가 이끄는 강도단의 완벽한 조폐국 침입 작전.",
        "link": "https://www.netflix.com/title/80192098"
    },
    {
        "title": "위처",
        "genre": "판타지/액션",
        "rating": 8.2,
        "poster": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=600&fit=crop",
        "synopsis": "괴물 사냥꾼 게롤트가 운명으로 얽힌 공주와 마법사와 함께하는 모험.",
        "link": "https://www.netflix.com/title/80189685"
    },
    {
        "title": "브리저튼",
        "genre": "로맨스/드라마",
        "rating": 7.9,
        "poster": "https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?w=400&h=600&fit=crop",
        "synopsis": "19세기 런던 사교계를 배경으로 펼쳐지는 화려하고 달콤한 로맨스.",
        "link": "https://www.netflix.com/title/80232398"
    },
    {
        "title": "블랙 미러",
        "genre": "SF/디스토피아",
        "rating": 8.5,
        "poster": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=400&h=600&fit=crop",
        "synopsis": "기술이 지배하는 미래 사회의 어두운 단면을 그린 앤솔로지 드라마.",
        "link": "https://www.netflix.com/title/70264888"
    },
    {
        "title": "오자크",
        "genre": "범죄/스릴러",
        "rating": 8.5,
        "poster": "https://images.unsplash.com/photo-1551434678-e076c223a692?w=400&h=600&fit=crop",
        "synopsis": "마약 카르텔에 빚진 가족이 호수 마을로 도망쳐 돈세탁을 벌이는 이야기.",
        "link": "https://www.netflix.com/title/80117552"
    },
    {
        "title": "킹덤",
        "genre": "좀비/역사",
        "rating": 8.4,
        "poster": "https://images.unsplash.com/photo-1508739773434-c26b3d09e071?w=400&h=600&fit=crop",
        "synopsis": "조선 시대를 배경으로 의문의 역병과 권력 암투에 맞서는 세자의 사투.",
        "link": "https://www.netflix.com/title/80180171"
    },
    {
        "title": "셜록",
        "genre": "미스터리/추리",
        "rating": 9.1,
        "poster": "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=400&h=600&fit=crop",
        "synopsis": "현대 런던을 배경으로 천재 탐정 셜록 홈즈와 왓슨의 사건 해결기.",
        "link": "https://www.netflix.com/title/70202589"
    },
    {
        "title": "마인드헌터",
        "genre": "범죄/스릴러",
        "rating": 8.9,
        "poster": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=600&fit=crop",
        "synopsis": "FBI 요원들이 연쇄살인마 심리를 분석하며 범죄 프로파일링을 개척하는 이야기.",
        "link": "https://www.netflix.com/title/80232911"
    },
    {
        "title": "에밀리, 파리에 가다",
        "genre": "로맨스/코미디",
        "rating": 7.3,
        "poster": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=400&h=600&fit=crop",
        "synopsis": "시카고 마케터 에밀리가 파리로 발령나 겪는 문화 충돌과 로맨스.",
        "link": "https://www.netflix.com/title/81037371"
    },
    {
        "title": "수리남",
        "genre": "범죄/액션",
        "rating": 7.8,
        "poster": "https://images.unsplash.com/photo-1511367461989-f85a21fda167?w=400&h=600&fit=crop",
        "synopsis": "수리남을 장악한 마약 대부를 잡기 위해 일반인이 국정원 작전에 투입된다.",
        "link": "https://www.netflix.com/title/81166782"
    },
    {
        "title": "지옥",
        "genre": "공포/SF",
        "rating": 7.6,
        "poster": "https://images.unsplash.com/photo-1519638831568-d9897f54ed69?w=400&h=600&fit=crop",
        "synopsis": "갑작스러운 지옥행 선고와 괴물 출현으로 혼란에 빠진 세상을 그린 이야기.",
        "link": "https://www.netflix.com/title/81441081"
    },
    {
        "title": "D.P.",
        "genre": "군대/드라마",
        "rating": 8.3,
        "poster": "https://images.unsplash.com/photo-1534367610401-9f5ed68180aa?w=400&h=600&fit=crop",
        "synopsis": "탈영병을 잡는 군무이탈체포조 DP 요원들이 마주하는 현실과 인간 군상.",
        "link": "https://www.netflix.com/title/81280917"
    },
    {
        "title": "소년심판",
        "genre": "법정/드라마",
        "rating": 8.1,
        "poster": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=400&h=600&fit=crop",
        "synopsis": "소년범을 혐오하는 판사가 소년부에 부임하며 마주하는 청소년 범죄의 현실.",
        "link": "https://www.netflix.com/title/81500416"
    },
    {
        "title": "나의 해방일지",
        "genre": "힐링/드라마",
        "rating": 8.6,
        "poster": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=400&h=600&fit=crop",
        "synopsis": "답답한 일상에서 해방되고 싶은 세 남매와 미스터리한 남자의 잔잔한 이야기.",
        "link": "https://www.netflix.com/title/81518709"
    },
    {
        "title": "이상한 변호사 우영우",
        "genre": "법정/드라마",
        "rating": 8.7,
        "poster": "https://images.unsplash.com/photo-1436450412740-6b988f486c6b?w=400&h=600&fit=crop",
        "synopsis": "자폐 스펙트럼을 가진 천재 변호사 우영우의 유쾌하고 따뜻한 성장 이야기.",
        "link": "https://www.netflix.com/title/81518991"
    },
]


# -------------------------------------------------------
# 라우트 1: 메인 페이지 렌더링
# -------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')


# -------------------------------------------------------
# 라우트 2: 평점 높은 순으로 정렬된 작품 목록 반환 (JSON)
# -------------------------------------------------------
@app.route('/api/sorted')
def get_sorted():
    # rating 기준 내림차순 정렬
    sorted_movies = sorted(MOVIES, key=lambda x: x['rating'], reverse=True)
    return jsonify(sorted_movies)


# -------------------------------------------------------
# 라우트 3: 랜덤 작품 1개 반환 (JSON)
# -------------------------------------------------------
@app.route('/api/random')
def get_random():
    pick = random.choice(MOVIES)
    return jsonify(pick)


# -------------------------------------------------------
# 앱 실행
# -------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
