<!DOCTYPE html>

<head>
    <html lang="en">
    <link rel="stylesheet" href="valTest.css">
    <link rel="stylesheet" href="normalize.css">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Data Between Two Dates from the Database</title>
</head>

<body>
    <div class="queryBox">

    <form action="betweenTwoDates.php" method="post">

        <label for="start">Start date:</label>
        <input type="date" id="start" name="start" value="1978-01-01" min="1978-01-01" max="2023-12-31" />

        <label for="end">End date:</label>
        <input type="date" id="end" name="end" value="1978-01-01" min="1978-01-01" max="2023-12-31" />

        <br>
        <input type="submit" value="Submit">
    </form>
</div>

</body>


<?php

// Check if the form is submitted 
    
if($_POST['start'] and $_POST['end']){
        $first = $_POST['start'];
        $last = $_POST['end'];                     
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

$sql = "SELECT * from trw WHERE timeGroup BETWEEN '$first' AND '$last'";
$result = $conn->query($sql);

$chuck = $result->fetch_all(MYSQLI_ASSOC);
$chuckwx = json_encode($chuck);

$file = fopen("/var/www/html/000/all.txt", "w") or die("Unable to open file");
echo $file;
fwrite($file, $chuckwx);
fclose($file);

$conn->close();

?>