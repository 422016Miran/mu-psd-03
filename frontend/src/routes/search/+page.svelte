<!-- Frontendでの処理ロジックを記述 -->
<script>
  import {selected} from '../store.js';
  let title = "Data Get";
  let income;
  let rooms; 
  let age;
  let data = []; // htmlタグの方の{datalist}の部分と同じ変数

  async function findData() {
    // APIにアクセスする定型文
    const response = await fetch("http://localhost:5000/calc/" + income + "/" + rooms + "/" + age);
    // 表示用変数にデータを入れると、画面も再描画される。
    data = await response.json();
  }
</script>

<main>
  <h1 class="title">{$selected ? $selected.text : '[waiting...]'}の天気予報</h1>
  <div class="parameter">
    <table>
      <tr>
	      <td>天気</td>
  	    <td><input bind:value={income} /></td>
      </tr>
      <tr>
  	    <td>気温</td>
	      <td><input bind:value={rooms} /></td>
      </tr>
      <tr>
  	    <td>降水量</td>
	      <td><input bind:value={age} /></td>
      </tr>
    </table>
  </div>
  <button on:click={findData}>Get Data.</button>
  <div />
  <hr />
  <table>
  <tr>
  	<td>Price</td>
        <td>{data.price}</td>
  </tr>
  </table>
  <hr />
  <a href="/">戻る</a>
</main>

<!-- 画面の装飾をする -->
<style>
  /* class=titleとなっている箇所を装飾する */
  main {
    background-color: antiquewhite;
  }
  .title {
    color: snow;
    background-color: rgb(5, 227, 220);
    text-align: center;
    font-size: 70px;
    background-image: url("./background2.jpg");
    background-size: cover;
    margin: 0%;
    margin-bottom: 20px;
  }
  table {
    text-align: center;
    display: block;
    margin: auto;
  }
  .parameter {
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
