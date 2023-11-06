<!DOCTYPE html>
<html>
<head>
<style>
table {
  width: 100%;
  border-collapse: collapse;
}

table, td, th {
  border: 1px solid black;
  padding: 5px;
}

th {text-align: left;}
</style>
</head>
<body>

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

$reqMonth = 8;
$reqYear = 2015;

$sql = "SELECT * from trweather WHERE Month = $reqMonth AND Year = $reqYear";
$result = $conn->query($sql);

echo "<table>
<tr>
<th>index</th>
<th>Rain</th>
<th>HiTemp</th>
<th>LowTemp</th>
<th>Year</th>
<th>Month</th>
<th>Day</th>
</tr>";

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
      echo ": " . $row["index"]. " " . $row["Rain"]. " " . $row["HiTemp"]. " " . $row["LowTemp"]. " " . $row["Year"]. " " . $row["Month"]. " " . $row["Day"]. "<br>";
    }
  } else {
    echo "0 results";
  }

while($row =array($result)) {
    echo "<tr>";
    echo "<td>" . $row['index'] . "</td>";
    echo "<td>" . $row['Rain'] . "</td>";
    echo "<td>" . $row['HiTemp'] . "</td>";
    echo "<td>" . $row['LowTemp'] . "</td>";
    echo "<td>" . $row['Year'] . "</td>";
    echo "<td>" . $row['Month'] . "</td>";
    echo "<td>" . $row['Day'] . "</td>";
    echo "</tr>";
  }
  echo "</table>";
  $conn->close();

/* 

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
      echo ": " . $row["index"]. " " . $row["Rain"]. " " . $row["HiTemp"]. " " . $row["LowTemp"]. " " . $row["Year"]. " " . $row["Month"]. " " . $row["Day"]. "<br>";
    }
  } else {
    echo "0 results";
  }
  $conn->close();
  ?>
  */