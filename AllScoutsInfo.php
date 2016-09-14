<!doctype html>
<html>
	<head>
		<title>All Scouts</title>
		<link rel="stylesheet" type="text/css" href="styles/style.css">
		<!-- Latest compiled and minified CSS -->
		<link rel="stylesheet"
			href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"
			integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7"
			crossorigin="anonymous">
		<!-- Optional theme -->
		<link rel="stylesheet"
			href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css"
			integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r"
			crossorigin="anonymous">
	</head>
	<body>
		<!--Begin Navbar-->
		<script src="//code.jquery.com/jquery.min.js"></script>
		<ol id="new-projects"></ol>
		<script src="scripts/copyNavBar.js"></script>
		<!--End Navbar-->

		<?php
			// Get a connection for the database
			require_once('mysqli_connect.php');
		
			// Create a query for the database
			$query = "SELECT first_name, last_name, scout_id, affiliation  FROM scout";
		
			// Get a response from the database by sending the connection
			// and the query
			$response = @mysqli_query($dbc, $query);
		
			// If the query executed properly proceed
			if($response){
				echo 
				'<div class="container table-responsive">
					<table class="table table-striped table-hover table-sm">
						<thead>
							<tr>
								<th align="left"><b>ID</b></th>
								<th align="left"><b>First Name</b></th>
								<th align="left"><b>Last Name</b></th>
								<th align="left"><b>Affiliation</b></th>
								<th align="left"></th>
							</tr>
						</thead>';
		
				// mysqli_fetch_array will return a row of data from the query
				// until no further data is available
				while($row = mysqli_fetch_array($response)){
					echo 
							'<tr >
								<td align="left">' .
										$row['scout_id'] . 
								'</td>
								<td align="left" height="50px" vertical-align="bottom">' . 
									$row['first_name'] . 
								'</td>
								<td align="left">' . 
									$row['last_name'] . 
								'</td>
								<td align="left">' .
										$row['affiliation'] . 
								'</td>
								<td align="left">
									<a class="btn btn-primary btn-sm" href="UserPage.html?scoutId=' .$row['scout_id'] .'" role="button">User Page</a> 
								</td>
							</tr>
						</a>';
				}
		
				echo 
					'</table>
				</dev>';
		
			} 
			else {
				echo "Couldn't issue database query<br />";
				echo mysqli_error($dbc);
			}
		
			// Close connection to the database
			mysqli_close($dbc);
		?>
	</body>
</html>
