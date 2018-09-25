%rebase('templtes/base')

%for user in users :
<ul>
  <li>id:{{user.id}}</li>
  <li>name: {{user.name}}</li>
  <li>age: {{user.age}}</li>
  <li>email: {{user.email}}</li>
</ul>

%end
