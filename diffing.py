# For Windows => Based on window 7, not finished
class Windows:
	def __init__(self):
		print "This is Windows!!"
		self.os = "Windows"
		self.version = ""
		self.installDate = ""
		self.tasklist = []
		self.osInformation()
		self.get_tasklist()

	def osInformation(self):
		import _winreg as reg
		from datetime import datetime
		HKLM, subKey = reg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion"
		registry = reg.CreateKey(HKLM, subKey)
		self.version = reg.QueryValueEx( registry,"ProductName")[0]
		self.installDate = datetime.fromtimestamp(reg.QueryValueEx( registry,"InstallDate")[0])

	def get_tasklist(self):
		import subprocess
		output = subprocess.Popen('tasklist', stdout=subprocess.PIPE)
		tasklist = []
		for line in output.stdout:
			tasklist.append(line.split("  ")[0])
		self.tasklist = list(set(tasklist[5:]))

	def printValue(self):
		print self.version
		print self.installDate
		print self.tasklist


# For Ubuntu => working now
class Linux:
	def __init__(self):
		print "This is Linux!!"
		pass


# For mac => Maybe someday
class Darwin:
	def __init__(self):
		print "This is Mac!!"
		pass

import platform

# print platform.platform()
# print platform.system()
# print platform.release()
# print platform.version()

os = eval(platform.system())()
os.printValue()