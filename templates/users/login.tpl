% rebase('templates/base')

<div class="container center">
	<h3>ログイン</h3>
</div>
<div class="row">
	<form class="col l10 offset-l1 s12" method="post">
		<div class="container">
			<div class="input-field container">
				<input name="email" id="email" type="text" required class="validate">
				<label for="email">Email</label>
			</div>
			<div class="input-field container">
				<input name="password" id="password" type="password" required class="validate">
				<label for="password">Password</label>
			</div>
			<div class=" container center-align">
				<button class="container center-align btn waves-effect waves-light" type="submit" name="action">ログインする</button>
			</div>
		</div>
	</form>
	<div class="col l10 offset-l1 s12 facebook-login">
		<div class="container">
			<div class=" container center-align">
				<a class="container center-align btn waves-effect #1565c0 blue darken-3" href="/facebook/login">Facebookでログインする</a>
			</div>
		</div>
	</div>
</div>
