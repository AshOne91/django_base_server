from template.base.template.account_template import AccountTemplate

class AccountTemplateImpl(AccountTemplate):
    def on_account_login_req(self, request):
        # 실제 로그인 로직
        return {"result": "success", "message": "Login successful"}

    def on_account_block_req(self, request):
        return {"result": "success", "message": "Account blocked successfully"}