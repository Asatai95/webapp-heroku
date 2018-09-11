<!DOCTYPE html>

<html lang="ja">

<head>
  <meta http-equiv="Content-Type" content="text/plain" ; charset="UTF-8" ; Content-Transfer-Encoding="base64" />
  <meta charset="utf-8">
  <meta name='keywords' content=''>
  <meta name='description' content="">
  <meta name='viewport' content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" media="screen" href="static/css/text.css">

  <script src="static/js/jquery-3.1.1.min.js"></script>
  <!-- <script type="text/javascript" src="static/js/tatume.js"></script> -->
  <link rel="stylesheet" type="text/css" href="static/js/slick-1.8.1/slick/slick.css" />
  <link rel="stylesheet" type="text/css" href="static/js/slick-1.8.1/slick/slick-theme.css" />
  <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
  <script type="text/javascript" src="static/js/slick-1.8.1/slick/slick.min.js"></script> -->

  <meta name="google-signin-client_id" content="1079133430628-rhbrhpfsoc59u3hqiv86tj9qe08piu3j.apps.googleusercontent.com">

  <title>TATUME</title>

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


  <div class='main_text'>
    <div class='title'>
      <p class='title_text'>ログイン</p>
    </div>
    <div class='main_content'>

      <div class="fb-login-button" data-max-rows="1" data-size="large" data-button-type='login_with' data-show-faces="false" data-auto-logout-link="false" data-use-continue-as="false" data-width="200" data-height='50'></div>


      <div id="my-signin2"></div>
      <script>
        function onSuccess(googleUser) {
          console.log('Googleにログイン : ' + googleUser.getBasicProfile().getName());
        }

        function onFailure(error) {
          console.log(error);
        }

        function renderButton() {
          gapi.signin2.render('my-signin2', {
            'scope': 'profile email',
            'content': 'test',
            'width': 240,
            'height': 40,
            'longtitle': true,
            'theme': 'dark',
            'onsuccess': onSuccess,
            'onfailure': onFailure
          });
        }
      </script>

      <script src="https://apis.google.com/js/platform.js?onload=renderButton" async defer></script>

      </div>
      <p class='ma'><span class='sen'><img src="static/img/sen.jpeg" alt=""></span> または
        <span class='sen'><img src="static/img/sen.jpeg" alt=""></span>
      </p>
      <div class='login'>
        <form action="/" method="GET">
          <p class='login_mail'><input type="text" name="log_id" maxlength="32" autocomplete="OFF" placeholder='メールアドレス' /></p>
          <p class='login_pass'><input type="password" name="passwd" maxlength="32" autocomplete="OFF" placeholder='パスワード' /></p>
          <p class="submit"><input type="submit" value="ログイン" /></p>
        </form>
      </div>
    </div>

</body>

</html>
