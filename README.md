# Article 13 EU Geoblocker
![alt text](http://cm1.narvii.com/7030/99355da804f85fb3a43e29e9ad348e67b997cbaa_00.jpg)

The Article 13 EU Geoblocker is a small project to show how the internet could be if this article come through.
The intension behind this project is a demo over the internet.

## How it works?

All users of the europe will see a blockpage for 10 seconds and then thy will redirected to the normal page what they want to visit. 

## #savetheinternet, #saveyourinternet, #wearenotbots


example request for test if it works
```text
http://localhost:8080/?ip=84.62.86.32 <--- europe addess
http://localhost:8080/?ip=111.111.111.111 <--- no europe addess
```

### Requirements:
- Webserver with ssh access.
- Python version 2.7.x

### Python libs:

pip install python-geoip
pip install python-geoip-geolite2


### Installation:

#### First: 
Move the complete directory where you want.

#### Second:
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
#### Third:
```sh
run ~$: python main.py
```
### Uninstallation:

kill the main.py
and delete the directory

Thats it
