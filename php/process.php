<?php 
include 'database.php';

//check if form submitted
if(isset($_POST['submit'])){
	$topic = mysqli_real_escape_string($con, $_POST['topic']);
	
	//set timezone
	date_default_timezone_set('America/New_York');
	$time = date('h:i:s a',time());
	
	//validate input
	if(!isset($topic) ||$topic =='' ){
		$error = "please fill in a topic";
		header("Location: index.php?error=".urldecode($error));
		exit();
	} else {
		$query = "INSERT INTO Topics (topic)
		VALUES ('$topic')";
		
		if(!mysqli_query($con, $query)){
			die('Error: '.mysqli_error($con));
		} else{
			header("Location:index.php");
			exit();
		}
		
	}
}
