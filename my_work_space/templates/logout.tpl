% rebase('templates/base/base_logout')

<body>
  <div class='main'>
    <div class='header'>
      <div class='img'>
        <img src="static/img/twitter.png" alt="">
      </div>
      <ul id='header' class='header_main'>
        % if current_user is None:
        <li class='login_account'><a href="#">{{current_user}}</a></li>
        % else:
        <li class='login_account'><a href="#">{{current_user.name}}</a></li>
        % end
        <li class='text'><a href="/info">TUBUYAKI</a></li>
        % if current_user:
        <li class='login_sub'><a href="#">ログアウト</a></li>
        % else:
        <li class='login_sub'><a href="#">ログイン</a></li>
        <li class='new'><a href="/create">登録</a></li>
        %end
      </ul>
    </div>
    <div class='main_content'>
      <div class='logout'>
        <p class='logout_text'>ログアウトしました</p>
        <p class='back'><a href="/">トップに戻る</a></p>
      </div>
    </div>
  </div>
</body>
