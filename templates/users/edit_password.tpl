% rebase('templates/base')

<div class="container center">
	<h3>会員パスワード編集</h3>
</div>
<div class="row">
	<form class="col l10 offset-l1 s12" action="/mypage/edit_password" method="post">
		<div class="container">
			<div class="input-field container">
				<input name="password1" id="password1" type="password" required class="validate">
				<label for="password1">Password (必須)</label>
			</div>
			<div class="input-field container">
				<input name="password2" id="password2" type="password" required class="validate">
				<label for="password2">Password check (必須)</label>
			</div>
			<div class=" container center-align">
				<button class="container center-align btn waves-effect waves-light" type="submit" name="action">編集する</button>
			</div>
		</div>
	</form>
</div>