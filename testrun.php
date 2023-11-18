<?php

$command = escapeshellcmd('python3 /Users/jameshayes/readCSVfromPHP.py');
$output = exec($command);
var_dump($output);

$image='<img src="http://3.135.162.69/monthlyTemps_db.png"/>';
$image1 = '<img src="http://3.135.162.69/monthlyRain_db.png"/>';
echo $image;
echo $image1;

?>