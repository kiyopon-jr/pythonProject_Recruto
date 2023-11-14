import sys
path = '/home/dreznuk23/pythonProject_Recruto'
if path not in sys.path:
   sys.path.insert(0, path)

from app import app as application