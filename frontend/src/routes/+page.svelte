<script>
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
  
  async function submit() {
     // APIにアクセスする定型文
     const response = await fetch("http://localhost:5000/calc/" + income + "/" + rooms + "/" + age);
    // 表示用変数にデータを入れると、画面も再描画される。
    data = await response.json();
  }

  // 初期化時に日付と時間を設定
  let currentDateTime = getCurrentDateTime();

  // 1秒ごとに日付と時間を更新
  setInterval(() => {
    currentDateTime = getCurrentDateTime();
  }, 1000);
</script>

<main>
  <h1 class="title">Welcome to Weather Report!</h1>
  <div>Weather {name}</div>
  <!-- 変数が描画される -->
  <div />
  <a href="/getdata">get data page</a>

  <p>地名を選んでください</p>
  <form on:submit>
    <select bind:value={selected}>
      {#each questions as question}
        <option value={question}>
          {question.text}
        </option>
      {/each}
    </select>
    <br>
    <button on:click={submit}>検索</button>
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
