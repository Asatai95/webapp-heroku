<!DOCTYPE html>

<html lang="ja">

<head>
  <meta http-equiv="Content-Type" content="text/plain" ; charset="UTF-8" ; Content-Transfer-Encoding="base64" />
  <meta charset="utf-8">
  <meta name='keywords' content=''>
  <meta name='description' content="">
  <meta name='viewport' content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" media="screen" href="static/css/tatume.css">

  <script src="static/js/jquery-3.1.1.min.js"></script>
  <script type="text/javascript" src="static/js/tatume_top.js"></script>
  <link rel="stylesheet" type="text/css" href="static/js/slick-1.8.1/slick/slick.css" />
  <link rel="stylesheet" type="text/css" href="static/js/slick-1.8.1/slick/slick-theme.css" />
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
  <script type="text/javascript" src="static/js/slick-1.8.1/slick/slick.min.js"></script>

  <title>TATUME</title>

  <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet" type="text/css">
  <script src="https://apis.google.com/js/api:client.js"></script>
  <script>
    var googleUser = {};
    var startApp = function() {
      gapi.load('auth2', function() {

        auth2 = gapi.auth2.init({
          client_id: '1079133430628-rhbrhpfsoc59u3hqiv86tj9qe08piu3j.apps.googleusercontent.com',
          cookiepolicy: 'single_host_origin',

        });
        attachSignin(document.getElementById('customBtn'));
      });
    };
  </script>
  <style type="text/css">
    #customBtn {
      display: inline-block;
      background: rgba(255, 77, 77, .9);
      color: #444;
      width: 240px;
      height: 40px;
      text-align: left;
      border-radius: 5px;
      white-space: nowrap;
      margin: 0 0 20px 0;
      border-radius: 5px;
    }

    #customBtn:hover {
      cursor: pointer;
      opacity: .9;
      box-shadow: 0 0 5px rgba(255, 77, 77);
    }

    span.icon {
      background: url('static/img/icon.png') transparent 5px 50% no-repeat;
      background-repeat: no-repeat;
      background-size: 60%;
      display: inline-block;
      vertical-align: middle;
      width: 35px;
      height: 40px;
      margin-left: 5px;
    }

    span.buttonText {
      display: inline-block;
      vertical-align: middle;
      padding-left: 10px;
      padding-right: 25px;
      font-size: 17px;
      color: white;
      font-weight: 600;
      font-family: 'Roboto', sans-serif;
    }
  </style>


  <div id="fb-root"></div>
  <script>
    (function(d, s, id) {
      var js, fjs = d.getElementsByTagName(s)[0];
      if (d.getElementById(id)) return;
      js = d.createElement(s);
      js.id = id;
      js.src = 'https://connect.facebook.net/ja_JP/sdk.js#xfbml=1&version=v3.1&appId=704097009951110&autoLogAppEvents=1';
      fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));
  </script>


</head>

<body>
  <div class='main'>
    <div class='header'>
      <div class='img'>
        <img src="static/img/tatume.png" alt="">
      </div>
      <ul id='header' class='header_main'>
        <a href="/info">
          <li class='text'>TATUME</li>
        </a>
        <a href="/img">
          <li class='text'>イラスト</li>
        </a>
        <a href="#">
          <li class='login_sub'>ログイン</li>
        </a>
      </ul>
    </div>
    <div class='content'>
      <div class='content_sub'>
        <p class='name'>TATUME</p>
        <p class='main_text_sub'>大切な人への思いを代筆します。</p>


      </div>
    </div>
  </div>

  <div class='back'>
    <div class='main_text'>
      <div class='title'>
        <p class='title_text'>ログイン</p>
      </div>
      <div class='main_content'>

        <div class="fb-login-button" data-max-rows="1" data-size="large" data-button-type='login_with' data-show-faces="false" data-auto-logout-link="false" data-use-continue-as="false" data-width="200" data-height='50'></div>


        <div id="gSignInWrapper">
          <div id="customBtn" class="customGPlusSignIn">
            <span class="icon"></span>
            <span class="buttonText">Googleでログイン</span>
          </div>
        </div>
        <!-- <div id="name"></div> -->
        <script>
          startApp();
        </script>


        <p class='ma'><span class='sen'><img src="static/img/sen.jpeg" alt=""></span> または
          <span class='sen'><img src="static/img/sen.jpeg" alt=""></span>
        </p>
        <div class='login'>
          <form action="/" id='form' method="POST">
            <p class='error'></p>
            <p class='login_mail'><input type="text" name="log_id" id='text' maxlength="32" autocomplete="OFF" placeholder='メールアドレス' /></p>

            <p class='login_pass'><input type="password" name="passwd" id='passwd' maxlength="32" autocomplete="OFF" placeholder='パスワード' /></p>
            <p class="submit"><input type="submit" id='submit' value="ログイン" /></p>

          </form>


          <p class='forgot'>パスワード忘れた方は<a href="#">こちら</a></p>
          <p class='new'>アカウントをお持ちではないですか？<a href="#" id='new'>新規登録</a></p>
        </div>
      </div>
    </div>
  </div>

  <div class='back_create'>
    <div class='main_create'>
      <div class='title'>
        <p class='title_text'>アカウント登録</p>
      </div>

        <div class='login_create'>
          <form action="/" id='form_new' method="POST">
            <p class='error'></p>

            <p class='user_name'><input type="text" name="user_name" id='user_name' maxlength="32" autocomplete="OFF" placeholder='ユーザー名' /></p>
            <p class='login_mail'><input type="text" name="log_id_new" id='text_new' maxlength="32" autocomplete="OFF" placeholder='メールアドレス' /></p>

            <p class='login_pass'><input type="password" name="passwd_new" id='passwd_new' maxlength="32" autocomplete="OFF" placeholder='パスワード' /></p>
            <p class="submit"><input type="submit" id='submit_new' value="新規登録" /></p>

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
