<?php
        // Get a connection for the database
        require_once('mysqli_connect.php');

        // Create a query for the database
        $query = "SELECT class_name, class_id, class_description FROM class";

        // Get a response from the database by sending the connection
        // and the query
        $response = @mysqli_query($dbc, $query);

        $courseList = array();
        // If the query executed properly proceed
        if($response){

                // mysqli_fetch_array will return a row of data from the query
                // until no further data is available
                while($row = mysqli_fetch_array($response)){
                        $tempCourse = array("courseName" => $row['class_name'], "courseDescription" => $row['class_description'], "id" => $row['class_id']);
                        array_push($courseList, $tempCourse);
                } 
        }

        // Close connection to the database
        mysqli_close($dbc);
        echo json_encode($courseList);
?>
