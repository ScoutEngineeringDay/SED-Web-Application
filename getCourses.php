<?php

/* set out document type to text/javascript instead of text/html */
header("Content-type: text/javascript");

/* our multidimentional php array to pass back to javascript via ajax */
$arr = array(
        array(
                "courseName" => "Robotics",
                "courseDescription" => "Earning the Robotics merit badge requires a Scout to understand how robots move (actuators), sense the environment (sensors), and understand what to do (programming); he should demonstrate robot design in building a robot. You should help ensure that the Scout has sufficiently explored the field of robotics to understand what it is about, and to discover whether this may be a field of interest for him as a career.",
                "instructor" => "James Smith",
                "time" => "4:00-5:00am"
        ),
        array(
                "courseName" => "Space Exploration",
                "courseDescription" => "Space is mysterious. We explore space for many reasons, not least because we don't know what is out there, it is vast, and humans are full of curiosity. Each time we send explorers into space, we learn something we didn't know before. We discover a little more of what is there.",
                "instructor" => "Tammy Porter",
                "time" => "6:00-7:00pm"
        )
);

/* encode the array as json. this will output [{"first_name":"Darian","last_name":"Brown","age":"28","email":"darianbr@example.com"},{"first_name":"John","last_name":"Doe","age":"47","email":"john_doe@example.com"}] */
echo json_encode($arr);

?>