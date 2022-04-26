//document.getElementById("Raj").innerHTML = "My Name is Raj"



//console.dir(document)



//console.log(document.domain)



//console.log(document.head);



//console.log(document.body);



//console.log(document.BODY);



//console.log(document.all);



//console.log(document.all[8]);



//document.all[8].textContent = "prime intuit";



//console.log(document.getElementById('header-title'));



//document.all[7].textContent = "Prime Intuit";//

//console.log(document.forms);//

//var headerTitle = document.getElementById('header-title');

//console.log(headerTitle);

//headerTitle.textcontent = 'Number of pages'

//headerTitle.innerHTML = '<h3>number of pages</h3>';//

//headerTitle.style.borderBottom = 'solid 3px #64eb34';
/*
var items = document.getElementsByClassName('listitem');

console.log(items);



items[4].textContent = "Wall-E"

items[4].style.fontWeight = 'bold'

items[4].style.background = 'pink'



for(var i = 0; i<items.length;i++){

  if (i%2 === 0){

  items[i].style.background = "red"

}

}

var header = document.querySelector('#header-title');
console.log(header);
header.style.borderBottom = "solid 4px #42f57b";


var input = document.querySelector('input');
input.value = 'Please Enter Your Name ';

var submit = document.querySelector('input[type="submit"]');
submit.value = 'Send';

var item = document.querySelector(".listitem");
item.style.color = 'red';

var seconditem = document.querySelector(".listitem:nth-child(5)");
console.log('seconditem');
seconditem.style.color = 'coral';

var fifthitem = document.querySelector(".listitem:nth-child(3)");
console.log('fifthitem');
fifthitem.style.color = 'coral';

var titles = document.querySelectorAll(".title");
console.log(titles);
titles[0].textContent = "Chicago";
*/
var odd = document.querySelectorAll('.listitem:nth-child(odd)');
var even = document.querySelectorAll('.listitem:nth-child(even)');
console.log(odd);
for (var i = 0; i < odd.length; i++) {
  odd[i].style.backgroundColor = '#9234';
  even[i].style.backgroundColor = '#ccc';
}
