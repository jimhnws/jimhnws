<?php

# Set up variables to query the mySQL databases

$server = '3.135.162.69';
$user = 'chuckwx';
$passwd = 'jfr716!!00';
$db_name = 'trweather';

$con = mysqli_connect($server, $user, $passwd, $db_name);

# Check connection
if ($con->connect_error) {
    die("Connection failed: " . $con->connect_error);
  }

# Get the years avaiable in the database

$result = $con->query("SELECT DISTINCT Year FROM `trw`");

echo "<html>";
echo "<body>";
echo "<select name='Year'>";

while ($row = $result->fetch_assoc()) {

        unset($year);
        $year = $row['Year']; 
        echo $year;
        echo '<option value="'.$year.'"</option>';
                 
}

    echo "</select>";
    echo "</body>";
    echo "</html>";
?>
