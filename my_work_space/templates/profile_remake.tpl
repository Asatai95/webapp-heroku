% rebase('templates/base/base_profile_remake')

<div class='main'>

  <div class='header'>
    <div class='img'>
      <img src="../static/img/nin_img.png" alt="">
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
  <main id="profile_edit">
    <button type="button" name="button" class='button_back'>
      <a href="/mypage">マイページに戻る</a>
    </button>
    <div class="logo">
      <p>ユーザー登録</p>
    </div>
    <div class='text'>
      <div class='error'>
        <p>{{error}}</p>
      </div>
    </div>
    <form action="/edit" method="POST" enctype="multipart/form-data">
      %for view in profile_view :
      <div class="inline_img">

        <label id='image' for="userid" class='name'>image</label>
        <img src="{{view[3]}}" alt="プロフィール画像">
        <input id="img_file" class="file" type="file" name="img_file" value="画像選択" >
        <!-- <label for="file" class="view_box">
         +画像を選択
         <input id="file" class="file" type="file" name="file" value="" style="display:none;">
       </label> -->
      </div>
      <div id='userID' class="inline">
        <label for="userid" class='userID'>userID</label>
        <input type="text" name="userid" value="{{view[0]}}">
      </div>
      <div id="name" class="inline">
        <label for="name" class='name'>お名前</label>
        <input id='name_text' type="text" name="user_name" value="{{view[1]}}">
      </div>
      <div id="email">
        <label for="email" class='email'>E-mail</label>
        <input id='email_text' type="text" name="email" value="{{view[2]}}">
      </div>
      <div id='comment' class="inline">
        <label for="comment" class='comment'>ひと言</label>

        <textarea id='comment_text' type="text" name="user_intro" value="">{{view[4]}}</textarea>

      </div>
      %end
      <input id='submit' class="button" type="submit" value="登録" />
    </form>
  </main>
</div>
