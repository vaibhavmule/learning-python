# myapp/mongoadmin.py

# Import the MongoAdmin base class
from mongonaut.sites import MongoAdmin

# Import your custom models
from models import Post

# Instantiate the MongoAdmin class
class Post(MongoAdmin):
	search_fields = ('title',)
	list_fields = ('title', 'text',)
# Then attach the mongoadmin to your model
Post.mongoadmin = MongoAdmin()