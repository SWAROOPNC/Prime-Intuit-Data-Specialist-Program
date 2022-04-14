alert("Welcome to Swaroop Bank");
var deposit = prompt("Enter the amount you want to deposit");
alert("You have deposited Rs. "+deposit);
console.log("Deposit Successful");
alert("Pounds to KG convertor ");
var pound = prompt("Enter the pounds ");
var kg = 0.456*pound;
alert("Kg is "+kg);
console.log("Conversion Successful");
var x = (deposit == pound);
alert("deposit == pound "+x);
var x = (deposit != pound);
alert("deposit != pound "+x);
var x = 1;
var y = 2;
var x1 = ('2' ==y && x === 1);
alert("('2' == y && x === 1) "+x1);
var x1 = (x>=0 ||  y === 2);
alert("(x>=0 ||  y === 2) "+x1);
var x1 = !((x!=1) &&  y === (1+1));
alert("!((x!=1) &&  y === (1+1))"+x1);

var hot = false ;
var temp = prompt("Enter temperature ");

if (temp > 25) {
  hot = true;
}
console.log(hot);
if (temp > 20)
{
  alert("Temperature is HOT, NOte , java not related to javascript");
  console.log("Temperature is HOT");
}
else {
  alert("Temperature is not soo hot , NOte , java not related to javascript");
  console.log("Temperature is not HOT");
}

if (temp > 20 && temp <25)
{
  console.log("Temperature is MODERATE");
}
else if (temp>25){
  console.log("Temperature is VERY  HOT");
}
else {
  alert("Temperature is COLD");
}
