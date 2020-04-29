function parseURL(url) {
  const params = new URLSearchParams(url);
  const data = {
  	reported_user_id: params.get('reported_user_id'),
  	reported_tweet_id: params.get('reported_tweet_id'),
  	language: params.get('lang')
  }
  fetch('https://semaphore-staging.herokuapp.com/api/v0/raw_flags/', {
	  method: 'POST',
	  headers: {
	    'Content-Type': 'application/json',
	  },
	  body: JSON.stringify(data),
	  state: 'modern',
	})
	.then((response) => {
    if (response.status == 403) {
      console.log('found 403 error');
      chrome.windows.create(
        {url: "login.html", type: "popup", width: 320, height: 320});
    }
  })
	.then((data) => {
	  console.log('Success:', data);
	})
	.catch((error) => {
	  console.error('Error:', error);
	});
}