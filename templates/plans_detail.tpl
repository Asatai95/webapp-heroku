% rebase('templates/base')
<h2>{{plan.name}}</h2>
<div class="container" style="width:50%;">
    <div class="card">
        <div class="card-image waves-effect waves-block waves-light">
            <img class="activator" src="{{ url('static_file', filepath='img/office.jpg') }}">
        </div>
        <div class="card-content">
            <span class="card-title activator grey-text text-darken-4">{{plan.name}}</span>
            <p>￥{{plan.amount}}</p>
            <!-- Modal Trigger -->
            <a class="waves-effect waves-light btn modal-trigger" href="#modal1">
              % if current_user is None or current_user.plan_id is None:
                購入する
              %elif current_user.plan_id == plan.id:
                契約中
              % else:
                変更する
              % end
            </a>
            <!-- Modal Structure -->
            <div id="modal1" class="modal">
                <div class="modal-content">
                <h4>
                  % if current_user is None or current_user.plan_id is None:
                    購入しますか？
                  % else:
                    変更しますか？
                  % end
                </h4>
                </div>
                <div class="modal-footer">
                <form action="/plans/{{plan.namespace}}/charge" method="post">
                    <a href="#!" class="modal-close waves-effect waves-red btn-flat">キャンセル</a>
                    <button class="waves-effect waves-light btn modal-trigger">
                      % if current_user is None or current_user.plan_id is None:
                        購入する
                      % else:
                        変更する
                      % end
                    </button>
                </form>
                </div>
            </div>
        </div>
        <div class="card-reveal">
            <span class="card-title grey-text text-darken-4">{{plan.name}}</span><i class="material-icons right">close</i></span>
            <p>{{plan.detail}}</p>
        </div>
    </div>
</div>
