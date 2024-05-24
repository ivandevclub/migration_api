# routers.py
class PostgresRouter:
    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'socios.Socio':
            return 'postgres'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.db_table == 'socios.Socio':
            return 'postgres'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.db_table == 'socios.Socio' or \
           obj2._meta.db_table == 'socios.Socio':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'sociopg':
            return db == 'postgres'
        return None
    
class MongoRouter:
    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'clientes':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.db_table == 'clientes':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.db_table == 'clientes' or \
           obj2._meta.db_table == 'clientes':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'socio':
            return db == 'default'
        return None
