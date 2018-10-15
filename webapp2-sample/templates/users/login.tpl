% rebase('templates/base')

<div class="container center">
	<h3>ログイン</h3>
</div>
<div class="row">
	<form class="col l10 offset-l1 s12" method="POST">
		<div class="container">
			<div class="input-field container">
				<input id="email" name="email" type="text" required class="validate">
				<label for="email">Email</label>
			</div>
			<div class="input-field container">
				<input id="password" name="password" type="password" required class="validate">
				<label for="password">Password</label>
			</div>
			<div class=" container center-align">
				<button class="container center-align btn waves-effect waves-light" type="submit" name="action">登録する</button>
			</div>
		</div>
	</form>
</div>
