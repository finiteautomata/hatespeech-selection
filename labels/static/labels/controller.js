class LabelController {
  constructor() {
    this.n = 0;
  }

  get currentTab() {
    return document.getElementsByClassName("tab")[this.n];
  }


  showTab() {
    // This function will display the specified tab of the form ...
    this.currentTab.style.display = "block";
    // ... and fix the Previous/Next buttons:
    // if (this.n == (x.length - 1)) {
    //   document.getElementById("nextBtn").innerHTML = "Finalizar";
    // } else {
    //   document.getElementById("nextBtn").innerHTML = "Siguiente";
    // }
  }

  formCheck() {

    var labels = this.currentTab.querySelectorAll('.labels');

    var ret = true;
    var msg = "";
    for (let label_div of labels) {
      let label_name = label_div.getAttribute("data-label");
      console.log("Checking ", label_name);

      if (label_div.querySelectorAll("input:checked").length == 0) {
        ret = false;
        msg += label_div.querySelector("p").textContent;
      }
    }

    if (!ret) {
      alert("Faltan etiquetar "+msg);
    }
    return ret;
  }

  nextTweet() {
    // This function will figure out which tab to display
    if (!this.formCheck())
      return false;

    var label = Label.createFromTab(this.currentTab);
    label.save(
      (req) => this.labelSaved(req),
      (req) => this.labelErr(req)
    );
  }

  labelSaved(xmlhttp) {
    var numTabs = document.getElementsByClassName("tab").length;
    this.currentTab.style.display = "none";
    this.n += 1;
    // if you have reached the end of the form... :
    if (this.n >= numTabs) {
      //...the form gets submitted:
      location.href = "/";
    }
    else {
      this.showTab();
    }
  }

  labelErr(xmlhttp) {
    alert("Hubo un error guardando esta etiqueta");
  }

}
