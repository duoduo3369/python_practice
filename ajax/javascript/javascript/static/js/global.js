function popAlert()
{
	alert("弹出")
}
imagelist = ["person.jpg","pench.gif","book.jpg","chess.PNG"];
i = 1;
function resize(){
	document.getElementById("image").style.height = (document.body.clientHeight - 100) * 0.9;
	/*
	imgHeight = (document.body.clientHeight - 100)*0.9;
	document.getElementById("image").style.height = imgHeight;
	*/
	//alert("height"+document.getElementById("image").style.height + " " + document.getElementById("image").style.width);
}
function changeImage(){
	i++;
	var length = imagelist.length;
	document.getElementById("image").src = "static/img/"+imagelist[i % length];
	
}
function resizeRock() {
	document.getElementById("image").style.height = (document.body.clientHeight - 100) * 0.9;
}
function regist(){
	if(!navigator.cookieEnabled){
		document.getElementById("info").innerHTML = "cookie不能用啊原来";
		return null;
	}
	var user_name = readCookie("regist_user_name");
	//document.getElementById("info").innerHTML = "欢迎你：" + user_name;
	if(user_name){
		document.getElementById("info").innerHTML = "欢迎你：" + user_name;
	}else{
		var name = prompt("请输入名字");
		if(name){
			writeCookie("regist_user_name", name, 5);
		}
	}	
}
