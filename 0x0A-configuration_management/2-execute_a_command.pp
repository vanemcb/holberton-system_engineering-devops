# Manifest that kills a process named killmenow

exec {"kill a process":
command => 'pkill -9 killmenow',
provider => shell
}
