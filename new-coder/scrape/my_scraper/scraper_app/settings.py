BOT_NAME = 'livingsocial'

SPIDER_MODULE = ['scraper_app.spiders']

DATABASE = {'drivename': 'postgres',
			'host': 'localhost',
			'port': '5432',
			'username': 'postgres',
			'password': '123',
			'database': 'scrape'}

ITEM_PIPELINES = ['scraper_app.pipelines.LivingSocialPipeline']
