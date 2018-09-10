

class UserRegisterHandler(BaseJsonHandler):
    def post(self, *args, **kwargs):
        """
        ユーザの登録orログイン
        :return:
        """
        email = self.request.get('email')
        password = self.request.get('password')
        # TODO: 適宜リクエストの不正等のエラーは返すといいでしょう

        # authモジュールのUserモデルにはauth_idからUserをクエリするメソッドが用意されています。
        # Idやpasswordのエラーが返されるのでハンドルします
        try:
            user = User.get_by_auth_password(email, password)
            # ログイン成功時はセッションにユーザ情報を保存します
            self._set_session(user)
            return 'logged in'
        except auth.InvalidAuthIdError:
            # 今回はユーザ未登録の場合は新規作成をします

            # 同じくUserモデルにはuser作成のメソッドも用意されています。
            # 返り値がタプルなので注意
            result, info = User.create_user(auth_id=email)
            # 成功時のみinfoにuserエンティティが入ります
            user = info if result else None
            if not user:
                # ユーザ作成失敗時はエラーを返すといいでしょう
                return 'user cannot create'

            self._set_session(user)
            return 'user created'
        except auth.InvalidPasswordError:
            # password error
            return 'password invalid'

    def _set_session(self, user):
        user_dict = self.auth.store.user_to_dict(user)
        self.auth.set_session(user_dict)
