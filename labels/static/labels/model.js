
class Label {

  constructor(slug, tweet_id, hateful, profanity) {
    this.slug = slug;
    this.tweet_id = tweet_id;
    this.hateful = hateful;
    this.profanity = profanity;
  }

  save(successCallback, errCallback) {
    var xmlhttp = new XMLHttpRequest();
    // FIX: this is awful
    xmlhttp.open("POST", "/label/" + this.slug + "/");
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

  static createFromTab(tab) {
    var tweet_id = tab.getAttribute("data-tweet-id");
    var slug = tab.getAttribute("data-article-slug");
    var hateful = tab.querySelector('input[name="hate"]:checked').value;
    var profanity = tab.querySelector('input[name="profanity"]:checked').value;
    return new Label(
      slug, tweet_id,
      parseInt(hateful), parseInt(profanity)
    );
  }
}
