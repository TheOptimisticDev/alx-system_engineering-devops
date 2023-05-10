# Resolving Apache returning a 500 error.

exec { 'resolve error':
  provider => 'shell',
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
