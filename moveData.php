<!DOCTYPE html>
<html>
<head>
<style>
table {
  width: 50%;
  border-collapse: collapse;
}

table, td, th {
  border: 2px solid black;
  padding: 5px;
  background-color: white;
  
}

th {text-align: left;}
</style>
</head>

<body>

<form action=" moveData.php" method="post">
    <input type="text" name="Month" placeholder="Month (1-12)" />
    <input type="text" name="Year"  placeholder="Year (yyyy)"/>
    <input type="submit" name="submit" />
</form>

<?php

// Check if the form is submitted 

if($_POST['Month'] and $_POST['Year']){
    $month = $_POST['Month'];
    $year = $_POST['Year'];

}

$servername = "3.135.162.69";
$username = "chuckwx";
$password = "jfr716!!00";
$dbname = "trweather";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * from trweather WHERE Month = $month AND Year = $year";
$result = $conn->query($sql);

$file = fopen("/var/www/html/000/monthly.csv", "w") or die("Unable to open file");

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        $rain = $row["Rain"] . ",";
        $hiTemp = $row["HiTemp"] . ","; 
        $lowTemp = $row["LowTemp"] . ",";
        $year1 = $row["Year"] . ","; 
        $month1 = $row["Month"]. ",";
        $day1 = $row["Day"] . "\r\n";
        
        fwrite($file, $rain);
        fwrite($file, $hiTemp);
        fwrite($file, $lowTemp);
        fwrite($file, $year1);
        fwrite($file, $month1);
        fwrite($file, $day1);
               
    }
  } else {
    echo "0 results";
  }

   fclose($file);

$conn->close();
?>

</body>
</html>


