# 2-execute_a_comand.pp
# Kills a process

exec {'killnow':
    command     => '/usr/bin/pkill -f kilnow',
    path        => ['bin', '/usr/bin'],
    refreshonly => true,
}
