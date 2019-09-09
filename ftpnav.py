#!/usr/bin/python
import ftplib

# login - server/username/password
session = ftplib.FTP('192.168.0.9','corey','password')

# change to directory
path = '/team-files/'
session.cwd(path)

# get size of file
size = session.size('team_5.ootp')
print(size)

# run script if not equal to size
if (size != 81570):
	# delete file
	session.delete('team_5.ootp')

	# upload file
	file = open("/home/robot/Desktop/team_xx.ootp", 'rb')
	session.storbinary('STOR team_xx.ootp', file)

	# rename file, does not generate alert
	session.rename('team_xx.ootp', 'team_5.ootp')

	# close
	file.close()
	session.quit()
else:
	session.quit()
