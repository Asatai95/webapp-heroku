% rebase('templates/base/base_mytweet_edit.tpl')

<body>
  <div class='main'>
    <div class='header'>
      <div class='img'>
        <img src="../../static/img/nin_img.png" alt="">
      </div>
      <ul id='header' class='header_main'>
        % if current_user is None:
        <li class='login_account'><a href="/">{{current_user}}</a></li>
        % else:
        <li class='login_account'><a href="/mypage">{{current_user.name}}</a></li>
        % end
        <li class='text'><a href="/info">TUBUYAKI</a></li>
        <li class='text'><a href="/tweet">つぶやく</a></li>
        <li class='text'><a href="/search">つぶやく検索</a></li>
        % if current_user:
        <li class='login_sub'><a href="/logout">ログアウト</a></li>
        % else:
        <li class='new'><a href="/create">登録</a></li>
        %end
      </ul>
    </div>
    <div class='tweet_box'>
      <div class='tweet_comment'>

        <form action="/mypage/edit/{{tweet_edit_id}}" method="POST">

          <textarea cols="30" rows="5" maxlength="150" name="tweet" wrap="hard">{{mytweet_edit}}</textarea>
          <div class='error'></div>
          <div class='submit'>
            <input type="submit" name="save" value="編集">
          </div>

        </form>

      </div>

    </div>
  </div>


</body>
