
function AddUsers(base_url, destId){
	let users_url = base_url + "/users";
    let destElement = document.getElementById(destId);
    let linesToAdd = "";

  $.get(users_url,function(data){
      for(let i=0; i<data.length; i++){
		 
          $.get(users_url + "/" + data[i].user_id ,function(user){
              linesToAdd =
              `<li>
                    <h2>${i+1}</h2>
                    <h3>${user.username}</h3>
                    <p></p>
                    <p>	ID: ${user.user_id}</p>
                    <p>	Gender: ${user.gender}</p>
                    <p>	Birthday: ${user.birthday}</p>
                    <button onclick="location.href='/users/${user.user_id}/snapshots'">Get Snapshots</button>
                </li>`;

               if(destElement == null)
               {
                    destElement.innerHTML = "";
               }
             destElement.innerHTML += linesToAdd;
			 	 
        });
      }
  });
}

