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
echo "<select name='Year' id='Year' onchange='submit()';>";
echo "<option value=''>Select a Year</option>";
while ($row = $result->fetch_assoc()) {
  echo "<option value='" . $row['Year'] . "'>" . $row['Year'] . "</option>";
}

echo "</select>";
echo "</form>";

$conn->close();

if($_POST['Year']){
    $year = $_POST['Year'];

    echo $year;
}
#
# Get Month from Year
#

$valueMonth = $_POST['Month'];

$servername = "3.135.162.69";
$username = "chuckwx";
$password = "jfr716!!00";
$dbname = "trweather";

echo "<html>";
echo "<body>";
echo "<form method='Post'>";

// Create connection
$con = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($con->connect_error) {
  die("Connection failed: " . $con->connect_error);
}

$sql = "SELECT DISTINCT Month FROM trw WHERE Year = '$valueYear'";
$result = $con->query($sql);

echo "<label>Month </label>";
echo "<select name='Month' id='Month' onchange='this.form.submit()';>";
echo "<option value=''>Select a Month</option>";
while ($row = $result->fetch_assoc()) {
    echo "<option value='" . $row['Month'] . "'>" . $row['Month'] . "</option>";
}

echo "</select>";
echo "</form>";

$con->close();

// Check if the form is submitted 
    
if($_POST['Month']){
    $month = $_POST['Month'];

    echo $month;
                
}   

echo "</body>";
echo "</html>";

?>

