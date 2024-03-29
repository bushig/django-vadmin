def register(*models, site=None):
    """
    Register the given model(s) classes and wrapped ModelAdmin class with
    admin site:

    @register(Author)
    class AuthorAdmin(django_vadmin.ModelAdmin):
        pass

    The `site` kwarg is an admin site to use instead of the default admin site.
    """
    from django_vadmin import ModelAdmin
    from django_vadmin.sites import site as default_site, AdminSite

    def _model_admin_wrapper(admin_class):
        if not models:
            raise ValueError('At least one model must be passed to register.')

        vadmin_site = site or default_site

        if not isinstance(vadmin_site, AdminSite):
            raise ValueError('site must subclass AdminSite')

        if not issubclass(admin_class, ModelAdmin):
            raise ValueError('Wrapped class must subclass ModelAdmin.')

        vadmin_site.register(models, admin_class=admin_class)

        return admin_class
    return _model_admin_wrapper
