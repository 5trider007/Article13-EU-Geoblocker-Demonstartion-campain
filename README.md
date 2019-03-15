# Article 13 EU Geoblocker

The Article 13 EU Geoblocker is a small project to show how the internet could show if this article come through.
The intension behind this project is a demo over the internet.

#savetheinternet, #saveyourinternet, #wearenotbots


example request for test if it works
```text
http://localhost:8080/?ip=84.62.86.32 <--- europe addess
http://localhost:8080/?ip=111.111.111.111 <--- no europe addess
```

Requirements:
- Webserver with ssh access.
- Python version 2.7.x

Python libs:

pip install python-geoip
pip install python-geoip-geolite2


Installation:

Paste this in to your website as php-code.
You can paste it on all subpages if you want.
```php
<?php
$url = 'http://localhost:8080'; // the geoip server
$ip = $_SERVER['REMOTE_ADDR']; // clients ip address
if(!isset($_COOKIE['have_seen_blocker'])) //if client has not seen the blocker it will see it one times per day
{
	echo file_get_contents($url."?ip=". $ip.'&url=http://'. $_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI']);
	setcookie('have_seen_blocker', "1");
}
?>
```
