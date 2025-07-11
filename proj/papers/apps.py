from django.apps import AppConfig


class PapersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'papers'
    def ready(self):
        from Database.mongoDB import get_papers_collection
        papers_col = get_papers_collection()
        papers_col.create_index([
            ("title", 1),
            ("abstract", 1),
            ("keywords", 1)
        ])