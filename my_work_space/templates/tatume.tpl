% rebase('templates/base/base_top')

<body>
  <div class='main'>

    <div class='header'>
      <div class='img'>
        <a href="/"><img src="static/img/nin_img.png" alt=""></a>
      </div>
      <ul id='header' class='header_main'>
        <li class='text'>
          <a href="/info">TUBUYAKI</a>
        </li>
        % if current_user:
         <li class='login_sub'><a href="/logout">ログアウト</a></li>
        % else:
         <li class='login_sub'><a href="#">ログイン</a></li>
        %end
      </ul>
    </div>
    <div class='content'>
      <div class='content_sub'>
        <p class='name'>TUBUYAKI</p>
        <p class='main_text_sub'>世界中のユーザーとつぶやこう！！</p>
      </div>
    </div>
  </div>

  <div class='back'>
    <div class='main_text'>
      <div class='title'>
        <p class='title_text'>ログイン</p>
      </div>
      <div class='main_content'>
          <div class="container">
            <div class="container-button">
              <img src="static/img/facebook_icon.png" alt="">
              <a class="container center-align btn waves-effect #1565c0 blue darken-3" href="/facebook/login">Facebookでログインする</a>
            </div>
          </div>

        <div id="gSignInWrapper">
          <div id="customBtn" class="customGPlusSignIn">
            <span class="icon"></span>
            <span class="buttonText"><a href="/google/login">Googleでログイン</a></span>
          </div>
        </div>

        <div id="tSignInWrapper">
          <div id="twitter" class="customGPlusSignIn">
            <span class="icon twitter"></span>
            <span class="buttonText twitter"><a href="/twitter/login">Twitterでログイン</a></span>
          </div>
        </div>

        <p class='ma'><span class='sen'><img src="static/img/sen.jpeg" alt=""></span> または
          <span class='sen'><img src="static/img/sen.jpeg" alt=""></span>
        </p>
        <div class='login'>
          <form action="/" id='form' method="POST">
            <p class='error'></p>
            <p class='login_mail'><input type="text" name="email" id='text' maxlength="32" autocomplete="OFF" placeholder='メールアドレス' /></p>
            <p class='login_pass'><input type="password" name="password" id='passwd' maxlength="32" autocomplete="OFF" placeholder='パスワード' /></p>
            <p class="submit"><input type="submit" id='submit' value="ログイン" /></p>

          </form>
          <p class='forgot'>パスワード忘れた方は<a href="/remake_password">こちら</a></p>
          %if stripe_cookie is None:
              <p class='new'>アカウントをお持ちではないですか？<a href="/pay" id='new'>新規登録</a></p>
          %else:
              <p class='new'>アカウントをお持ちではないですか？<a href="/create" id='new'>新規登録</a></p>
          %end
        </div>
      </div>
    </div>
  </div>


  </div>

</body>
