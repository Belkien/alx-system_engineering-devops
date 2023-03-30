#Executes command basically
exec {'pkill lillmenow':
	path => '/usr/bin:/usr/sbin:bin'
}

