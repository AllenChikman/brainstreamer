function UsernameText(destId, user_id){

	let base_url = "http://localhost:5000";
	let users_url = base_url + "/users/" + user_id;
    let destElement = document.getElementById(destId);
    let linesToAdd = "";

  $.get(users_url,function(user){
	linesToAdd = `(User: ${user.username})`;
	destElement.innerHTML += linesToAdd;

  });

}


function SnapshotTimestamp(destId, user_id, snapshot_id){

	let base_url = "http://localhost:5000";
	let snapshots_url = base_url + "/users/" + user_id + "/snapshots";
    let destElement = document.getElementById(destId);
    let linesToAdd = "";

  $.get(snapshots_url,function(snapshots){
      date_time = "";
      for(let i=0; i<snapshots.length; i++){
		 let snapshot = snapshots[i];
         if(snapshot.snapshot_id == snapshot_id){
            date_time = snapshot.datetime;
            break;
         }
      }
      linesToAdd = ` Snapshot - ${date_time} `;
      destElement.innerHTML = linesToAdd + destElement.innerHTML;
  });
}



function GetSnapshotResults(dataId, imgsId, user_id, snapshot_id){

    let destElement = document.getElementById(destId);
    let linesToAdd = "";

    // urls
    let base_url = "http://localhost:5000";
	let result_fields_url = base_url + "/users" + "/" +user_id + "/snapshots" +"/" + snapshot_id;
    let pose_url = result_fields_url + "/pose"
    let feelings_url = result_fields_url + "/feelings"
    let color_image_url = result_fields_url + "/color_image"
    let depth_image_url = result_fields_url + "/depth_image"

    // variable declarations
    let translation = "";
    let hunger = "";
    let rotation = "";
    let thirst = "";
    let happiness = "";
    let exhaustion = "";
    let color_img_path = "";
    let depth_img_path = "";

    rotation = $.get(pose_url,function(result_fields){

    rotation = `{
    ${result_fields.rotation.w.toFixed(4)},
    ${result_fields.rotation.x.toFixed(4)},
    ${result_fields.rotation.y.toFixed(4)},
    ${result_fields.rotation.z.toFixed(4)}
    }`;

    translation = `{
    ${result_fields.translation.x.toFixed(4)},
    ${result_fields.translation.y.toFixed(4)},
    ${result_fields.translation.z.toFixed(4)}
    }`;

  });


    $.get(feelings_url,function(result_fields){

    hunger = result_fields.hunger.toFixed(4);
    thirst = result_fields.thirst.toFixed(4);
    happiness = result_fields.happiness.toFixed(4);
    exhaustion = result_fields.exhaustion.toFixed(4);
  });

    $.get(color_image_url,function(result_fields){
        let idx = result_fields.data_path.indexOf("snapshots_imgs/");
        let img_path = result_fields.data_path.slice(idx);
        color_img_path = "/static/" + img_path;
    });

    $.get(depth_image_url,function(result_fields){
                let idx = result_fields.data_path.indexOf("snapshots_imgs/");
        let img_path = result_fields.data_path.slice(idx);
        depth_img_path = "/static/" + img_path;
    });

RenderSnapshotResults(
         dataId,
         rotation,
         translation,
         hunger,
         thirst,
         happiness,
         exhaustion);
}

RenderSnapshotImgs(imgsId, color_img_path, depth_img_path);

function RenderSnapshotResults(
         destId,
         rotation,
         translation,
         hunger,
         thirst,
         happiness,
         exhaustion)

{
    let destElement = document.getElementById(destId);
    let linesToAdd = `<tr>
        <th style="text-decoration: underline;">Position</th>
        <th style="text-decoration: underline;">Feelings</th>
    </tr>
    <tr>
        <td>Translation: ${translation}</td>
        <td>Hunger: ${hunger} </td>
    </tr>
    <tr>
        <td>Rotation: ${rotation}</td>
        <td>Thirst: ${thirst}</td>
    </tr>
    <tr>
        <td></td>
        <td>Happiness: ${happiness}</td>
    </tr>
    <tr>
        <td></td>
        <td>Exhaustion: ${exhaustion}</td>
    </tr> `;

    destElement.innerHTML += linesToAdd;
}

function RenderSnapshotImgs(destId, color_img_path, depth_img_path)
{
    let destElement = document.getElementById(destId);
    let linesToAdd = `
    <img class="w3-left" src=${color_img_path} style="width:49%; padding-top:1%;">
    <img class="w3-right" src=${depth_img_path} style="width:49%; padding-top:1%;">`;
destElement.innerHTML += linesToAdd;
}