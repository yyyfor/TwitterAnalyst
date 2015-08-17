<?php
//connect to mysql

$con = mysqli_connect("127.0.0.1:3307","zw627","zw627123","zw627");

//test connection
if(mysqli_connect_errno()){
	echo 'failed connect to mysql: '.$mysqli_connect_error();
}
