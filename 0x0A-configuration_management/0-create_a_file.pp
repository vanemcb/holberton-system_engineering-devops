# Create a file in /tmp:

file { '0-create_a_file.pp':
  path               => '/tmp/holberton',
  source_permissions => '/tmp/holberton',
  owner              => '/tmp/holberton',
  group              => '/tmp/holberton',
  content            => 'I love Puppet'
}
