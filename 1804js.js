  console.log("while loop ")
  var x=0;
  while (x<5)
    {
      console.log("x is currentl : "+x);
      if (x==3)
        {
          console.log("x is now equal to 3 ");
          break;
        }
        x=x+1;
    }
console.log("while even numbers ")
var x=1;
while (x<11)
  {
    if (x%2==0)
      {
        console.log(x);
      }
      x=x+1;
  }
console.log(" for loop ");

for (var i = 0; i < 5; i++) {
  console.log("number is "+i)
}
console.log(" for loop word ");
var word = "abcdefghi"
for (var i = 0; i < word.length; i++)
{
  if (i%2===0)
    {
      console.log(word[i])
    }
    i=i+1;

}
console.log(" Functions ");
function hello()
{
  console.log("Hello PI ");
}
hello();

function helloYou(name)
{
  console.log("Hello "+name);
}
helloYou(prompt("Enter name"));
