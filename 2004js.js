var n1 = parseInt(prompt("Enter num1"));
console.log(n1);
var op = prompt("Enter operator ");
console.log(op);
var n2 = parseInt(prompt("Enter num2"));
console.log(n2);

if (op=='+')
{
  x=n1+n2;
}
else if (op=='-') {
  x=n1-n2;
}
else if (op=='*') {
  x=n1*n2;
}
else if (op=='/') {
  x=n1/n2;
}
alert(n1+op+n2+"="+x);
console.log(n1+op+n2+"="+x);
switch (op) {
  case '+':x=n1+n2;  break;
  case '-':x=n1-n2;  break;
  case '*':x=n1*n2;  break;
  case '/':x=n1/n2;  break;
  default:
}
alert(n1+op+n2+"="+x);
console.log(n1+op+n2+"="+x);


function Add() {
  num1=parseInt(document.getElementById('num1').value);
  num2=parseInt(document.getElementById('num2').value);
  document.getElementById('result').innerHTML=num1+num2;
}
function Sub() {
  num1=parseInt(document.getElementById('num1').value);
  num2=parseInt(document.getElementById('num2').value);
  document.getElementById('result').innerHTML=num1-num2;
}
function multiplyBy() {
  num1=parseInt(document.getElementById('num1').value);
  num2=parseInt(document.getElementById('num2').value);
  document.getElementById('result').innerHTML=num1*num2;
}
function divideBy() {
  num1=parseInt(document.getElementById('num1').value);
  num2=parseInt(document.getElementById('num2').value);
  document.getElementById('result').innerHTML=num1/num2;
}
function Min() {
  num1=parseInt(document.getElementById('num1').value);
  num2=parseInt(document.getElementById('num2').value);
  if (num1>num2) {
    var x1=num2
  }
  document.getElementById('result').innerHTML=x1;
}
function Max() {
  num1=parseInt(document.getElementById('num1').value);
  num2=parseInt(document.getElementById('num2').value);
  if (num1>num2) {
    var x1=num1
  }
  document.getElementById('result').innerHTML=x1;
}
