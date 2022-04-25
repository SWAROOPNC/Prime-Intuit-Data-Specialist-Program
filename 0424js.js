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
