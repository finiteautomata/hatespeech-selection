
class Label {

  constructor(tweet_id, hateful) {
    this.tweet_id = tweet_id;
    this.hateful = hateful
  }

  save(successCallback, errCallback) {
    var xmlhttp = new XMLHttpRequest();
    // FIX: this is awful
    xmlhttp.open("POST", "/label");
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
    // Callbacks
    xmlhttp.onload = successCallback;
    xmlhttp.onerror = errCallback;

    xmlhttp.send(JSON.stringify({
      tweet_id: this.tweet
    }));
  }

  static createFromTab(tab) {
    var tweet_id = tab.getAttribute("data-tweet-id");

    return new Label(tweet_id);
  }
}
