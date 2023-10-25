let switchMode = document.getElementById("switchMode");

switchMode.onclick = function() {

	if (localStorage.getItem("theme") === null){
		localStorage.setItem("theme", "dark");
	}
	else if (localStorage.getItem("theme") === 'dark'){
		localStorage.setItem("theme", "light");
	}
	else {
		localStorage.setItem("theme", "dark");
	}
	addStyle();

}

function addStyle(argument) {
	let theme = document.getElementById("theme");
	try {
		if (localStorage.getItem("theme") === "light"){
			theme.href = '/static/css/light_styles.css';
			switchMode.style.color = rgbToHex(36, 171, 0);
		}
		else if (localStorage.getItem("theme") === "dark"){
			theme.href = '/static/css/dark_styles.css';
			switchMode.style.color = rgbToHex(36, 171, 0);
		}
	}
	catch (err){}	
}



addStyle();

