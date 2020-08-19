function deleteFromGroup(anchor) {

  var xmlhttp = new XMLHttpRequest();
  article_id = anchor.getAttribute("data-article-id");
  group_name = anchor.getAttribute("data-group-name");

  // FIX: this is awful
  xmlhttp.open("DELETE", "/groups/" + group_name + "/articles/" + article_id);
  xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
  // Callbacks
  xmlhttp.onload = function(res){
    var response = JSON.parse(this.response);

    successCallback(response, anchor);
  };
  xmlhttp.onerror = function(res){
    var response = JSON.parse(this.response);

    errCallback(response, anchor);
  };

  var info = {
  }

  //xmlhttp.send(JSON.stringify(info));
  xmlhttp.send();
}

function successCallback(response, anchor) {
  var row = anchor.parentNode.parentNode;
  var tableBody = row.parentNode;

  row.remove();
  //tableBody.removeChild(row);
}

function errCallback(response, anchor) {
  alert("No ha sido posible efectuar la operación: "+ response.error);
}
