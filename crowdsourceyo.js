var counter = 0;

function yo_all(api_token):
	requests.post("http://api.justyo.co/yoall/", data={'api_token': api_token})


var crowd-yo_token = '2f9286ca-25cd-5342-e48c-8442aabbb2bb'

setInterval(function() {
	if (document.referrer != null) {
				counter++;
	}
	if (counter > 5) {
		yo_all(crowd-yo_token)
	}
}, 500);

setInterval(function() {
			counter = 0;
}, 100000000);