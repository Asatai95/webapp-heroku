<!DOCTYPE html>

<html lang="ja">

<head>
  <meta http-equiv="Content-Type" content="text/plain"; charset="UTF-8"; Content-Transfer-Encoding="base64" />
  <meta charset="utf-8">
  <meta name='keywords' content=''>
  <meta name='description' content="">
  <meta name='viewport' content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" media="screen" href="static/css/info.css">

  <script src="static/js/jquery-3.1.1.min.js"></script>
  <script type="text/javascript" src="static/js/tatume.js"></script>
  <link rel="stylesheet" type="text/css" href="static/js/slick-1.8.1/slick/slick.css"/>
  <link rel="stylesheet" type="text/css" href="static/js/slick-1.8.1/slick/slick-theme.css"/>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
  <script type="text/javascript" src="static/js/slick-1.8.1/slick/slick.min.js"></script>

  <title>TUBUYAKI</title>

</head>
<body>
  <div class='main'>
    <div class='header'>
     <div class='header_sub'>
      <div class='img'>
        <a href="/"><img src="static/img/nin_img.png" alt=""></a>
      </div>
      <ul id='header' class='header_main'>
        % if current_user is None:
        <li class='login_account'><a href="/">{{current_user}}</a></li>
        % else:
        <li class='login_account'><a href="/mypage">{{current_user.name}}</a></li>
        % end
        <li class='text'><a href="/info">TUBUYAKI</a></li>
        <li class='text'><a href="/tweet">つぶやく</a></li>
        % if current_user:
        <li class='login_sub'><a href="/logout">ログアウト</a></li>
        % else:
        <li class='new'><a href="/create">登録</a></li>
        %end
      </ul>
     </div>
    </div>
    <div class='content'>
      <div class='content_sub'>
        <p class='content_text'>TUBUYAKI</p>
      </div>
      <div class='content_tatume'>
        <p class='content_tatume_title'>つぶやきとは</p>
        <p class='content_tatume_img'><img src="static/img/text.png" alt=""></p>
        <p class='content_tatume_text'>
          つぶやきは、日本語の文字数制限を200文字に設定しており、</br>
          Twitterの140文字では自分の思いを表現できない方々のためのツールです。</br>
          早速、つぶやいてみよう！！</br>
        </p>
      </div>
      <div class='content_tatume_last'>
        <div class='content_last_text'>
          <p class='content_tatume_text'>経歴</p>
          <p class='content_tatume_text'>20XX/XX/XX サービス開始</p>
        </div>
      </div>
    </div>
    <div class='content_left'>
      <div class='content_title'>
        <p class='text_right'>つぶやき</p>
      </div>
      <div class='content_title_last'>
        <p class='text_right'>経歴</p>
      </div>
    </div>
  </div>
</body>
</html>
