function submitDescriptionForm(event){
  event.preventDefault();
  var form = event.target;
  var formdata = new FormData(form);
  debugger;
  axios.put(
    form.action,
    { description: formdata.get("description") },
    { headers: { 'Content-Type': 'application/json' }}
  )
  .then(() => alert("Descripción modificada"))
  .catch(() => alert("Hubo un problema al modificar la descripción"));
}
