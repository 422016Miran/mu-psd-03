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
  //let selected;

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
    goto("/search"); // /searchページに遷移
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
  <div class="date">現在の日時: {currentDateTime}</div>
  <div>Weather {name}</div>
  <!-- 変数が描画される -->
  <div />
  <div>
    <img src="/japanmap.jpg" alt="日本地図" />
  </div>
  <!--<a href="/getdata">get data page</a>-->

  <p class="call">地名を選んでください</p>
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
  <p class="dotted-line">
    検索した地名: {$selected && $selected.text ? $selected.text : ""}
  </p>

  <h3>【使い方】</h3>
  <p>
    ウェザーリポートをご覧いただきありがとうございます。以下にこのWebアプリを使用する上での説明が書いてあります。<br
    />
    ・ボックスに地名が選択肢として用意されているので、希望の地名を選んでください。<br
    />
    ・検索ボタンを押すと、天気予報のページに移動します。
  </p>
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
  }
  .date {
    text-align: right;
    margin-right: 30px;
  }
  img {
    width: auto;
    height: auto;
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
  .dotted-line {
    border-bottom: 2px dotted black;
    padding-bottom: 10px;
  }
</style>
