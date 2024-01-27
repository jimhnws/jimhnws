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

$result = $con->query("SELECT DISTINCT Month FROM `trw` WHERE Year = 2023");

echo "<html>";
echo "<body>";
echo "<select name='Month'>";

while ($row = $result->fetch_assoc()) {

        unset($month);
        $month = $row['Month']; 
        echo $month;
        echo '<option value="'.$month.'"</option>';
                 
}

    echo "</select>";
    echo "</body>";
    echo "</html>";
?>


