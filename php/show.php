<?php include 'database.php' ;?>
<?php 
  $topic = $_GET['topic'];
  $query1 ="SELECT count(*) FROM Tweets WHERE topic = '$topic' AND sentiment > 0" ;
  $messages1 = mysqli_query($con, $query1);
  $query2 ="SELECT count(*) FROM Tweets WHERE topic = '$topic' AND sentiment = 0" ;
  $messages2 = mysqli_query($con, $query2);
  $query3 ="SELECT count(*) FROM Tweets WHERE topic = '$topic' AND sentiment < 0" ; 																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																
  $messages3 = mysqli_query($con, $query3);
  $query4 ="select latitude from Locations,Tweets where Tweets.topic = '$topic' AND Locations.place = Tweets.place group by latitude";
  $messages4 = mysqli_query($con, $query4);
  $query5 ="SELECT longitude FROM Locations,Tweets WHERE Tweets.topic = '$topic' AND Locations.place = Tweets.place group by latitude" ;
  $messages5 = mysqli_query($con, $query5);

  $query6 ="SELECT count(*) FROM Tweets WHERE topic = '$topic' AND sentiment is not null and place is not null";
  $messages6 = mysqli_query($con, $query6);
  $query7 ="SELECT count(*) FROM Tweets";
  $messages7 = mysqli_query($con, $query7);

while($row1 = mysqli_fetch_array($messages4))
    {
        $latitude[] = $row1['latitude'];	
    }
while($row2 = mysqli_fetch_array($messages5))
    {
        $longitude[] = $row2['longitude'];
    }

   	  
?>																																																																																																																			<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8" />
        <title>project</title>
        <script src='Chart.js/Chart.js'></script>
	<script src="http://maps.googleapis.com/maps/api/js"></script>
</head>
<body>
<h1>Total Number of Different Sentiment</h1>
<canvas id="myChart" width="400" height="400"></canvas>
<h1>Ratio of Different Sentiment</h1>
<canvas id="myChart1" width="400" height="400"></canvas>
<h1>Ratio of Processed text</h1>
<canvas id="myChart2" width="400" height="400"></canvas>
<h1>Ping of The Location</h1>
<div id="map" style="width:800px;height:800px;"></div>
<?php $row1 = mysqli_fetch_assoc($messages1); ?>
<?php $row2 = mysqli_fetch_assoc($messages2); ?>
<?php $row3 = mysqli_fetch_assoc($messages3); ?>
<?php $row6 = mysqli_fetch_assoc($messages6); ?>
<?php $row7 = mysqli_fetch_assoc($messages7); ?>
<script>
var data1 = <?php echo json_encode($row1['count(*)']); ?>;
var data2 = <?php echo json_encode($row2['count(*)']); ?>;
var data3 = <?php echo json_encode($row3['count(*)']); ?>;
var data6 = <?php echo json_encode($row6['count(*)']); ?>;
var data7 = <?php echo json_encode($row7['count(*)']); ?>;
var i;
var latitude = new Array(<?php echo implode(',', $latitude); ?>);
var longitude = new Array(<?php echo implode(',',$longitude); ?>);

    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 5,
      center: new google.maps.LatLng(latitude[0],longitude[0]),
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    var infowindow = new google.maps.InfoWindow();

    var marker, i; 

    for (i = 0; i < latitude.length; i++) {  
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(latitude[i],longitude[i]),
        map: map
      });

      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent(latitude[i]);
          infowindow.open(map, marker);
        }
      })(marker, i));
    }

var data = {
    labels: ["positive", "neutral", "negative"],
    datasets: [
        {
            label: "My First dataset",
            fillColor: "rgba(220,220,220,0.5)",
            strokeColor: "rgba(220,220,220,0.8)",
            highlightFill: "rgba(220,220,220,0.7)",
            highlightStroke: "rgba(220,220,220,1)",
            data: [data1, data2, data3]
        }
    ]
}

var data0 = [
    {
        value: data1,
        color:"#F7464A",
        highlight: "#FF5A5E",
        label: "positive"
    },
    {
        value: data2,
        color: "#46BFBD",
        highlight: "#5AD3D1",
        label: "neutral"
    },
    {
        value: data3,
        color: "#FDB45C",
        highlight: "#FFC870",
        label: "negative"
    }
]

var data1 = [
    {
        value: data6,
        color:"#F7464A",
        highlight: "#FF5A5E",
        label: "positive"
    },
    {
        value: data7,
        color: "#46BFBD",
        highlight: "#5AD3D1",
        label: "neutral"
    }
]
var ctx = document.getElementById("myChart").getContext("2d");
var ctx2 = document.getElementById("myChart1").getContext("2d");
var ctx3 = document.getElementById("myChart2").getContext("2d");
new Chart(ctx).Bar(data);
new Chart(ctx2).Pie(data0);
new Chart(ctx3).Pie(data1);
</script>
</body>
</html>

