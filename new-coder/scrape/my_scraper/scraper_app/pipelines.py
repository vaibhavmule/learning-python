from sqlalchemy.orm import sessionmaker
from models import Deals, db_connect, create_deals_table

class LivingSocialPipeline(object):
	"""LivingSocial Pipeline for storing scrape items in the database"""
	def __init__(self):
		"""Initialize database connecton and sessionmaker
		Create deals table"""

		engine = db_connect()
		create_deals_table(engine)
		self.Session = sessionmaker(bind=engine)

	def process_item(self, item, spider):
		"""Save deals in the database."""
		session = Self.Session()
		deal = Deals(**item)

		try:
			session.add(deal)
			session.commit()
		except:
			session.rollback()
			raise
		finally:
			session.close()
		return item
