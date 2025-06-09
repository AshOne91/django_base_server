from django.apps import AppConfig


class TestAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_app'

    def ready(self):
        from template.base.template_type import TemplateType
        from template.base.template.admin_template import AdminTemplate
        from template.base.template.account_template import AccountTemplate

        TemplateContext = TemplateContext.get_instance()
