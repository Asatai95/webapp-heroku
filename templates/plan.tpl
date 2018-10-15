% rebase('templates/base')

<main>
    <div class="goods">
        % for plan in plans:
        <div class="card">
            <div class="card-image waves-effect waves-block waves-light">
                <img class="activator" src="{{ url('static_file', filepath='img/office.jpg') }}">
            </div>
            <div class="card-content">
                <span class="card-title activator grey-text text-darken-4">{{plan.name}}</span>
                <p>￥{{plan.amount}}</p>
                <!-- Modal Trigger -->
                <a class="waves-effect waves-light btn modal-trigger" href="/plans/{{plan.namespace}}">詳細を見る</a>
            </div>
            <div class="card-reveal">
                <span class="card-title grey-text text-darken-4">{{plan.name}}<i class="material-icons right">close</i></span>
                <p>{{plan.detail}}</p>
            </div>
        </div>
        % end
    </div>
</main>
