<!DOCTYPE html>

<html lang="ja">

<head>
  <meta http-equiv="Content-Type" content="text/plain"; charset="UTF-8"; Content-Transfer-Encoding="base64" />
  <meta charset="utf-8">
  <meta name='keywords' content=''>
  <meta name='description' content="">
  <meta name='viewport' content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" media="screen" href="static/css/top.css">

  <!-- <link rel="stylesheet" media='screen and (min-width:0) and (max-width:375px)' href="static/css/top_sp.css">
  <link rel="stylesheet" media='screen and (min-width:376px) and (max-width:768px)' href="static/css/top_pad.css">
  <link rel="stylesheet" media='screen and (min-width:769px)' href="static/css/top.css"> -->

  <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
  <script type="text/javascript" src="static/js/test.js"></script>

  <title>Heroku</title>

</head>
<body>
 <div class='test'>
  <form action="/text_sub" method="POST" enctype="multipart/form-data">
    <div class="inline_img">
      <label id='image' for="userid" class='name'>image</label>
      <img src="static/img/ninwanko.png" alt="プロフィール画像">
      <input id="img_file" class="file" type="file" name="img_file" value="画像選択">
      <!-- <label for="file" class="view_box">
        +画像を選択
        <input id="file" class="file" type="file" name="file" value="" style="display:none;">
      </label> -->
    </div>
  </form>
</div>

</body>
</html>