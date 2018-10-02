% rebase('templates/base')

<div class="container center">
	<h3>会員登録</h3>
</div>
<div class="row">
	<form class="col l10 offset-l1 s12" action="/users/sign_up_confirm" method="post">
		<div class="container">
			<div class="form-error">
				<ul id="error-messages" class="container">
					% if duplicate_error is not None:
					<li><label id="email-error" class="error" for="email">{{duplicate_error}}</label></li>
					% end
				</ul>
			</div>
			<div class="input-field container">
				% if user.name is not None:
				<input name="name" id="name" type="text" class="validate" value="{{user.name}}">
				% else:
				<input name="name" id="name" type="text" class="validate">
				% end
				<label for="name">Name</label>
			</div>
			<div class="input-field container">
				% if user.age is not None:
				<input name="age" id="age" type="text" class="validate" value="{{user.age}}">
				% else:
				<input name="age" id="age" type="text" class="validate">
				% end
				<label for="age">Age</label>
			</div>
			<div class="input-field container">
				% if user.email is not None:
				<input name="email" id="email" type="text" required class="validate" value="{{user.email}}">
				% else:
				<input name="email" id="email" type="text" required class="validate">
				% end
				<label for="email">Email (必須)</label>
			</div>
			<div class="input-field container">
				<input name="password1" id="password1" type="password" required class="validate">
				<label for="password1">Password (必須)</label>
			</div>
			<div class="input-field container">
				<input name="password2" id="password2" type="password" required class="validate">
				<label for="password2">Password check (必須)</label>
			</div>
			<div class=" container center-align">
				<button class="container center-align btn waves-effect waves-light" type="submit" name="action">登録する</button>
			</div>
		</div>
	</form>
	<div class="col l10 offset-l1 s12 facebook-login">
		<div class="container">
			<div class=" container center-align">
				<a class="container center-align btn waves-effect #1565c0 blue darken-3" href="/facebook/login">Facebookで登録する</a>
			</div>
		</div>
	</div>
</div>
