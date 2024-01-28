<?php

$valueYear = $_POST['Year'];


$servername = "3.135.162.69";
$username = "chuckwx";
$password = "jfr716!!00";
$dbname = "trweather";

echo "<html>";
echo "<body>";
echo "<form method='post'>";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT DISTINCT Year FROM trw";
$result = $conn->query($sql);

echo "<label>Year </label>";
echo "<select name='Year' onchange='this.form.submit()';>";
#echo "<option value=''>Select a Year</option>";
while ($row = $result->fetch_assoc()) {
  echo "<option value='" . $row['Year'] . "'>" . $row['Year'] . "</option>";
}

echo "</select>";
echo "</form>";

echo $valueYear;

$conn->close();

?>