% rebase('templates/base/base_create')

<body>
  <div class='main'>
    <div class='back_create'>

      <div class='main_create'>
        <div class='title'>
          <p class='title_text'>アカウント登録</p>
        </div>

        <div class='create'>

          <form action="/check" id='form_new' method="POST">
            <p id='error' class='error'>{{duplicate_error}}</p>

            <span class="input input--hoshi">
              <input name='name' class="input__field input__field--hoshi" type="text" id="name" />
              <label class="input__label input__label--hoshi input__label--hoshi-color-1" for="input-4">
                <span class="input__label-content input__label-content--hoshi name">Name</span>
            </label>
            </span>

            <span class="input input--hoshi">
              <input name='email' class="input__field input__field--hoshi" type="text" id="email" />
              <label class="input__label input__label--hoshi input__label--hoshi-color-2" for="input-5">
                <span class="input__label-content input__label-content--hoshi email">Email</span>
            </label>
            </span>

            <span class="input input--hoshi">
              <input name='password' class="input__field input__field--hoshi" type="password" id="passwd" />
              <label class="input__label input__label--hoshi input__label--hoshi-color-3" for="input-6">
                <span class="input__label-content input__label-content--hoshi password">Password</span>
            </label>
            </span>

            <p class="submit"><input type="submit" id='submit' value="新規登録" /></p>

          </form>
          <p class='img_sen'><span class='sen'><img src="static/img/yazirushi.png" alt=""></span> または
            <span class='sen'><img src="static/img/yazirushi.png" alt=""></span>
          </p>


          <p class='sns'><a href="#" id='sns'>SNSアカウントで登録</a></p>
          <p class='login'>TOPに戻る<a href="/">TOP</a></p>
          <p class='login'>すでにアカウントをお持ちですか？<a href="/" id='login'>ログイン</a></p>
          <div class='sns_button'>
            <p class='sns_text'>SNSログイン</p>
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
          </div>
        </div>
      </div>
    </div>
  </div>
</body>
