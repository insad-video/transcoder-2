__version__ = '2.2.4'
__author__ = 'Marshall L Smith Jr <marshallsmithjr@gmail.com>'
__license__ = 'GPLv3'


#
# Global state indicators
#
from queue import Queue

verbose = False
keep_source = False
dry_run = False

status_queue = Queue()
