from template.base.template_context import TemplateContext
from template.base.template_type import TemplateType

class AccountProtocol:
    def __init__(self):
        account_template = TemplateContext.get_template(TemplateType.ACCOUNT)
        self.on_account_login_req_callback = account_template.on_account_login_req if hasattr(account_template, 'on_account_login_req') else None
        self.on_account_block_req_callback = account_template.on_account_block_req if hasattr(account_template, 'on_account_block_req') else None

    def account_login_req_controller(self, req_data):
        if self.on_account_login_req_callback:
            return self.on_account_login_req_callback(req_data)
        else:
            raise NotImplementedError("on_account_login_req not implemented in AccountTemplate")

    def account_block_req_controller(self, req_data):
        if self.on_account_block_req_callback:
            return self.on_account_block_req_callback(req_data)
        else:
            raise NotImplementedError("on_account_block_req not implemented in AccountTemplate")
