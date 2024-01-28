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

#$chuck = $result->fetch_all(MYSQLI_ASSOC);
#$chuckwx = json_encode($chuck);
#echo '<prev>'; print_r($chuckwx); echo '</prev>';

echo "<html>";
echo "<body>";
echo "<label>Year </label>";
echo "<select name='Year' id='Year'>";

while ($row = $result->fetch_assoc()) {

        unset($year);
        $year = $row['Year']; 
        echo '<option value="'.$year.'"</option>';
                 
}

    echo "</select>";
    echo "</body>";
    echo "</html>";


?>

