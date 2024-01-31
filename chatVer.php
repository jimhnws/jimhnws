<?php
session_start();
?>

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

// Function to sanitize input
function sanitizeInput($input)
{
    return htmlspecialchars(trim($input));
}

?>

<html>
    
<body>

<form method='post' action='chatVer.php'>

    <label>Year </label>
    <select name='Year' id='Year' onchange='this.form.submit();'>
        <option value=''>Select a Year</option>
        <?php
        $sql = "SELECT DISTINCT Year FROM trw";
        $result = $conn->query($sql);
        while ($row = $result->fetch_assoc()) {
            echo "<option value='" . sanitizeInput($row['Year']) . "'>" . sanitizeInput($row['Year']) . "</option>";
        }
        ?>
    </select>

</form>

<?php


// Check if the form is submitted
if (isset($_POST['Year'])) {
    $year = sanitizeInput($_POST['Year']);
    $_SESSION['Year'] = $_POST['Year'];
          
}
   

    // Get Month from Year using prepared statement
    $stmt = $conn->prepare("SELECT DISTINCT Month FROM trw WHERE Year = ?");
    $stmt->bind_param("s", $year);
    $stmt->execute();
    $result = $stmt->get_result();

    ?>

    <form method='post' action='chatVer.php'>
        <label>Month </label>
        <select name='Month' id='Month' onchange='this.form.submit();'>
            <option value=''>Select a Month</option>
            <?php
            while ($row = $result->fetch_assoc()) {
                echo "<option value='" . sanitizeInput($row['Month']) . "'>" . sanitizeInput($row['Month']) . "</option>";
            }
            ?>
        </select>
    </form>
        
    <?php
    $stmt->close();
    ?>

<?php
// Check if the form is submitted
if (isset($_POST['Month'])) {
    $month = sanitizeInput($_POST['Month']);
    echo $month;
}    

// Put the data together for one last sql statement

echo $month;
echo $_SESSION['Year'];
$blast = $_SESSION['Year'];

$sqlFinal = "SELECT * from trw WHERE Year = '$blast' AND Month = '$month'";
$result = $conn->query($sqlFinal);
$chuck = $result->fetch_all(MYSQLI_ASSOC);
$chuckwx = json_encode($chuck);
echo '<prev>'; print_r($chuckwx); echo '</prev>';


?>

</body>
</html>
