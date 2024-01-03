<!DOCTYPE html>
<html>
    <head>
    <meta charset="utf-8" />  
    <meta name="viewport" content="width=device-width, initial-scale=1" />  
    <link rel="stylesheet" href="stylesQuery.css">
    <link rel="stylesheet" href="normalize.css">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Get Monthly Data from the Database</title>
</head>

<body>

    <p>Monthly Almanac</p>
    <div class = "query_boxMonth">
        <form action=" monthlyUpdate.php" method="post">
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
                <option value="1993">1993</option>
                <option value="1995">1995</option>
                <option value="1996">1996</option>
                <option value="1997">1997</option>
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
                <option value="2012">2012</option>
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
            </select><br>
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
            </select><br>
            <input type="submit" value="Submit">
        </form>    
    </div>    

<?php

if($_POST['Month'] and $_POST['Year']){
    $month = $_POST['Month'];
    $year = $_POST['Year'];
}           

$servername = "3.135.162.69";
$username = "chuckwx";
$password = "jfr716!!00";
$dbname = "trweather";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * from trw WHERE Month = $month AND Year = $year";
$result = $conn->query($sql);

$chuck = $result->fetch_all(MYSQLI_ASSOC);
$chuckwx = json_encode($chuck);
//echo '<prev>'; print_r($chuckwx); echo '</prev>';

$file = fopen("/var/www/html/000/monthly.txt", "w") or die("Unable to open file");

fwrite($file, $chuckwx);
fclose($file);

$conn->close();

$output = shell_exec('/var/www/html/000/testBlast.sh 2>&1');
//var_dump($output);

sleep(2);

?>

<div id="display" style="width: 80%;position: absolute;top: 0;left: 13%;"></div>
<script>
  function load_anotherpage() {
    document.getElementById("display").innerHTML =
      '<embed type="text/html" src="http://3.135.162.69/try1.html" width="500" height="700">';
  }  

  load_anotherpage();
</script>  

<div class="image1">
    <iframe src="http://3.135.162.69/allInOne.png" name="targetframe" allowTransparency="true" scrolling="no" frameborder="0" width="1000" height="800">
    </iframe>
</div>

<div id="display1" style="width: 70%;position: absolute;top: 79%;left: 12%;"></div>
<script>
  function load_anotherpage() {
    document.getElementById("display1").innerHTML =
      '<embed type="text/html" src="http://3.135.162.69/try2.html" width="80%" height="200">';
  }

  load_anotherpage();
</script>

</body>
</html>


       
