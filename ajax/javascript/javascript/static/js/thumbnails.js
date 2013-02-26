window.onload = initPage;

function initPage() {  // find the thumbnails on the page  image = document.getElementById("image");
    image.onclick = function() {
      // find the image name
      
      getDetails("itemGuitar");
    }}function getDetails(itemName) {  request = createRequest();  if (request == null) {    alert("Unable to create request");    return;  }  var url= "get_image?ImageID=" + escape(itemName);  request.open("GET", url, true);  request.onreadystatechange = displayDetails;  request.send(null);}
function displayDetails() {  if (request.readyState == 4) {    if (request.status == 200) {      detailDiv = document.getElementById("info");      detailDiv.innerHTML = request.responseText;    }  }}