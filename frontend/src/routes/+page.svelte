<script>
  import { goto } from '$app/navigation';
  let name = "Report"; // 変数を宣言する。
  let questions = [
    { id: 1, text: '札幌'},
    { id: 2, text: '東京'},
    { id: 3, text: '名古屋'},
    { id: 4, text: '大阪'},
    { id: 5, text: '福岡'},
    { id: 6, text: '那覇'}
  ];
  let selected;

  // 日付と時間を取得する関数
  function getCurrentDateTime() {
    const now = new Date();
    const date = now.toLocaleDateString();
    const time = now.toLocaleTimeString();
    return `${date} ${time}`;
  }
  
  // 天気予報のページに移動する関数
  function navigateToSearch(event) {
    event.preventDefault(); // Prevent the default form submission
    goto('/search');  // /searchページに遷移
  }

  // 初期化時に日付と時間を設定
  let currentDateTime = getCurrentDateTime();

  // 1秒ごとに日付と時間を更新
  setInterval(() => {
    currentDateTime = getCurrentDateTime();
  }, 1000);
</script>

<main>
  <h1 class="title">ウェザーリポート</h1>
  <div>Weather {name}</div>
  <!-- 変数が描画される -->
  <div />
  <!--<a href="/getdata">get data page</a>-->

  <p>地名を選んでください</p>
  <form on:submit={navigateToSearch}>
    <select bind:value={selected}>
      {#each questions as question}
        <option value={question}>
          {question.text}
        </option>
      {/each}
    </select>
    <br>
    <button type="weather">検索</button>
  </form>
  <p>検索した地名: {selected ? selected.text : '[waiting...]'}</p>
  ------------------------------------------------------------------
  <h3>【使い方】</h3>
  <p>現在の日時: {currentDateTime}</p>
</main>

<style>
  /* class=testとなっている箇所に適用されるスタイル */
  .title {
    color: snow;
    background-color: blue;
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
</style>
