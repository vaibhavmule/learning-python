from django.db import models

# Create your models here.
notify = False

class Post(BaseModel):
	title = CharField(max_length=60)
	body = TextField()
	created = DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created"]

	def __unicode__(self):
		return self.title

class Comment(BaseModel):
	author = CharField(max_length=60, blank=True)
	body = TextField()
	post = ForeignKey(Post, related_name="comments", blank=True)
	created = DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u"%s: %s" % (self.post, self.body[:60])

	def save(self, *args, **kwargs):
		""" Email when a comment is added"""
		if notify:
			tpl = "Comment was addded to '%s' by '%s': \n\n%s"
			message = tpl % (self.post, self.author, self.body)
			from_addr = "no-reply@mydomain.com"
			recipient_list = ["vaibhavmule135@gmail.com"]

			send_mail("New comment added", message, from_addr, recipient_list)

		super(Comment, self).save(*args, **kwargs)