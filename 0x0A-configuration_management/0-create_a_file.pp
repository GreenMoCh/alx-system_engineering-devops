# 0-create_a_file.pp
# Creates a file in /tmp

file { '/tmp/school':
    ensure  => file,
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}
