var script = document.createElement('script');
script.src = '/static/js/jquery/3.4.1/jquery.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);


function getUsers(){
	var base_url = "http://localhost:5000";
	var users_url = base_url + "/users";

  $.get(users_url,function(data){
    var users = data;

    for(var i=0; i<users.length; i++){
      var user = users[i];
      var row = $('<tr></tr>');
      var temp_user = $('<td></td>', {'text':user.username});
      row.append(temp_user);
      $('#users').append(row);
    }
  });
}


function getSnapshots(user_id){
	var base_url = "http://localhost:5000";
	var user_url = base_url + "/users" + "/" +user_id + "/snapshots";

  $.get(user_url,function(data){
    var snapshots = data;

    for(var i=0; i<snapshots.length; i++){
      var snapshot = snapshots[i];
      var row = $('<tr></tr>');
      var temp_snapshot = $('<td></td>', {'text':snapshot.datetime});
      row.append(temp_snapshot);
      $('#snapshots').append(row);
    }
  });
}

function getSnapshots(user_id){
	var base_url = "http://localhost:5000";
	var user_url = base_url + "/users" + "/" +user_id + "/snapshots";

  $.get(user_url,function(data){
    var snapshots = data;

    for(var i=0; i<snapshots.length; i++){
      var snapshot = snapshots[i];
      var row = $('<tr></tr>');
      var temp_snapshot = $('<td></td>', {'text':snapshot.datetime});
      row.append(temp_snapshot);
      $('#snapshots').append(row);
    }
  });
}


function getResultFields(user_id, snapshot_id){
	var base_url = "http://localhost:5000";
	var result_fields_url = base_url + "/users" + "/" +user_id + "/snapshots" +"/" + snapshot_id;

  $.get(result_fields_url,function(data){
    var result_fields = data;
	var row = $('<tr></tr>');
	for(var i=0; i<result_fields.length; i++){
		row.append( $('<td></td>', {'text':result_fields[i]}));
	}

	$('#result_fields').append(row);

  });
}
