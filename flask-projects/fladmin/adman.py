from flask import Flask
from flask.ext.admin import Admin, BaseView, expose

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')

app = Flask(__name__)

admin = Admin(app)
admin.add_view(MyView(name='Hello'))
admin.add_view(MyView(name='Hello1', endpoint='test1', category='Test')
admin.add_view(MyView(name='Hello1', endpoint='test1', category='Test')

app.run()