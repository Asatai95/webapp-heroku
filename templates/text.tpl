<!DOCTYPE html>

<html lang="ja">

<head>
  <meta http-equiv="Content-Type" content="text/plain"; charset="UTF-8"; Content-Transfer-Encoding="base64" />
  <meta charset="utf-8">
  <meta name='keywords' content=''>
  <meta name='description' content="">
  <meta name='viewport' content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" media="screen" href="static/css/text.css">

  <script src="static/js/jquery-3.1.1.min.js"></script>
  <!-- <script type="text/javascript" src="static/js/tatume.js"></script> -->
  <link rel="stylesheet" type="text/css" href="static/js/slick-1.8.1/slick/slick.css"/>
  <link rel="stylesheet" type="text/css" href="static/js/slick-1.8.1/slick/slick-theme.css"/>
  <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
  <script type="text/javascript" src="static/js/slick-1.8.1/slick/slick.min.js"></script> -->

  <title>TATUME</title>

  <div id="fb-root"></div>
  <script>(function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = 'https://connect.facebook.net/ja_JP/sdk.js#xfbml=1&version=v3.1&appId=704097009951110&autoLogAppEvents=1';
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));</script>

</head>
<body>
 <script>
  function statusChangeCallback(response) {
    console.log('statusChangeCallback');
    console.log(response);

    if (response.status === 'connected') {

      testAPI();
    } else if (response.status === 'not_authorized') {

      document.getElementById('status').innerHTML = 'Please log ' +
        'into this app.';
    } else {

      document.getElementById('status').innerHTML = 'Please log ' +
        'into Facebook.';
    }
  }

  function checkLoginState() {
    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });
  }

  // function Logout() {
  //   FB.Logout(function(response) {
  //
  //   });
  // }

  window.fbAsyncInit = function() {
    FB.init({
      appId: '704097009951110',
      status : true,
      cookie: true,
      xfbml: true,
      version: 'v3.1'
    });

    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });

    // FB.Logout(function(response) {
    //
    // });

    FB.AppEvents.logPageView();

  };

  (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {
      return;
    }
    js = d.createElement(s);
    js.id = id;
    js.src = "https://connect.facebook.net/en_JP/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));

  function testAPI() {
    console.log('Welcome!  Fetching your information.... ');
    FB.api('/me', function(response) {
      console.log('Successful login for: ' + response.name);
      document.getElementById('status').innerHTML =
        'Thanks for logging in, ' + response.name + '!';
    });
  }
 </script>

  <div class='main_text'>
    <div class='title'>
      <p class='title_text'>ログイン</p>
    </div>
    <div class='main_content'>


      <div class="fb-login-button" data-max-rows="1" data-size="large" data-button-type='login_with' data-show-faces="false" data-auto-logout-link="false" data-use-continue-as="false" data-width="200px" data-height='50px'></div>

    </div>
    <p class='ma'><span class='sen'><img src="static/img/sen.jpeg" alt=""></span>
      または
      <span class='sen'><img src="static/img/sen.jpeg" alt=""></span>
    </p>
    <div class='login'>
      <form action="/" method="GET">
        <p class='login_mail'><input type="text" name="log_id" maxlength="32" autocomplete="OFF" placeholder='メールアドレス'/></p>
        <p class='login_pass'><input type="password" name="passwd" maxlength="32" autocomplete="OFF" placeholder='パスワード' /></p>
        <p class="submit"><input type="submit" value="ログイン" /></p>
      </form>
    </div>
  </div>
</body>
</html>
