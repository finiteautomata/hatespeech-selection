function deleteFromGroup(anchor) {

  var xmlhttp = new XMLHttpRequest();
  article_id = anchor.getAttribute("data-article-id");
  group_name = anchor.getAttribute("data-group-name");

  // FIX: this is awful
  xmlhttp.open("DELETE", "/groups/" + group_name + "/articles/" + article_id);
  xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
  // Callbacks
  xmlhttp.onload = function(){
    successCallback(anchor);
  };
  xmlhttp.onerror = function(){
    errCallback(this);
  };

  var info = {
  }

  //xmlhttp.send(JSON.stringify(info));
  xmlhttp.send();
}

function successCallback(anchor) {

  alert("ANDUVO BIEN");
}

function errCallback(anchor) {
  alert("ANDUVO MAL");
}
