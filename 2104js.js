function insert(num) {
  document.form1.textview.value = document.form1.textview.value+num;
}
function equal() {
  if (document.form1.textview.value) {
    document.form1.textview.value = eval(document.form1.textview.value);
  }
}
function backSpace() {
  var exp= document.form1.textview.value;
  document.form1.textview.value = exp.substr(0, exp.length - 1)
}
