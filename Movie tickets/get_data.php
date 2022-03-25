<?php
if(isset($_POST['booking_id']){
    $booking_id = $_POST['booking_id'];
    $seats = $_POST['seats'];

    $conx = mysqli_connect("localhost","root","","Check_in");

    $sql="INSERT INTO `details`(`booking_id`, `seats`) VALUES ('[$booking_id]','[$seats]');";
})