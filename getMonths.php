
<?php 
include 'getYears.php'; 
echo $valueYear;

###############################
# Get the Month next          #
###############################

$valueMonth = $_POST['Month'];
  
$servername = "3.135.162.69";
$username = "chuckwx";
$password = "jfr716!!00";
$$dbname = "trweather";

echo "<html>";
echo "<body>";
echo "<form method='post'>";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT DISTINCT Month FROM trw WHERE Year = '$valueYear'";
$result = $conn->query($sql);

echo "<label>Month </label>";
echo "<select name='Month' onchange='this.form.submit()';>";
#echo "<option value=''>Select a Month</option>";
while ($row = $result->fetch_assoc()) {
  echo "<option value='" . $row['Month'] . "'>" . $row['Month'] . "</option>";
}

echo "</select>";
echo "</form>";

$conn->close();
