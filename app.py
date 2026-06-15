<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>주말에 뭐 보지?</title>
  <style>
    /* ===================== 기본 리셋 & 전체 레이아웃 ===================== */
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: #141414;   /* 넷플릭스 배경색 */
      color: #fff;
      font-family: 'Segoe UI', sans-serif;
      min-height: 100vh;
    }

    /* ===================== 헤더 ===================== */
    header {
      background: linear-gradient(180deg, #000 0%, #141414 100%);
      text-align: center;
      padding: 50px 20px 30px;
    }

    header h1 {
      font-size: clamp(2rem, 6vw, 4rem);  /* 반응형 폰트 크기 */
      color: #E50914;                      /* 넷플릭스 빨간색 */
      letter-spacing: 2px;
      text-shadow: 0 0 20px rgba(229,9,20,0.5);
      margin-bottom: 10px;
    }

    header p {
      color: #aaa;
      font-size: 1rem;
      margin-bottom: 30px;
    }

    /* ===================== 버튼 영역 ===================== */
    .btn-area {
      display: flex;
      justify-content: center;
      gap: 20px;
      flex-wrap: wrap;
      margin-bottom: 10px;
    }

    .btn {
      padding: 14px 32px;
      font-size: 1rem;
      font-weight: bold;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      transition: transform 0.2s, box-shadow 0.2s;
    }

    .btn:hover {
      transform: scale(1.05);
      box-shadow: 0 6px 20px rgba(229,9,20,0.4);
    }

    /* 버튼 1: 평점순 정렬 */
    .btn-sort {
      background-color: #E50914;
      color: #fff;
    }

    /* 버튼 2: 랜덤 추천 */
    .btn-random {
      background-color: #fff;
      color: #141414;
    }

    /* ===================== 카드 그리드 ===================== */
    #card-container {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 20px;
      padding: 30px 40px;
      max-width: 1400px;
      margin: 0 auto;
    }

    /* 개별 카드 */
    .card {
      background-color: #1f1f1f;
      border-radius: 8px;
      overflow: hidden;
      transition: transform 0.3s, box-shadow 0.3s;
      cursor: pointer;
    }

    .card:hover {
      transform: translateY(-8px) scale(1.02);
      box-shadow: 0 12px 30px rgba(229,9,20,0.3);
    }

    .card img {
      width: 100%;
      height: 280px;
      object-fit: cover;
      display: block;
    }

    .card-info {
      padding: 12px;
    }

    .card-title {
      font-size: 0.95rem;
      font-weight: bold;
      margin-bottom: 5px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .card-genre {
      font-size: 0.78rem;
      color: #aaa;
      margin-bottom: 6px;
    }

    .card-rating {
      font-size: 0.85rem;
      color: #E50914;
      font-weight: bold;
    }

    .card-synopsis {
      font-size: 0.75rem;
      color: #bbb;
      margin-top: 6px;
      line-height: 1.4;
      display: -webkit-box;
      -webkit-line-clamp: 2;       /* 2줄로 자르기 */
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .card-link {
      display: inline-block;
      margin-top: 10px;
      font-size: 0.75rem;
      color: #E50914;
      text-decoration: none;
    }

    .card-link:hover { text-decoration: underline; }

    /* ===================== 랜덤 추천 모달 ===================== */
    #modal-overlay {
      display: none;              /* 기본은 숨김 */
      position: fixed;
      inset: 0;                   /* top/right/bottom/left 모두 0 */
      background: rgba(0,0,0,0.85);
      z-index: 1000;
      justify-content: center;
      align-items: center;
      animation: fadeIn 0.3s ease;
    }

    /* display:none -> flex 로 바꿀 때 쓸 클래스 */
    #modal-overlay.active { display: flex; }

    @keyframes fadeIn {
      from { opacity: 0; }
      to   { opacity: 1; }
    }

    #modal-box {
      background: #1f1f1f;
      border: 2px solid #E50914;
      border-radius: 12px;
      padding: 30px;
      max-width: 420px;
      width: 90%;
      text-align: center;
      position: relative;
      animation: popUp 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    @keyframes popUp {
      from { transform: scale(0.5); opacity: 0; }
      to   { transform: scale(1);   opacity: 1; }
    }

    #modal-box img {
      width: 100%;
      max-height: 300px;
      object-fit: cover;
      border-radius: 8px;
      margin-bottom: 16px;
    }

    #modal-box h2 {
      font-size: 1.5rem;
      color: #E50914;
      margin-bottom: 8px;
    }

    #modal-box .modal-genre  { color: #aaa; font-size: 0.9rem; margin-bottom: 6px; }
    #modal-box .modal-rating { color: #fff; font-size: 1rem; margin-bottom: 12px; }
    #modal-box .modal-synopsis { color: #ccc; font-size: 0.88rem; line-height: 1.5; margin-bottom: 16px; }

    #modal-box .modal-link {
      display: inline-block;
      background: #E50914;
      color: #fff;
      padding: 10px 24px;
      border-radius: 6px;
      text-decoration: none;
      font-weight: bold;
      font-size: 0.9rem;
      margin-bottom: 12px;
    }

    /* 닫기 버튼 */
    #modal-close {
      position: absolute;
      top: 12px;
      right: 16px;
      font-size: 1.5rem;
      background: none;
      border: none;
      color: #aaa;
      cursor: pointer;
    }
    #modal-close:hover { color: #fff; }

    /* ===================== 반짝이는 타이틀 효과 (랜덤 결과) ===================== */
    #modal-box h2.flash {
      animation: flash 0.6s ease 3;
    }
    @keyframes flash {
      0%, 100% { color: #E50914; }
      50%       { color: #ffcc00; text-shadow: 0 0 20px #ffcc00; }
    }

    /* ===================== 안내 텍스트 ===================== */
    #hint {
      text-align: center;
      color: #555;
      font-size: 0.9rem;
      padding: 20px;
    }
  </style>
</head>
<body>

  <!-- ====== 헤더 ====== -->
  <header>
    <h1>🎬 주말에 뭐 보지?</h1>
    <p>넷플릭스 인기 작품 20선 · 오늘 저녁을 책임집니다</p>
    <div class="btn-area">
      <!-- 버튼 1: 평점 높은 순 정렬 -->
      <button class="btn btn-sort" onclick="loadSorted()">⭐ 평점 높은 순 정렬</button>
      <!-- 버튼 2: 랜덤 추천 -->
      <button class="btn btn-random" onclick="loadRandom()">🎲 뭐 볼지 랜덤 추천!</button>
    </div>
  </header>

  <!-- ====== 안내 텍스트 ====== -->
  <p id="hint">위 버튼을 눌러 작품을 확인하세요!</p>

  <!-- ====== 카드 목록 ====== -->
  <div id="card-container"></div>

  <!-- ====== 랜덤 추천 모달 ====== -->
  <div id="modal-overlay" onclick="closeModal(event)">
    <div id="modal-box">
      <button id="modal-close" onclick="closeModal(null)">✕</button>
      <img id="modal-img" src="" alt="포스터" />
      <h2 id="modal-title"></h2>
      <p class="modal-genre"  id="modal-genre"></p>
      <p class="modal-rating" id="modal-rating"></p>
      <p class="modal-synopsis" id="modal-synopsis"></p>
      <a id="modal-link" href="#" target="_blank" class="modal-link">▶ 넷플릭스에서 보기</a>
    </div>
  </div>

  <script>
    // ===================================================
    // 카드 HTML 생성 함수
    // movie: 작품 데이터 객체 하나
    // ===================================================
    function createCard(movie) {
      return `
        <div class="card">
          <img src="${movie.poster}" alt="${movie.title} 포스터"
               onerror="this.src='https://via.placeholder.com/400x600/1f1f1f/E50914?text=No+Image'"/>
          <div class="card-info">
            <div class="card-title">${movie.title}</div>
            <div class="card-genre">${movie.genre}</div>
            <div class="card-rating">⭐ ${movie.rating} / 10</div>
            <div class="card-synopsis">${movie.synopsis}</div>
            <a class="card-link" href="${movie.link}" target="_blank">▶ 넷플릭스에서 보기</a>
          </div>
        </div>
      `;
    }

    // ===================================================
    // 버튼 1: 평점 높은 순 정렬
    // Flask /api/sorted 엔드포인트에 GET 요청
    // ===================================================
    function loadSorted() {
      document.getElementById('hint').style.display = 'none';

      fetch('/api/sorted')
        .then(res => res.json())          // JSON 파싱
        .then(movies => {
          const container = document.getElementById('card-container');
          // 카드를 모두 지우고 다시 그리기
          container.innerHTML = movies.map(createCard).join('');
        })
        .catch(err => alert('데이터를 불러오지 못했습니다: ' + err));
    }

    // ===================================================
    // 버튼 2: 랜덤 추천
    // Flask /api/random 엔드포인트에 GET 요청
    // ===================================================
    function loadRandom() {
      fetch('/api/random')
        .then(res => res.json())
        .then(movie => {
          // 모달에 데이터 채우기
          document.getElementById('modal-img').src      = movie.poster;
          document.getElementById('modal-title').textContent    = '🎉 ' + movie.title;
          document.getElementById('modal-genre').textContent    = movie.genre;
          document.getElementById('modal-rating').textContent   = '⭐ ' + movie.rating + ' / 10';
          document.getElementById('modal-synopsis').textContent = movie.synopsis;
          document.getElementById('modal-link').href             = movie.link;

          // 모달 표시
          document.getElementById('modal-overlay').classList.add('active');

          // 제목 반짝 효과
          const title = document.getElementById('modal-title');
          title.classList.remove('flash');
          void title.offsetWidth;   // 리플로우로 애니메이션 재시작
          title.classList.add('flash');
        })
        .catch(err => alert('데이터를 불러오지 못했습니다: ' + err));
    }

    // ===================================================
    // 모달 닫기
    // event가 있으면 배경(overlay) 클릭인지 확인
    // ===================================================
    function closeModal(event) {
      if (event && event.target !== document.getElementById('modal-overlay')) return;
      document.getElementById('modal-overlay').classList.remove('active');
    }
  </script>
</body>
</html>
