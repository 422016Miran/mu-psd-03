<script>
  import { goto } from "$app/navigation";
  import { selected } from './store.js';
  let name = "Report"; // 変数を宣言する。
  let questions = [
    { id: 1, text: "札幌" },
    { id: 2, text: "東京" },
    { id: 3, text: "名古屋" },
    { id: 4, text: "大阪" },
    { id: 5, text: "福岡" },
    { id: 6, text: "那覇" },
  ];

  let weatherData = {
    1: { weather: "曇り", temperature: "23°C" },
    2: { weather: "晴れ", temperature: "28°C" },
    3: { weather: "雨", temperature: "20°C" },
    4: { weather: "晴れ", temperature: "27°C" },
    5: { weather: "曇り", temperature: "25°C" },
    6: { weather: "晴れ", temperature: "30°C" },
  };

  let errorMessage = '';

  let selectedQuestion = questions[0].id;
  $: selectedWeather = weatherData[selectedQuestion];

  // 日付と時間を取得する関数
  function getCurrentDateTime() {
    const now = new Date();
    const date = now.toLocaleDateString();
    const time = now.toLocaleTimeString([], {
      hour: "2-digit",
      minute: "2-digit",
    });
    return `${date} ${time}`;
  }

  // 天気予報のページに移動する関数
  function navigateToSearch(event) {
    event.preventDefault(); // Prevent the default form submission
    //goto("/search"); // /searchページに遷移
    if (!$selected) {
      errorMessage = '※地名を選択してください。';
    } else {
      errorMessage = '';
      goto('/search'); // /searchページに遷移
    }
  }

  // 初期化時に日付と時間を設定
  let currentDateTime = getCurrentDateTime();

  // 1秒ごとに日付と時間を更新
  setInterval(() => {
    currentDateTime = getCurrentDateTime();
  }, 1000);

  // 各セクションにスクロールする関数
  function scrollToSection(id) {
    const section = document.getElementById(id);
    if (section) {
      section.scrollIntoView({ behavior: 'smooth' });
    }
  }
  // メニューの表示/非表示を管理する変数
  let showMenu = false;
</script>

<main>
  <div class="menu-bar">
    <button class="menu-button" on:click={() => showMenu = !showMenu}>Menu</button>
    <div class="menu-items {showMenu ? 'show' : ''}">
      <button on:click={() => { showMenu = false; scrollToSection('subtitle'); }}>全国</button>
      <button on:click={() => { showMenu = false; scrollToSection('call'); }}>検索</button>
      <button on:click={() => { showMenu = false; scrollToSection('usage'); }}>使い方</button>
    </div>
  </div>

  <h1 class="title">ウェザーリポート</h1>
  <div class="date">現在の日時: {currentDateTime}</div><br>
   <div id="subtitle" class="subtitle">★全国各地の天気予報★</div>
   <!-- 変数が描画される -->
  <div />
 
  <div class="outer-container">
    <div class="container">
      <img src="/images/japanmap.jpg" alt="日本地図">
      <div class="button-container">
      {#each questions as question}
        <label>
          <input type="radio" bind:group={selectedQuestion} value={question.id} style="display: none;" />
          <button class="round-button" on:click={() => selectedQuestion = question.id}>{question.text}</button>
        </label>
      {/each}
      </div>
      <h2 class="weather">{questions.find(q => q.id === selectedQuestion).text}の天気</h2>
      <div class="weather-info">
        <p>天気: {selectedWeather.weather}</p>
        <p>気温: {selectedWeather.temperature}</p>
      </div>
    </div>
  </div>
  <!--<a href="/getdata">get data page</a>-->
  <br>
  <div class="dotted-line"></div>

  <div class="subtitle">★明日の天気予報★</div>
  <p id="call" class="call">下の欄から地名を選んでください</p>
  <form on:submit={navigateToSearch}>
    <select bind:value={$selected}>
      <option value="" disabled selected>選択してください</option>
      {#each questions as question}
        <option value={question}>
          {question.text}
        </option>
      {/each}
    </select>
    <br />
    <button type="search">検索</button>
  </form>
  {#if errorMessage}
  <p class="error">{errorMessage}</p>
  {/if}

  <p class="dotted-line">
   　検索した地名: {$selected && $selected.text ? $selected.text : ""}
  </p>
  
  <h3 id="usage" class="usage">【使い方】</h3>
  
    　ウェザーリポートをご覧いただきありがとうございます。以下にこのWebアプリを使用する上での説明が書いてあります。<br
    />
    <div class="express">【全国各地の天気予報】</div>
    ・日本地図の右に各地名が記されたボタンが配置されています。そのボタンを押すと当日の地域の天気と気温が表示されます。<br>
    <div class="express">【明日の天気予報】</div>
    ・ボックスに地名が選択肢として用意されているので、希望の地名を選んでください。<br
    />
    ・検索ボタンを押すと、天気予報のページに移動します。<br>

  
</main>

<style>
  /* class=testとなっている箇所に適用されるスタイル */
  main {
    background-color: antiquewhite;
  }
  .title {
    font-size: 70px;
    color: snow;
    background-color: blue;
    text-align: center;
    background-image: url("./background.jpg");
    background-size: cover;
    margin: 0%;
  }
  /*メニュー*/
  .menu-bar {
    position: relative;
    display: inline-block;
    width: 80px;
  }
  .menu-button {
    font-size: 15px;
    width: 100%;
    height: 45px;
    padding: 10px;
    background-color: black;
    color: white;
    border: none;
    cursor: pointer;
  }
  .menu-button:hover {
    background-color: #0045b3;
  }
  .menu-items {
    display: none;
    position: absolute;
    width: 100%;
    background-color: white;
    border: 1px solid #ccc;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }
  .menu-items.show {
    display: block;
  }
  .menu-items button {
    font-size: 15px;
    display: block;
    width: 100%;
    padding: 10px;
    background-color: white;
    border: none;
    cursor: pointer;
    text-align: center;
    border-bottom: 1px solid #ccc; 
  }
  .menu-items button:hover {
    background-color: #f0f0f0;
  }

  .date {
    text-align: right;
    margin-right: 10px;
  }

  .subtitle {
    font-size: 30px;
    text-align: center;
  }

  .outer-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }
  .container {
    position: relative;
    display: inline-block;
  }
  img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: auto;
  }
  .button-container {
    display: flex;
    flex-direction: column; /* 縦並びにする */
    align-items: center;
    position: absolute;
    right: 10px; /* 画像の右端に配置 */
    top: 50%;
    transform: translateY(-50%);
  }
  .round-button {
    width: 60px;
    height: 40px;
    border-radius: 50%;
    background-color: gray;
    color: white;
    border: none;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    margin: 5px;
  }

  .weather {
    text-align: center;
  }
  .weather-info {
    text-align: center;
    font-size: 20px;
  }

  .call {
    text-align: center;
    font-size: larger;
  }

  form {
    text-align: center;
  }
  select {
    text-align: center;
    width: 85px;
    height: 30px;
  }
  button {
    width: 85px;
    max-width: 100%;
  }
  .error {
    text-align: center;
    color: red;
  }

  .dotted-line {
    border-bottom: 2px dotted black;
    padding-bottom: 10px;
  }

  .usage {
    font-size: 30px;
    margin: 0%;
  }
  .express {
    font-size: larger;
  }
</style>
