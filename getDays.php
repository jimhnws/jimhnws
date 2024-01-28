<?php

##############################
# Get the Day                # 
##############################

$valueDay = $_POST['Day'];

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

$sql = "SELECT DISTINCT Day FROM `trw` WHERE Month = '$valueMonth' AND Year = '$valueYear'";
$result = $conn->query($sql);
#$chuck = $result->fetch_all(MYSQLI_ASSOC);
#$chuckwx = json_encode($chuck);
#echo '<prev>'; print_r($chuckwx); echo '</prev>';

echo "<label>Day </label>";
echo "<select name='Day' onchange='this.form.submit()';>";
echo "<option value=''>Select a Day</option>";
while ($row = $result->fetch_assoc()) {
  echo "<option value='" . $row['Day'] . "'>" . $row['Day'] . "</option>";
}

echo "</select>";
echo "</form>";

$conn->close();
?>