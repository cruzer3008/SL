x = '
{
"Author1":{"name":"Yash","native":"India","title":"Bahubali","year":2012},
"Author2":{"name":"Ram","native":"UP","title":"Ramayana","year":2006},
"Author3":{"name":"Rahim","native":"Pakistan","title":"Quran","year":1654},
"Author4":{"name":"Jesus","native":"London","title":"Bible","year":213}
}';

var x = JSON.parse(x);

document.getElementById("n1").innerHTML = x.Author1.name;
document.getElementById("na1").innerHTML = x.Author1.native;
document.getElementById("t1").innerHTML = x.Author1.title;
document.getElementById("y1").innerHTML = x.Author1.year;

document.getElementById("n2").innerHTML = x.Author2.name;
document.getElementById("na2").innerHTML = x.Author2.native;
document.getElementById("t2").innerHTML = x.Author2.title;
document.getElementById("y2").innerHTML = x.Author2.year;

document.getElementById("n3").innerHTML = x.Author3.name;
document.getElementById("na3").innerHTML = x.Author3.native;
document.getElementById("t3").innerHTML = x.Author3.title;
document.getElementById("y3").innerHTML = x.Author3.year;

document.getElementById("n4").innerHTML = x.Author4.name;
document.getElementById("na4").innerHTML = x.Author4.native;
document.getElementById("t4").innerHTML = x.Author4.title;
document.getElementById("y4").innerHTML = x.Author4.year;
