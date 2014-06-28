def yo_all(api_token):
	return requests.post("http://api.justyo.co/yoall/", data={'api_token': api_token})

crowd-yo_token = ''
yo_all(crowd-yo_token)