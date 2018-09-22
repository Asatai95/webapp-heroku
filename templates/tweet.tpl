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
      <div class="stream">
        <div class="content">
          <div class="stream-header">
            <a href="#"><img src="" alt=""></a>
            <p>
              <span class="tweet-time"></span>
              <span class="user-name"></span>
            </p>

          </div>
          <div class="inline">
            <div class="stream-content">
              <p></p>
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
    </div>
    <footer>
      <div class='tweet_main'>
        <button id='tweet_button' type="button" name="button">Tweet</button>
      </div>
      <div class="tweet_content">
        <img src="static/img/ninwanko.png" alt="">
        <textarea name="tweet" id='tweet' class='tweet_box' rows="8" cols="80"></textarea>
      </div>
    </footer>
  </div>
</body>
