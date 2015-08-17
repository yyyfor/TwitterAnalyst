<?php include 'database.php' ;?>
<?php 
    //create select query
	$query ="select * from Topics";
	$messages = mysqli_query($con, $query);
 ?>
<!DOCTYPE html>
<html>
    <head>
	  <meta charset="utf-8" />
	  <title>Project</title>
	  <link rel="stylesheet" href="css/style.css" type="text/css" />
    </head>
	  <body>
	       <div id ="container">
		<header>
		<h1> project </h1>
		</header>
		<div id="shouts">
		<ul>
			<?php while($row = mysqli_fetch_assoc($messages)) : ?>
			<?php $key = $row['topic']; ?>
			<li class="shout"><span><?php echo "<a href='show.php?topic=" . $row['topic'] . "'> $key </a>"; ?></li>
			<?php endwhile; ?>	
		</ul>	
	       </div>
	        <div id="input">
			<?php if(isset($_GET['error'])) : ?>
		<div class="error"><?php echo $_GET['error']; ?></div>
			<?php endif; ?>
		<form method="post" action="process.php">
		<input type="text" name="topic" placeholder="Enter a topic"/>
		<br />
		<input class="shout-btn" type="submit" name="submit" value="submit" />
					
	  </body>
</html>
