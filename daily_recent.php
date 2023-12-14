<!DOCTYPE html>
<html lang="en">
    <link rel="stylesheet" href="valTest.css">
    <link rel="stylesheet" href="normalize.css">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>

<body>

    <p>Daily Almanac</p>
    <div class="testBox">

    <form action="daily_recent.php" method="post">
      <label>Please enter numbers as shown</label>
      <input type="text" name="Year"  placeholder="Year (yyyy)"/>
      <input type="text" name="Month" placeholder="Month (1-12)" />
      <input type="text" name="Date"   placeholder="Date (1-31)" />
      <input type="submit" name="submit" />
    </form>
    </div>

<?php

// Check if the form is submitted 

if($_POST['Month'] and $_POST['Year'] and $_POST['Date']){
    $year = $_POST['Year'];
    $month = $_POST['Month'];
    $day = $_POST['Date'];
        
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

$sql = "SELECT * from trw WHERE Year = $year AND Month = $month AND Day = $day";
$result = $conn->query($sql);

$chuck = $result->fetch_all(MYSQLI_ASSOC);
$chuckwx = json_encode($chuck);
//echo '<prev>'; print_r($chuckwx); echo '</prev>';

$file = fopen("/var/www/html/000/daily.txt", "w") or die("Unable to open file");

fwrite($file, $chuckwx);
fclose($file);

$conn->close();

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

$output = shell_exec('/var/www/html/000/dailyProcess.sh 2>&1');
//var_dump($output);
//header("Location: http://3.135.162.69/dailyTest.html");

?>

<div class="righter">
    <iframe src="http://3.135.162.69/dailyTest.html" name="targetframe" allowTransparency="true" scrolling="no" frameborder="0" width="1500" height="1500">
    </iframe>
</div>

</body>
</html>