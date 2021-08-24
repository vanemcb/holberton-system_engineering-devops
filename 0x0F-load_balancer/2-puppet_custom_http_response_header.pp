# Manifest to configure a web server

exec { 'update':
  command  => 'apt-get -y update'
  provider => shell
}
exec { 'upgrade':
  command  => 'apt-get -y upgrade'
  provider => shell
}
package {'nginx':
  ensure  => installed
  require => [exec['update'], exec['upgrade']]
}
file_line {'redirect':
  ensure  => 'present'
  path    => '/etc/nginx/sites-available/default'
  after   => 'server_name _;'
  line    => '\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'
  require => package['nginx']
}
file_line {'header':
  ensure  => 'present'
  path    => '/etc/nginx/sites-available/default'
  after   => 'server_name _;'
  line    => '\tadd_header X-Served-By $hostname;'
  require => package['nginx']
}
file {'/var/www/html/index.html':
  content => 'Holberton School'
  require => package['nginx']
}
service {'nginx':
  ensure  => running
  require => package['nginx']
}
