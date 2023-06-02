var submit_button = document.querySelector('#get-conversion');

submit_button.onclick = function() {
	var dataInput = document.getElementById("usd-value").value;
	var coinInput = document.getElementById("coins").value
	getConvert(dataInput, coinInput);
};

function getConvert(usd, coin) {
	url = "http://127.0.0.1:8080/convert/" + usd + "/" + coin
    fetch(url, {
		//headers
		//method
		//body
		method: "GET",
		credentials: "include",
		headers: {
			"Content-Type": "application/x-www-form-urlencoded"
		}
	}).then(function (response) {
		response.json().then(function (data) {
			var coinList = document.querySelector("#coin-response");
			// insert the card into the DOM
			var coinData = document.createElement("h3");
			coinData.innerHTML = "<b>Coin Name:</b> " + data.coin + "<br><b>Coin Equivalent:</b> " + data.numOfCoins;
			coinData.style.color = "#000000";
			coinList.appendChild(coinData);
		});
	});
};