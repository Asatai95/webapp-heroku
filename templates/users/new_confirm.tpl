% rebase('templates/base')

<div class="container center">
	<h3>会員登録（確認画面）</h3>
</div>
<div class="row">
    <div class="container">
    <table>
        <tbody>
            <tr>
            <td>Name</td>
            <td>{{user.name}}</td>
            </tr>
            <tr>
            <td>Age</td>
            <td>{{user.age}}</td>
            </tr>
            <tr>
            <td>Email</td>
            <td>{{user.email}}</td>
            </tr>
            <tr>
            <td>Password</td>
            <td>非表示</td>
            </tr>
        </tbody>
    </table>
    </div>
    <form class="col l10 offset-l1 s12" action="/users/sign_up" method="post">
		<div class="container">
            <ul class="container"></ul>
            <div class="input-field container">
                % if user.name is not None:
                <input name="name" id="name" type="hidden" class="validate" value="{{user.name}}">
                % end
            </div>
            <div class="input-field container">
                % if user.name is not None:
                <input name="age" id="age" type="hidden" class="validate" value="{{user.age}}">
                % end
            </div>
			<div class="input-field container">
				<input name="email" id="email" type="hidden" required class="validate" value="{{user.email}}">
			</div>
			<div class="input-field container">
				<input name="password1" id="password1" type="hidden" required class="validate" value="{{user.password}}">
			</div>
			<div class=" container center-align">
                <button class="container center-align btn waves-effect waves-light" type="submit" name="action">登録する</button>
			</div>
		</div>
    </form>
    <div class="col l10 offset-l1 s12">
        <div class="container">
            <div class=" container center-align"><br>
                <button class="container center-align btn waves-effect #80cbc4 teal lighten-3" onclick="goBack()" >戻る</button>
            </div>
        </div>
    </div>
</div>
