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

<form action="daily_recent.php" method="post">
    
    <input type="text" name="Year"  placeholder="Year (yyyy)"/>
    <input type="text" name="Month" placeholder="Month (1-12)" />
    <input type="text" name="Date"   placeholder="Date (1-31)" />
    <input type="submit" name="submit" />
</form>

<?php

// Check if the form is submitted 

if($_POST['Month'] and $_POST['Year'] and $_POST['Date']){
    $year = $_POST['Year'];
    $month = $_POST['Month'];
    $date = $_POST['Date'];
    
}

$servername = "3.135.162.69";
$username = "chuckwx";
$password = "jfr716!!00";
$dbname = "davisf6";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * from davisUpdate WHERE Year = $year AND Month = $month AND Date = $date";
$result = $conn->query($sql);

$chuck = $result->fetch_all(MYSQLI_ASSOC);
$chuckwx = json_encode($chuck);
echo '<prev>'; print_r($chuckwx); echo '</prev>';

$file = fopen("/var/www/html/000/daily.txt", "w") or die("Unable to open file");

fwrite($file, $chuckwx);
fclose($file);

$conn->close();

echo "<table>
<tr>
<th>Year</th>
<th>Month</th>
<th>Date</th>
<th>High</th>
<th>Low</th>
<th>Average</th>
<th>HDD</th>
<th>CDD</th>
<th>Rainfall</th>
</tr>";

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
    echo "<tr>"; 
    echo "<td>" . $row["Year"] . "</td>";
    echo "<td>" . $row["Month"] . "</td>"; 
    echo "<td>" . $row["Date"]. "</td>";
    echo "<td>" . $row["High"]. "</td>"; 
    echo "<td>" . $row["Low"]. "</td>";
    echo "<td>" . $row["Average"] . "</td>";
    echo "<td>" . $row["HDD"]. "</td>"; 
    echo "<td>" . $row["CDD"]. "</td>";
    echo "<td>" . $row["Rainfall"] . "</td>";
    }
  } else {
    echo "0 results";
  }


$conn->close();
?>

</body>
</html>