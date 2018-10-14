<!DOCTYPE html>

<html lang="ja" itemscope itemtype="http://schema.org/Article">

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

  <title>TATUME</title>
</head>

<body>

  <span id="signinButton">
    <span
      class="g-signin"
      data-callback="signinCallback"
      data-clientid="1079133430628-rhbrhpfsoc59u3hqiv86tj9qe08piu3j.apps.googleusercontent.com"
      data-cookiepolicy="single_host_origin"
      data-requestvisibleactions="http://schemas.google.com/AddActivity"
      data-scope="https://www.googleapis.com/auth/plus.login">
    </span>
  </span>

  <div id="info"></div>



      <!-- この非同期 JavaScript を </body> タグの直前に置きます -->
      <script type="text/javascript">
        (function() {
         var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
         po.src = 'https://apis.google.com/js/client:plusone.js';
         var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
       })();
      </script>
</body>

</html>
