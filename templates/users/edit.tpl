% rebase('templates/base')

<div class="container center">
	<h3>会員編集</h3>
</div>
<div class="row">
	<form class="col l10 offset-l1 s12" action="/mypage/edit" method="post">
		<div class="container">
			<div class="form-error">
				<ul id="error-messages" class="container">
					% if duplicate_error is not None:
					<li><label id="email-error" class="error" for="email">{{duplicate_error}}</label></li>
					% end
				</ul>
			</div>
			<div class="input-field container">
				% if current_user.name is not None:
				<input name="name" id="name" type="text" class="validate" value="{{current_user.name}}">
				% else:
				<input name="name" id="name" type="text" class="validate">
				% end
				<label for="name">Name</label>
			</div>
			<div class="input-field container">
				% if current_user.age is not None:
				<input name="age" id="age" type="text" class="validate" value="{{current_user.age}}">
				% else:
				<input name="age" id="age" type="text" class="validate">
				% end
				<label for="age">Age</label>
			</div>
			<div class="input-field container">
				% if current_user.email is not None:
				<input name="email" id="email" type="text" required class="validate" value="{{current_user.email}}">
				% else:
				<input name="email" id="email" type="text" required class="validate">
				% end
				<label for="email">Email (必須)</label>
			</div>
			<div class=" container center-align">
				<button class="container center-align btn waves-effect waves-light" type="submit" name="action">編集する</button>
			</div>
		</div>
	</form>
</div>
