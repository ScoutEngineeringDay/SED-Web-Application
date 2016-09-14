<?php
        // Get a connection for the database
        require_once('mysqli_connect.php');

        // Create a query for the database
        $query = "SELECT first_name, last_name, scout_id, gender, age, street, city, state, zip, phone, email, emergency_firstname, emergency_lastname, emergency_phone, affiliation, scout_username, scout_password FROM scout";

        // Get a response from the database by sending the connection
        // and the query
        $response = @mysqli_query($dbc, $query);

        $scoutList = array();
        // If the query executed properly proceed
        if($response){

                // mysqli_fetch_array will return a row of data from the query
                // until no further data is available
                while($row = mysqli_fetch_array($response)){
                         $tempScout = array("first_name" => $row['first_name'], 
                                "last_name" => $row['last_name'], 
                                "scout_id" => $row['scout_id'], 
                                "gender" => $row['gender'], 
                                "age" => $row['age'], 
                                "street" => $row['street'], 
                                "city" => $row['city'], 
                                "state" => $row['state'], 
                                "zip" => $row['zip'], 
                                "phone" => $row['phone'], 
                                "email" => $row['email'], 
                                "emergency_firstname" => $row['emergency_firstname'], 
                                "emergency_lastname" => $row['emergency_lastname'], 
                                "emergency_phone" => $row['emergency_phone'], 
                                "affiliation" => $row['affiliation'], 
                                "scout_username" => $row['scout_username'], 
                                "scout_password" => $row['scout_password']);

                        array_push($scoutList, $tempScout);
                } 
        }

        // Close connection to the database
        mysqli_close($dbc);
        echo json_encode($scoutList);
?>
