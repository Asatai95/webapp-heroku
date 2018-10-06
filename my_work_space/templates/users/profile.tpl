% rebase('templates/base/base_userpage')

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
    %for profiles in user_profile:
    <div class="profilecard">
      <div class="profile-header">
        <img src="../.{{profiles[1]}}" alt="">
        <p><span class="user-name">{{profiles[0]}}</span></p>
      </div>
      <div class="profile-content">
        <p>{{profiles[2]}}</p>
      </div>
      %if (profiles[3],) in follow_check:
        <a href="/follow/delete/{{profiles[3]}}" class="square_btn">フォローを外す</a>
      %else:
        <a href="/follow/{{profiles[3]}}" class="square_btn">フォローする</a>
      %end
    </div>
    %end

    <div class='main_content'>
      %for view in user_tweets :
      <div class="stream">
        <div class="content">
          <div class="stream-header">
            <a href="#"><img src="../.{{view[6]}}" alt=""></a>
            <p>
              <span class="tweet-time">{{view[0]}}</span>
              <span class="user-name">{{view[4]}}</span>
            </p>

          </div>
          <div class="inline">

          <div class="stream-content">

            <p name="comment">{{view[1]}}</p>
            <div class='inline_img'>
              <img src="../.{{view[5]}}" alt="">
            </div>
          </div>
          </div>
          <div class="stream-footer">
           <div class="favorite">
             %if (view[7],) in fab_check:
               <a href="/fab/delete/{{view[7]}}"><img src="../../static/img/oum.png" alt=""></a>
             %else:
               <a href="/fab/{{view[7]}}"><img src="../../static/img/fab_out.png" alt=""></a>
             %end
           </div>
         </div>
        </div>
      </div>
      %end
    </div>

  </div>
</body>
