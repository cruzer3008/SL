function check(){
		var x = document.getElementById("ip").value;
		alert(x);
		if(x==""){document.getElementById("result").innerHTML = "Enter some value";}
		else if(x<0){document.getElementById("result").innerHTML = "Enter a positive value";}
		else{
			if(x%3==0&&x%7==0)
				document.getElementById("result").innerHTML = "The number is divisible by 7 and divisible by 3";
			else if(x%3!=0&&x%7==0)
				document.getElementById("result").innerHTML = "The number is divisible by 7 and NOT divisible by 3";
			else if(x%3==0&&x%7!=0)
				document.getElementById("result").innerHTML = "The number is NOT divisible by 7 and divisible by 3";
			else
				document.getElementById("result").innerHTML = "The number is NOT divisible by 7 and NOT divisible by 3";
		}
}
