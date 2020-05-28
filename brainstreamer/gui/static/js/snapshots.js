
function AddUserCard(base_url, destId, user_id){
	let users_url = base_url + "/users/" + user_id;
    let destElement = document.getElementById(destId);
    let linesToAdd = "";

  $.get(users_url,function(user){
     
	linesToAdd =
		`<h1 style="color:rgb(255, 255, 179);"> ${user.username} </h1>
		<p> ID:  ${user.user_id}</p>
		<p> Gender: ${user.gender}</p>
		<p>${user.birthday}</p>`
	destElement.innerHTML += linesToAdd;
	
  });
}



function AddSnapshotList(base_url, destId, user_id){
	let snapshots_url = base_url + "/users/" + user_id + "/snapshots";
    let destElement = document.getElementById(destId);
    let linesToAdd = "";

  $.get(snapshots_url,function(snapshots){
      for(let i=0; i<snapshots.length; i++){
		 let snapshot = snapshots[i];
		 let result_url = "/users/" + user_id + "/snapshots/"+ snapshot.snapshot_id;
		  linesToAdd =
		`<li>
		<a href="${result_url}" style="text-decoration:none;">Snapshot${i+1} - <span style="font-weight: bold;">${snapshot.datetime}</span></a>
		</li>`;
		 destElement.innerHTML += linesToAdd;
			 	 

      }
  });
}


