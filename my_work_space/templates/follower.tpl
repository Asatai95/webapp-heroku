% rebase('templates/base/base_follower.tpl')

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
        <li class='text'><a href="/fab">お気に入り</a></li>
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

    %for view in follower_view_table:
    <div class="profilecard">
      <div class="profile-header">
        <a href="/pro"><img src="{{view[3]}}" alt=""></a>

        <p><span class="user-name">{{view[1]}}</span></p>
      </div>

      <div class="profile-content">
        <p>{{view[2]}}</p>
      </div>
      <a href="/follower/delete/{{view[0]}}" class="square_btn">フォロー外す</a>
    </div>
    %end
  </div>
</body>
