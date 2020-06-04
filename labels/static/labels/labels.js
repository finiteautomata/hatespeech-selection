class LabelController {

}

function showTab(n) {
  // This function will display the specified tab of the form ...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  // ... and fix the Previous/Next buttons:
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Siguiente";
  }
}


function saveLabel() {
  var x = document.getElementsByClassName("tab");
  var thisTab = x[currentTab];
  var label = Label.createFromTab(thisTab);

  label.save(labelSaved, labelErr);
}

function labelSaved() {
  var x = document.getElementsByClassName("tab");
  var thisTab = x[currentTab];

  x[currentTab].style.display = "none";

  // Increase or decrease the current tab by 1:
  currentTab = currentTab + 1;
  // if you have reached the end of the form... :
  if (currentTab >= x.length) {
    //...the form gets submitted:
    location.href = "/";
  }
  else {
    showTab(currentTab);
  }
}

function labelErr() {
  alert("Hubo un error guardando esta etiqueta");
}

function formCheck() {
  var x = document.getElementsByClassName("tab");
  var thisTab = x[currentTab];

  var labels = thisTab.querySelectorAll('.labels');

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


function nextTweet() {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:

  if (!formCheck())
    return false;

  saveLabel();
}
