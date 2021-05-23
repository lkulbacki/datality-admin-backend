class OffersRouter:
    """
    A router to control all database operations on models in the
    offers applications.
    """
    route_app_labels = {'offers'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read offers models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'offers'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write offers models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'offers'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the offers apps only appear in the
        'offers' database.
        """
        if app_label in self.route_app_labels:
            return db == 'offers'
        return None


class ProductsRouter:
    """
    A router to control all database operations on models in the
    products applications.
    """
    route_app_labels = {'products'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read products models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'products'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write products models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'products'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the products apps only appear in the
        'products' database.
        """
        if app_label in self.route_app_labels:
            return db == 'products'
        return None
