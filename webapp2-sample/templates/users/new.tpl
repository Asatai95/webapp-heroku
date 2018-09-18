% rebase('templates/base')

<div class="container center">
	<h3>会員登録</h3>
</div>
<div class="row">
	<form class="col l10 offset-l1 s12" method="POST">
		<div class="container">
			<div class="input-field container">
				<input id="email" name="email" type="text" required class="validate">
				<label for="email">Email</label>
			</div>
			<div class="input-field container">
				<input id="password1" name="password" type="password" required class="validate">
				<label for="password1">Password</label>
			</div>
			<div class="input-field container">
				<input id="password2" name='password' type="password" required class="validate">
				<label for="password2">Password check</label>
			</div>
			<div class="input-field container">
				<input id="name" name='name' type="text" class="validate">
				<label for="name">Name</label>
			</div>
			<div class="input-field container">
				<input id="age" name='age' type="text" class="validate">
				<label for="age">Age</label>
			</div>
			<div class=" container center-align">
				<button class="container center-align btn waves-effect waves-light" type="submit" name="action">登録する</button>
			</div>
		</div>
	</form>
</div>
