<?php
  
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

$sql = "SELECT DISTINCT Year FROM trw";
$result = $conn->query($sql);

echo "<label>Year </label>";
echo "<select>";
while ($row = $result->fetch_assoc()) {
  echo $year;   
  echo "<option value='" . $row['Year'] . "'>" . $row['Year'] . "</option>";
}

echo "</select>";

$conn->close();


?>