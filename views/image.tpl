<!DOCTYPE html>

<html lang="ja">

<head>
  <meta http-equiv="Content-Type" content="text/plain"; charset="UTF-8"; Content-Transfer-Encoding="base64" />
  <meta charset="utf-8">
  <meta name='keywords' content=''>
  <meta name='description' content="">
  <meta name='viewport' content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" media="screen" href="static/css/image.css">

  <!-- <script src="static/js/jquery-3.1.1.min.js"></script>
  <script type="text/javascript" src="static/js/tatume.js"></script>
  <link rel="stylesheet" type="text/css" href="static/js/slick-1.8.1/slick/slick.css"/>
  <link rel="stylesheet" type="text/css" href="static/js/slick-1.8.1/slick/slick-theme.css"/>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
  <script type="text/javascript" src="static/js/slick-1.8.1/slick/slick.min.js"></script> -->

  <title>TATUME</title>

</head>
<body>
 <div class='main'>
  <div class='header'>
   <div class='header_sub'>
    <div class='img'>
      <img src="static/img/tatume.png" alt="">
    </div>
    <ul id='header' class='header_main'>
      <a href="/info"><li class='text_now'>TATUME</li></a>
      <a href="/img"><li class='text'>イラスト</li></a>
      <a href="#"><li class='login'>ログイン</li></a>
    </ul>
   </div>
  </div>
  <div class='content'>
    <div class='content_sub'>
      <p class='content_text'>IMAGE</p>
    </div>
  </div>
  <div class='content_img'>

    <ul id='img_main' class='img_main'>
      %for img in images:
      <li class='img_main_content'><a href="#"><img src="{{img[img]}}" alt=""></a></li>
      <li class='img_main_content'><a href="#"><img src="{{img[0]}}" alt=""></a></li>
      %end
    </ul>

  </div>
 </div>
</body>
</html>
