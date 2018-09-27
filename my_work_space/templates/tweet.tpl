% rebase('templates/base/base_tweet')

<body>
  <div class='main'>
    <div class='header'>
      <div class='img'>
        <img src="static/img/tatume.png" alt="">
      </div>
      <ul id='header' class='header_main'>
        % if current_user is None:
        <li class='login_account'><a href="#">{{current_user}}</a></li>
        % else:
        <li class='login_account'><a href="#">{{current_user.name}}</a></li>
        % end
        <li class='text'><a href="/info">TUBUYAKI</a></li>
        % if current_user:
        <li class='login_sub'><a href="/logout">ログアウト</a></li>
        % else:

        <li class='new'><a href="/create">登録</a></li>
        %end
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
              <span class="user-name">{{view[4]}}</span>
            </p>

          </div>
          <div class="inline">

            <div class="stream-content">
              <p>{{view[1]}}</p>
              <div class='inline_img'>
                <img src="{{view[5]}}" alt="">
              </div>
              <div class="stream-footer">
                <div class="favorite" name='oki'>
                  <a href="/fab/{{view[2]}}"><img src="static/img/logo-pic.png" alt=""></a>
                  %if check_db is True:
                   <a href="/follow/delete/{{view[3]}}" class="square_btn">フォロー外す</a>
                  %else:
                   <a href="/follow/{{view[3]}}" class="square_btn">フォロ-する</a>
                  %end
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
        <button id='tweet_button' type="button" name="button">Tweetしよう！</button>
      </div>
      <div class="tweet_content">
        <form action="/tweet" method="POST" enctype="multipart/form-data">
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
