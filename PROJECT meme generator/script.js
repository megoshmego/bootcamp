document.addEventListener("DOMContentLoaded", function(){  
  var memeForm = document.getElementById("meme-form");
  var displayList = document.querySelector(".display");
 memeForm.addEventListener("submit", function(event) {
  event.preventDefault();
  
  var memeLi = document.createElement('li');
  memeLi.classList.add("meme-img");

var topText = document.getElementById("text-top");
var urlInput = document.getElementById('uploaded-img').value,
src =  urlInput,
img = document.createElement('img');
img.src = src;

var topTextDiv = document.createElement('div');
topTextDiv.classList.add("text", "top");
topTextDiv.innerText = document.getElementById("text-top").value;

var bottomTextDiv = document.createElement('div');
bottomTextDiv.classList.add("text", "bottom");
bottomTextDiv.innerText = document.getElementById("text-bottom").value;

var removeDiv = document.createElement('div');
removeDiv.classList.add("nope");
removeDiv.innerText = "nope";
removeDiv.style.color = "black";


displayList.appendChild(memeLi);
memeLi.appendChild(img);
memeLi.appendChild(topTextDiv);
memeLi.appendChild(bottomTextDiv);
memeLi.appendChild(removeDiv);

memeForm.reset();

});
function remove(event){
event.target.parentNode.remove();
}
displayList.addEventListener('click', remove, false);
});





















