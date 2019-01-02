x = '{"Person1":{"name":"Yash",story:"Bahubali"},"Person2":{"name":"Ram",story:"Ramayan"},"Person3":{"name":"Rahim",story:"Quran"},"Person4":{"name":"Jesus",story:"Bible"}}';

var x = JSON.parse(x)
document.getElementById("n1").innerHTML = x.Person1.name;
document.getElementById("s1").innerHTML = x.Person1.story;

document.getElementById("n2").innerHTML = x.Person2.name;
document.getElementById("s2").innerHTML = x.Person2.story;

document.getElementById("n3").innerHTML = x.Person3.name;
document.getElementById("s3").innerHTML = x.Person3.story;

document.getElementById("n4").innerHTML = x.Person4.name;
document.getElementById("s4").innerHTML = x.Person4.story;
