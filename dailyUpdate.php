<!DOCTYPE html>

<head>
    <html lang="en">
    <link rel="stylesheet" href="valTest.css">
    <link rel="stylesheet" href="normalize.css">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Daily Data from the Database</title>
</head>

<body>

    <p>Daily Almanac</p>
    <div class="testBox">

        <form action="dailyUpdate.php" method="post">
            <label>Year</label>
            <select id="Year" name="Year">
                <option value="1978">1978</option>
                <option value="1979">1979</option>
                <option value="1980">1980</option>
                <option value="1981">1981</option>
                <option value="1982">1982</option>
                <option value="1983">1983</option>
                <option value="1984">1984</option>
                <option value="1985">1985</option>
                <option value="1986">1986</option>
                <option value="1989">1989</option>
                <option value="1990">1990</option>
                <option value="1991">1991</option>
                <option value="1992">1992</option>
                <option value="1995">1995</option>
                <option value="1998">1998</option>
                <option value="1999">1999</option>
                <option value="2000">2000</option>
                <option value="2001">2001</option>
                <option value="2002">2002</option>
                <option value="2003">2003</option>
                <option value="2004">2004</option>
                <option value="2005">2005</option>
                <option value="2006">2006</option>
                <option value="2007">2007</option>
                <option value="2008">2008</option>
                <option value="2009">2009</option>
                <option value="2010">2010</option>
                <option value="2011">2011</option>
                <option value="2013">2013</option>
                <option value="2014">2014</option>
                <option value="2015">2015</option>
                <option value="2016">2016</option>
                <option value="2017">2017</option>
                <option value="2018">2018</option>
                <option value="2019">2019</option>
                <option value="2020">2020</option>
                <option value="2021">2021</option>
                <option value="2022">2022</option>
                <option value="2023">2023</option>  
                <option value="2024">2024</option>
            </select>
            <label>Month</label>
            <select id="Month" name="Month">
                <option value="1">Jan</option>
                <option value="2">Feb</option>
                <option value="3">Mar</option>
                <option value="4">Apr</option>
                <option value="5">May</option>
                <option value="6">Jun</option>
                <option value="7">Jul</option>
                <option value="8">Aug</option>
                <option value="9">Sep</option>
                <option value="10">Oct</option>
                <option value="11">Nov</option>
                <option value="12">Dec</option>
            </select>
            <label>Day</label>
            <select id="Date" name="Date">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
                <option value="10">10</option>
                <option value="11">11</option>
                <option value="12">12</option>
                <option value="13">13</option>
                <option value="14">14</option>
                <option value="15">15</option>
                <option value="16">16</option>
                <option value="17">17</option>
                <option value="18">18</option>
                <option value="19">19</option>
                <option value="20">20</option>
                <option value="21">21</option>
                <option value="22">22</option>
                <option value="23">23</option>
                <option value="24">24</option>
                <option value="25">25</option>
                <option value="26">26</option>
                <option value="27">27</option>
                <option value="28">28</option>
                <option value="29">29</option>
                <option value="30">30</option>
                <option value="31">31</option>
            </select><br>
            <input type="submit" value="Submit">
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
    echo "";
  }

$conn->close();

$output = shell_exec('/var/www/html/000/dailyProcess.sh 2>&1');
//var_dump($output);
//header("Location: http://3.135.162.69/dailyTest.html");

?>

<div id="display1" style="position: absolute;top: 0;left: 15%;"></div>
<script>
  function load_anotherpage() {
    document.getElementById("display1").innerHTML =
      '<embed type="text/html" src="http://3.135.162.69/dailyTest.html" width="1500" height="1500">';
  }

  load_anotherpage();
</script>

</body>
</html>