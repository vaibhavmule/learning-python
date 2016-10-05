import os
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

	def setUp(self):
		self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
		flaskr.app.config['TESTING'] = True
		self.app = flaskr.app.test_client()
		flaskr.init_db()

	def tearDown(self):
		os.close(self.db_fd)
		os.unlink(flaskr.app.config['DATABASE'])
	def test_empy_db(self):
		rv = self.app.get('/')
		assert 'No entries here so far' in rv.data
	def login(self, username, password):
		return self.app.post('/login', data=dict
			username=username,
			password=password
		), follow_redirects=True
	def logout(self):
		return self.app.get('/logout', follow_redirects=True)
 
if __name__ == '__main__':
	unittest.main()
