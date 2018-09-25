% rebase('templates/base_tweet')

<body>
  <div class='main'>
    <div class='header'>
      <div class='img'>
        <img src="static/img/tatume.png" alt="">
      </div>
      <ul id='header' class='header_main'>
        <a href="/info">
          <li class='text'>TUBUYAKI</li>
        </a>
        <a href="#">
          <li class='login_sub'>ログイン</li>
        </a>
      </ul>
    </div>
    <div class='main_content'>
      %for view in tweets :
      <div class="stream">
        <div class="content">
          <div class="stream-header">
            <a href="#"><img src="" alt=""></a>
            <p>
              <span class="tweet-time">{{view[0]}}</span>
              <span class="user-name">{{view[1]}}</span>
            </p>

          </div>
          <div class="inline">
            <div class="stream-content">
              <p>{{view[2]}}</p>
              <div class="stream-footer">
                <div class="favorite" name='oki'>
                  <a href="#"><img src="static/img/logo-pic.png" alt=""></a>
                  <a href="#" class="square_btn">フォローする</a>
                </div>

              </div>
            </div>
          </div>
        </div>
      </div>
      %end
    </div>
    <footer>
      <div class='tweet_main'>
        <button id='tweet_button' type="button" name="button">Tweet</button>
      </div>
      <div class="tweet_content">
       <form action="/tweet" method="POST" enctype="multipart/form-data" >
        <div class='img_pro'>
         <img src="static/img/ninwanko.png" alt="">
        </div>
        <div class='box'>
         <textarea name="tweet" id='tweet' class='tweet_box' rows="8" cols="80"></textarea>
         <span class='img_view'></span>
       </div>
        <div class='tweet_button'>
          <div class='tweet_img'>
            <img src="static/img/upload.png" alt="" class='upload'>
            <label for="img" class='file'>

              UPLOAD
              <input type="file" name='img' id='img' class="img">
            </label>
          </div>
          <div class='button'>
            <button type="submit" name="button">
              <span class='submit_text'>Tweet</span>
              <input type="submit" id='submit' class='submit' value="">
            </button>
          </div>
        </div>

      </form>
     </div>
    </footer>
  </div>
</body>
