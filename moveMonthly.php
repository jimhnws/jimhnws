<!DOCTYPE html>
<html>
    <head>
    <meta charset="utf-8" />  
    <meta name="viewport" content="width=device-width, initial-scale=1" />  
    <link rel="stylesheet" href="stylesQuery.css">
    <link rel="stylesheet" href="normalize.css">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Get Monthly Data from the Database</title>
</head>

<body>
    <p>Monthly Almanac</p>

    <div class = "query_box">
    <form action=" moveMonthly.php" method="post">
     <input type="text" name="Month" placeholder="Month (1-12)" />
     <input type="text" name="Year"  placeholder="Year (yyyy)"/>
        <input type="submit" name="submit" />
    </form>
    </div>

<?php

if($_POST['Month'] and $_POST['Year']){
    $month = $_POST['Month'];
    $year = $_POST['Year'];
}

$servername = "3.135.162.69";
$username = "chuckwx";
$password = "jfr716!!00";
$dbname = "trweather";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * from trweather WHERE Month = $month AND Year = $year";
$result = $conn->query($sql);

$chuck = $result->fetch_all(MYSQLI_ASSOC);
$chuckwx = json_encode($chuck);
//echo '<prev>'; print_r($chuckwx); echo '</prev>';

$file = fopen("/var/www/html/000/monthly.txt", "w") or die("Unable to open file");

fwrite($file, $chuckwx);
fclose($file);

$conn->close();

$output = shell_exec('/var/www/html/000/testBlast.sh 2>&1');
//var_dump($output);

sleep(2);

?>

<div class="righter">
    <iframe src="http://3.135.162.69/monthlyTable.html" name="targetframe" allowTransparency="true" scrolling="no" frameborder="0" width="500" height="700">
    </iframe>
</div>

<div class="image1">
    <iframe src="http://3.135.162.69/allInOne.png" name="targetframe" allowTransparency="true" scrolling="no" frameborder="0" width="1000" height="800">
    </iframe>
</div>

<!--
<div class="image2">
    <iframe src="http://3.135.162.69/monthlyRain_db.png" name="targetframe" allowTransparency="true" scrolling="no" frameborder="0" width="1000" height="1000">
    </iframe>
</div>
    -->

</body>
</html>