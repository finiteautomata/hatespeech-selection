function deleteFromGroup(group_name, article_id) {

  var xmlhttp = new XMLHttpRequest();
  // FIX: this is awful
  xmlhttp.open("DELETE", "/group/" + article_id + "/");
  xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
  // Callbacks
  xmlhttp.onload = function(){
    successCallback(this);
  };
  xmlhttp.onerror = function(){
    errCallback(this);
  };

  var info = {
    tweet_id: this.tweet_id,
    hateful: this.hateful,
    profanity: this.profanity,
  }

  xmlhttp.send(JSON.stringify(info));
}
