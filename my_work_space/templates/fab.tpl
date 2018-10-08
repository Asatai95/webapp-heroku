% rebase('templates/base/base_fab')

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
        <li class='new'><a href="/create">登録</a></li>
        %end
      </ul>
    </div>
    <div class="back">
      <a href="javascript:history.back();"><input type="submit" value="戻る" /></a>
    </div>
    <div class='main_content'>
      %for view in tweets :
      <div class="stream">
        <div class="content">
          <div class="stream-header">
            <a href="/users/profile/{{view[6]}}"><img src="../.{{view[8]}}" alt=""></a>
            <p>
              <span class="tweet-time">{{view[3]}}</span>
              <span class="user-name">{{view[7]}}</span>
            </p>

          </div>
          <div class="inline">

            <div class="stream-content">
              <p>{{view[5]}}</p>
              <div class='inline_img'>
                <img src="../.{{view[9]}}" alt="">
              </div>
              <div class="stream-footer">
                <div class="favorite" name='oki'>
                 %if (view[0],) in fab_check:
                  <a href="/fab/delete/{{view[0]}}"><img src="../../static/img/oum.png" alt=""></a>
                 %else:
                  <a href="/fab/delete/{{view[0]}}"><img src="../../static/img/logo-pic.png" alt=""></a>
                 %end
                 %if (view[6],) in follow_check:
                  <a href="/follow/delete/{{view[6]}}" class="square_btn">フォローを外す</a>
                 %else:
                  <a href="/follow/{{view[6]}}" class="square_btn">フォローする</a>
                 %end
                </div>

              </div>
            </div>
          </div>
        </div>
      </div>
      %end
    </div>
  </div>
</body>
