% rebase('templates/base')
<h2>登録完了しました</h2>
<ul>
    <li>名前:{{user.name}}</li>
    % if user.age is not None:
    <li>年齢:{{user.age}}</li>
    % else:
    <li>年齢：</li>
    % end
    <li>メールアドレス:{{user.email}}</li>
</ul>