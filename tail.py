

GENERAL_QUERY_LOG_SQL = 'SELECT gl FROM MySqlGeneralLog gl WHERE eventTime > ? ORDER BY eventTime'

# get last_time from statefile, or start from 60 seconds ago?
# execute general/slow query to grab rows from mysql
# print to stdout for logging
# write last_time to statefile
# repeat

class State(object):

	def __init__(self, path='statefile'):
		self._path = path
		self._read(path)

	def _read(self, path):
		pass

	def write(self, state):
		pass

class Tailer(object):

	def __init__(self):
		pass

	def start(self):
		pass

	def is_ignored(query):
		return False


