<!DOCTYPE html>

<html lang="ja">

<head>
  <meta http-equiv="Content-Type" content="text/plain" ; charset="UTF-8" ; Content-Transfer-Encoding="base64" />
  <meta charset="utf-8">
  <meta name='keywords' content=''>
  <meta name='description' content="">
  <meta name='viewport' content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" media="screen" href="static/css/pay.css">

  <title>TUBUYAKI</title>

</head>

<body>
  <div class='main'>
    <div class='header'>
      <div class='img'>
        <a href="/"><img src="static/img/nin_img.png" alt="">
      </div>
      <ul id='header' class='header_main'></a>
        <li class='text'>
          <a href="/">TOP</a>
        </li>
        <li class='text'>
          <a href="/info">TUBUYAKI</a>
        </li>
        </ul>
      </div>
      <div class='content'>
        <form action="/pay" method="post">
          <div class='title'>
            <p class='title-text'>確認画面</p>
          </div>
          <div class='pay_text'>
            <p class='text'>
              TUBUYAKIをご利用するためには500円、お支払いいただく必要があります。</br>
              下記のボタンよりお支払いしてください。
            </p>
          </div>
          <article>
            <label>Amount: ¥500</label>
          </article>
          <script src="https://checkout.stripe.com/v2/checkout.js" class="stripe-button" data-key="{{ publishable_key }}" data-locale="auto" data-amount="100" data-name="TUBUYAKI" data-description="アプリ購入" data-currency="jpy" data-image="static/img/ninwanko.png" data-locale="ja"></script>
        </form>
        <div class='back'>
          <p class='back_button'>既にお支払い済みですか？<a href="/check_account">クリック</a></p>
        </div>
        <div class='back top'>
          <p class='back_button'><a href="/">TOPに戻る</a></p>
        </div>
      </div>
    </div>
</body>


</html>
