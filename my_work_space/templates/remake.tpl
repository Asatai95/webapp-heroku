<!DOCTYPE html>

<html lang="ja">

<head>
  <meta http-equiv="Content-Type" content="text/plain" ; charset="UTF-8" ; Content-Transfer-Encoding="base64" />
  <meta charset="utf-8">
  <meta name='keywords' content=''>
  <meta name='description' content="">
  <meta name='viewport' content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" media="screen" href="../../static/css/remake_passsword_mail.css">

  <script src="../../static/js/jquery-3.1.1.min.js"></script>
  <script type="text/javascript" src="../../static/js/remake.js"></script>
  <link rel="stylesheet" type="text/css" href="../../static/js/slick-1.8.1/slick/slick.css" />
  <link rel="stylesheet" type="text/css" href="../../static/js/slick-1.8.1/slick/slick-theme.css" />
  <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
  <script type="text/javascript" src="static/js/slick-1.8.1/slick/slick.min.js"></script> -->

  <link rel="stylesheet" type="text/css" href="../../TextInputEffects/fonts/font-awesome-4.2.0/css/font-awesome.min.css" />
  <link rel="stylesheet" type="text/css" href="../../TextInputEffects/css/normalize.css" />
  <link rel="stylesheet" href="../../TextInputEffects/css/demo.css">
  <link rel="stylesheet" href="../../TextInputEffects/css/set1.css">
  <!-- <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script> -->
  <script src="../../TextInputEffects/js/classie.js"></script>

  <title>TUBUYAKI</title>

</head>

<body>
  <div class='main'>
    <div class='main_create'>

      <div class='title'>
        <p class='title_text'>パスワード再設定</p>
      </div>
      <div class='create'>

        <form action="/remake/{{mail_id}}/{{mail}}" id='form_new' method="POST">
          <p id='error' class='error'>{{duplicate_error}}</p>

          <span class="input input--hoshi">
          <input name='password1' class="input__field input__field--hoshi" type="password" id="passwd1" />
          <label class="input__label input__label--hoshi input__label--hoshi-color-3" for="input-6">
            <span class="input__label-content input__label-content--hoshi password 1">パスワード</span>
          </label>
          </span>

          <span class="input input--hoshi">
          <input name='password2' class="input__field input__field--hoshi" type="password" id="passwd2" />
          <label class="input__label input__label--hoshi input__label--hoshi-color-3" for="input-6">
            <span class="input__label-content input__label-content--hoshi password 2">パスワード確認用</span>
          </label>
          </span>

          <p class="submit"><input type="submit" id='submit' value="変更" /></p>
        </form>
      </div>
    </div>
  </div>
</body>

</html>
