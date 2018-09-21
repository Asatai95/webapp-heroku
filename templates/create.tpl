<!DOCTYPE html>

<html lang="ja">

<head>
  <meta http-equiv="Content-Type" content="text/plain" ; charset="UTF-8" ; Content-Transfer-Encoding="base64" />
  <meta charset="utf-8">
  <meta name='keywords' content=''>
  <meta name='description' content="">
  <meta name='viewport' content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" media="screen" href="static/css/create.css">

  <script src="static/js/jquery-3.1.1.min.js"></script>
  <script type="text/javascript" src="static/js/create.js"></script>
  <link rel="stylesheet" type="text/css" href="static/js/slick-1.8.1/slick/slick.css" />
  <link rel="stylesheet" type="text/css" href="static/js/slick-1.8.1/slick/slick-theme.css" />
  <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
  <script type="text/javascript" src="static/js/slick-1.8.1/slick/slick.min.js"></script> -->

  <link rel="stylesheet" type="text/css" href="TextInputEffects/fonts/font-awesome-4.2.0/css/font-awesome.min.css" />
  <link rel="stylesheet" type="text/css" href="TextInputEffects/css/normalize.css" />
  <link rel="stylesheet" href="TextInputEffects/css/demo.css">
  <link rel="stylesheet" href="TextInputEffects/css/set1.css">
  <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
  <script src="TextInputEffects/js/classie.js"></script>

  <title>TATUME</title>

</head>

<body>
  <div class='main'>
    <div class='back_create'>

      <div class='main_create'>
        <div class='title'>
          <p class='title_text'>アカウント登録</p>
        </div>

        <div class='create'>

          <form action="/create" id='form_new' method="POST">
            <p id='error' class='error'></p>

            <span class="input input--hoshi">
              <input name='name' class="input__field input__field--hoshi" type="text" id="name" />
              <label class="input__label input__label--hoshi input__label--hoshi-color-1" for="input-4">
                <span class="input__label-content input__label-content--hoshi name">Name</span>
            </label>
            </span>

            <span class="input input--hoshi">
              <input name='email' class="input__field input__field--hoshi" type="text" id="email" />
              <label class="input__label input__label--hoshi input__label--hoshi-color-2" for="input-5">
                <span class="input__label-content input__label-content--hoshi email">Email</span>
              </label>
            </span>

            <span class="input input--hoshi">
              <input name='passwd' class="input__field input__field--hoshi" type="text" id="passwd" />
              <label class="input__label input__label--hoshi input__label--hoshi-color-3" for="input-6">
                <span class="input__label-content input__label-content--hoshi password">Password</span>
              </label>
            </span>

            <p class="submit"><input type="submit" id='submit' value="新規登録" /></p>

          </form>
          <p class='img_sen'><span class='sen'><img src="static/img/yazirushi.png" alt=""></span> または
            <span class='sen'><img src="static/img/yazirushi.png" alt=""></span>
          </p>


          <p class='sns'><a href="#" id='forgot'>SNSアカウントで登録</a></p>
          <p class='login'>すでにアカウントをお持ちですか？<a href="/" id='login'>ログイン</a></p>
        </div>
      </div>
    </div>
  </div>
</body>

</html>
