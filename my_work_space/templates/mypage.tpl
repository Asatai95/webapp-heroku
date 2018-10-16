% rebase('templates/base/base_mypage')

<body>
  <div class='main'>
    <div class='header'>
      <div class='img'>
        <a href="/tweet"><img src="../static/img/nin_img.png" alt=""></a>
      </div>
      <ul id='header' class='header_main'>
        % if current_user is None:
        <li class='login_account'><a href="/">{{current_user}}</a></li>
        % else:
        <li class='login_account'><a href="/mypage">{{current_user.name}}</a></li>
        % end
        <li class='text'><a href="/info">TUBUYAKI</a></li>
        <li class='text'><a href="/tweet">つぶやく</a></li>
        <li class='text'><a href="/search">つぶやき検索</a></li>
        % if current_user:
        <li class='login_sub'><a href="/logout">ログアウト</a></li>
        % else:
        <li class='new'><a href="/">ログイン</a></li>
        %end
      </ul>
    </div>
    <div class='check_main'>
      <div class='check_box'>
        <form action='/user/delete/{{user_account}}'>
          <p class='title'>アカウント削除確認</p>
          <ul class='error'>
            <li class='error_text'></li>
          </ul>
          <p class='email'>
            <label for="email">Email</label>
            <input type="text" name="email" id="email" maxlength="32" autocomplete="OFF" placeholder='Email' />
          </p>
          <p class='password'>
            <label for="password">Password</label>
            <input type="password" name="password" id="password" maxlength="32" autocomplete="OFF" placeholder='Password' />
          </p>
          <div class='check_button'>
            <p class='button_tag'>
              <button class='button' id='button' name='submit' type='submit'><a href="/user/delete/{{user_account}}">削除</a></button>
            </p>
          </div>
        </form>
      </div>
    </div>
    <!-- <div class='box'>
     <form action="/user/delete/{{user_account}}">
      <div class='check_comment'>
        <p class='comment'>本当にアカウントを削除しますか？</p>
        <p class='check_button_delete'>
          <button class='button' id='button' type='submit'><a href="/users/delete/{{user_account}}">削除</a></button>
        </p>
      </div>
    </form>
    </div> -->
    <div class='delete_error'>
      <p class='delete_error_text'>{{error}}</p>
    </div>
    %for profiles in profile:
    <div class="profilecard">
      <div class="profile-header">
        <img src="{{profiles[2]}}" alt="">
        <p><span class="user-name">{{profiles[0]}}</span><a href="/edit"><img class="edit" src="static/img/pencil.png" alt=""></a></p>
      </div>
      <div class="profile-content">
        <p>{{profiles[1]}}</p>
      </div>
      <a href="/follower" class="square_btn">フォロワー</a>
      <a href="#" class="square_btn button_delete">アカウント削除</a>
    </div>
    %end
    <div class='main_content'>
      %for view in my_tweets :
      <div class="stream">
        <div class="content">
          <div class="stream-header">
            <a href="#"><img src="{{view[6]}}" alt=""></a>
            <p>
              <span class="tweet-time">{{view[0]}}</span>
              <span class="user-name">{{view[4]}}</span>
            </p>

          </div>
          <div class="inline">

            <div class="stream-content">

              <p name="comment">{{view[1]}}</p>
              <div class='inline_img'>
                <img src="{{view[5]}}" alt="">
              </div>
            </div>
          </div>
          <div class='outline'>
            <div class='stream-delete'>
              <div class='delete'>
                <a href="/mypage/edit/{{view[2]}}" class="cp_btn">編集</a>
              </div>
            </div>
            <div class='stream-delete'>
              <div class='delete'>
                <a href="/mypage/delete/{{view[2]}}" class="cp_btn">削除</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      %end
    </div>

  </div>
</body>
