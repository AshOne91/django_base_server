from django.apps import AppConfig

from template.admin.admin_template_impl import AdminTemplateImpl
from template.account.account_template_impl import AccountTemplateImpl
from template.base.template_context import TemplateContext


class TestAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_app'

    def ready(self):
        from template.base.template_type import TemplateType
        from template.base.template.admin_template import AdminTemplate
        from template.base.template.account_template import AccountTemplate

        TemplateContext.add_template(TemplateType.ADMIN, AdminTemplateImpl())
        TemplateContext.add_template(TemplateType.ACCOUNT, AccountTemplateImpl())
