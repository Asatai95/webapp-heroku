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

  <title>TATUME</title>

</head>

<body>
  <div class='back_create'>
    <div class='main_create'>
      <div class='title'>
        <p class='title_text'>アカウント登録</p>
      </div>

        <div class='login'>
          <form action="/" id='form_new' method="POST">
            <p class='error'></p>

            <p class='user_name'><input type="text" name="user_name" id='user_name' maxlength="32" autocomplete="OFF" placeholder='ユーザー名' /></p>
            <p class='login_mail'><input type="text" name="new_log_id" id='new_text' maxlength="32" autocomplete="OFF" placeholder='メールアドレス' /></p>

            <p class='login_pass'><input type="password" name="new_passwd" id='new_passwd' maxlength="32" autocomplete="OFF" placeholder='パスワード' /></p>
            <p class="submit"><input type="submit" id='new_submit' value="新規登録" /></p>

          </form>
          <p class='ma'><span class='sen'><img src="static/img/sen.jpeg" alt=""></span> または
            <span class='sen'><img src="static/img/sen.jpeg" alt=""></span>
          </p>


          <p class='forgot_create'><a href="#">SNSアカウントで登録</a></p>
          <p class='new_create'>すでにアカウントをお持ちですか？<a href="#">ログイン</a></p>
        </div>
      </div>
    </div>
  </div>
</body>

</html>
