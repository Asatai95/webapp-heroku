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

  <script async defer src="https://apis.google.com/js/api.js" onload="this.onload=function(){};handleClientLoad()" onreadystatechange="if (this.readyState === 'complete') this.onload()">
  </script>

  <script type="text/javascript">
    function signinCallback(authResult) {
      if (authResult['access_token']) {
        // 正常に承認されました
        // ユーザーが認証されたのでログイン ボタンを非表示にします。例:
        document.getElementById('signinButton').setAttribute('style', 'display: none');

        //追加部分--------------
        var info = document.getElementById('info');
        var textNode = document.createTextNode("Google+にログインできた。");
        info.appendChild(textNode);
        //---------追加部分終わり


      } else if (authResult['error']) {
        // エラーが発生しました。
        // 可能性のあるエラー コード:
        //   「access_denied」 - ユーザーがアプリへのアクセスを拒否しました
        //   「immediate_failed」 - ユーザーを自動的にログインできませんでした
        // console.log（「There was an error: 」 + authResult[「エラー」]）;
      }
    }
  </script>


</head>

<body>


  <div class='main_text'>
    <div class='title'>
      <p class='title_text'>ログイン</p>
    </div>
    <div class='main_content'>

      <div class="fb-login-button" data-max-rows="1" data-size="large" data-button-type='login_with' data-show-faces="false" data-auto-logout-link="false" data-use-continue-as="false" data-width="200" data-height='50'></div>


      <div id="signinButton">
        <div id='dv1' class="g-signin" data-callback="signinCallback" data-width="230" data-height='50' data-clientid="1079133430628-rhbrhpfsoc59u3hqiv86tj9qe08piu3j.apps.googleusercontent.com" data-cookiepolicy="single_host_origin" data-requestvisibleactions="http://schemas.google.com/AddActivity"
          data-scope="https://www.googleapis.com/auth/plus.login" style='width: 230px; heigth: 40px;'></div>
      </div>

      <div id="info"></div>

      <script type="text/javascript">
        (function() {
          var po = document.createElement('script');
          po.type = 'text/javascript';
          po.async = true;
          po.src = 'https://apis.google.com/js/client:plusone.js?onload=start';
          var s = document.getElementsByTagName('script')[0];
          s.parentNode.insertBefore(po, s);
        })();
      </script>

      <div id="my-signin2"></div>
      <script>
        function onSuccess(googleUser) {
          console.log('Logged in as: ' + googleUser.getBasicProfile().getName());
        }

        function onFailure(error) {
          console.log(error);
        }

        function renderButton() {
          gapi.signin2.render('my-signin2', {
            'scope': 'profile email',
            'width': 240,
            'height': 50,
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
