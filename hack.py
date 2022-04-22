import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("hack").lisensi()
else:
	       exit(f' Unknow device machine {arc}')
