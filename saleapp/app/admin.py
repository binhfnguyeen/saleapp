from saleapp.app.models import Category, Product, User, UserRole
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from saleapp.app import app, db
from flask_login import current_user

admin = Admin(app=app, name="eCommerce Admin", template_mode='bootstrap4')

class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(UserRole.ADMIN)

class CategoryView(AdminView):
    column_list = ['name']


class ProductView(AdminView):
    column_list = ['id', 'name', 'price']
    can_export = True
    column_searchable_list = ['name']
    page_size = 5
    column_filters = ['id', 'name', 'price']
    column_editable_list = ['name']

admin.add_view(CategoryView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(AdminView(User, db.session))