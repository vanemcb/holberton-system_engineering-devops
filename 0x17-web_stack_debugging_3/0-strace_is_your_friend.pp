# manifest to fix server syscall
exec {'Fix file .php':
  command  => 'sudo sed -i "s/phpp/php/" /var/www/html/wp-settings.php;',
  provider => shell,
}
