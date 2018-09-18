% rebase('templates/base')

<div class="container center">
	<h3>会員登録</h3>
</div>
<div class="row">
	<form class="col l10 offset-l1 s12">
		<div class="container">
			<div class="input-field container">
				<input id="email" type="text" required class="validate">
				<label for="email">Email</label>
			</div>
			<div class="input-field container">
				<input id="password1" type="text" required class="validate">
				<label for="password1">Password</label>
			</div>
			<div class="input-field container">
				<input id="password2" type="text" required class="validate">
				<label for="password2">Password check</label>
			</div>
			<div class="input-field container">
				<input id="name" type="text" class="validate">
				<label for="name">Name</label>
			</div>
			<div class="input-field container">
				<input id="age" type="text" class="validate">
				<label for="age">Age</label>
			</div>
			<div class=" container center-align">
				<button class="container center-align btn waves-effect waves-light" type="submit" name="action">登録する</button>
			</div>
		</div>
	</form>
</div>