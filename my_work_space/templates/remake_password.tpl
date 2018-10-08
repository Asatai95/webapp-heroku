% rebase('templates/base/base_remake_password')
<body>
  <div class='main'>
    <div class='back_create'>

      <div class='main_create'>
        <div class="back">
          <a href="javascript:history.back();"><input type="submit" value="戻る" /></a>
        </div>
        <div class='title'>
          <p class='title_text'>パスワード再設定</p>
        </div>

        <div class='create'>

          <form action="/remake_password" id='form_new' method="POST">
            <p id='error' class='error'>{{duplicate_error}}</p>

            <span class="input input--hoshi">
              <input name='email' class="input__field input__field--hoshi" type="text" id="email" />
              <label class="input__label input__label--hoshi input__label--hoshi-color-2" for="input-5">
                <span class="input__label-content input__label-content--hoshi email">Email</span>
              </label>
            </span>
            <p class="submit"><input type="submit" id='submit' value="メール送信" /></p>
          </form>
          <p class='img_sen'><span class='sen'><img src="static/img/yazirushi.png" alt=""></span> または
            <span class='sen'><img src="static/img/yazirushi.png" alt=""></span>
          </p>

          <p class='sns'><a href="/" id='forgot'>SNSアカウントでログイン</a></p>
        </div>
      </div>
    </div>
  </div>
</body>
