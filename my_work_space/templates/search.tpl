% rebase('templates/base/base_search')


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
        <li class='text'><a href="/fab">お気に入り</a></li>
        % if current_user:
        <li class='login_sub'><a href="/logout">ログアウト</a></li>
        % else:
        <li class='new'><a href="/create">登録</a></li>
        %end
      </ul>
    </div>
    <div class='content_search_box'>
      <form action="/search" name="search" method="POST">
        <dl class="search_box">
          <dt><input type="text" name="search"  placeholder="キーワード検索" /></dt>
          <dd><button><span></span></button></dd>
        </dl>
      </form>

    </div>

    <div class='erra'>{{test}}</div>

    <div class='main_content'>
      %for view in tweets :
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
              <p>{{view[1]}}</p>
              <div class='inline_img'>
                <img src="{{view[5]}}" alt="">
              </div>
              <div class="stream-footer">
                <div class="favorite" name='oki'>
                  %if (view[8],) in fab_check:
                   <a href="/fab/delete/{{view[8]}}"><img src="static/img/logo-pic.png" alt=""></a>
                  %else:
                   <a href="/fab/{{view[8]}}"><img src="static/img/oum.png" alt=""></a>
                  %end
                  %if (view[3],) in follow_check :
                   <a href="/follow/delete/{{view[3]}}" class="square_btn">フォロー外す</a>
                  %else:
                   <a href="/follow/{{view[3]}}" class="square_btn">フォローする</a>
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
