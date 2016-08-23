<html>
    <head>
        <title>Scout Registered</title>
    </head>
    <body>
        <?php

            if(isset($_POST['submit'])){
                
                $data_missing = array();
                
                if(empty($_POST['first_name'])){

                    // Adds name to array
                    $data_missing[] = 'First Name';

                } else {

                    // Trim white space from the name and store the name
                    $f_name = trim($_POST['first_name']);

                }

                if(empty($_POST['last_name'])){

                    // Adds name to array
                    $data_missing[] = 'Last Name';

                } else{

                    // Trim white space from the name and store the name
                    $l_name = trim($_POST['last_name']);

                }

                if(empty($data_missing)){
                    
                    require_once('../mysqli_connect.php');
                    
                    $query = "INSERT INTO scout (first_name, last_name, date_entered, scout_id) VALUES (?, ?, NOW(), NULL)";
                    
                    $stmt = mysqli_prepare($dbc, $query);
                    if (!$stmt) {
                        die('mysqli error: '.mysqli_error($dbc));
                    }

                    /*
                    i Integers
                    d Doubles
                    b Blobs
                    s Everything Else
                    */

                    mysqli_stmt_bind_param($stmt, "ss", $f_name, $l_name);
                    // if (!mysqli_stmt_bind_param($stmt, "sssi", $f_name, $l_name)) {
                    //     die('bind error: '.mysqli_stmt_error($stmt));
                    // }
                    
                    if (!mysqli_execute($stmt)) {
                        die('stmt error: '.mysqli_stmt_error($stmt));
                    }

                    $affected_rows = mysqli_stmt_affected_rows($stmt);
                    
                    if($affected_rows == 1){
                        echo 'Scout Entered';
                        mysqli_stmt_close($stmt);
                        mysqli_close($dbc);    
                    } 
                    else {
                        echo 'Error Occurred<br />';
                        echo mysqli_error();
                        mysqli_stmt_close($stmt);
                        mysqli_close($dbc);   
                    }    
                } 
                else {
                    echo 'You need to enter the following data<br />';
                    foreach($data_missing as $missing){
                        echo "$missing<br />";   
                    }   
                }   
            }
        ?>

        <p>
            <b>Thank you for registering!</b>
        </p>
        
        <button id="returnHome" class="float-left submit-button" >Return to event Home page</button>
        <script type="text/javascript">
            document.getElementById("returnHome").onclick = function () {
                location.href = "index.html";
            };
        </script>

    </body>
</html>
