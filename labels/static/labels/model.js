
class Label {

  constructor(article_id, tweet_id, hateful, profanity) {
    this.article_id = article_id;
    this.tweet_id = tweet_id;
    this.hateful = hateful;
    this.profanity = profanity;
  }

  save(successCallback, errCallback) {
    var xmlhttp = new XMLHttpRequest();
    // FIX: this is awful
    xmlhttp.open("POST", "/label/" + this.article_id + "/");
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
    // Callbacks
    xmlhttp.onload = () => successCallback(this);
    xmlhttp.onerror = () => errCallback(this);

    xmlhttp.send(JSON.stringify({
      tweet_id: this.tweet,
      hateful: this.hateful,
      profanity: this.profanity,
    }));
  }

  static createFromTab(tab) {
    var tweet_id = tab.getAttribute("data-tweet-id");
    var article_id = tab.getAttribute("data-article-id");
    var hateful = tab.querySelector('input[name="hate"]:checked').value;
    var profanity = tab.querySelector('input[name="profanity"]:checked').value;
    return new Label(
      article_id, tweet_id,
      parseInt(hateful), parseInt(profanity)
    );
  }
}
