<!DOCTYPE html>

<head>
    <html lang="en">
    <link rel="stylesheet" href="stylesQuery.css">
    <link rel="stylesheet" href="normalize.css">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get High Temperature Info from the Database</title>
</head>

<body>
    
<div id="display1" style="position: absolute;top: 0;left: 5%;"></div>
<script>
  function load_anotherpage() {
    document.getElementById("display1").innerHTML =
      '<embed type="text/html" src="http://3.135.162.69/pivotLow.html" width=225% height="750">';
  }

  load_anotherpage();
</script>

</body>
</html>