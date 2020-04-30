chrome.cookies.get({"url": "https://semaphore-staging.herokuapp.com/my_flags", "name": "sessionid"}, function(cookie) {
  chrome.cookies.set({
    "url": "https://semaphore-staging.herokuapp.com/api/v0/raw_flags/", 
    "value": cookie.value, 
    "expirationDate": cookie.expirationDate});
});

chrome.runtime.onInstalled.addListener(function() {
  chrome.storage.sync.set({'toggle_state': true}, function() {
    console.log('Extension is on');
  });
});

chrome.webRequest.onSendHeaders.addListener(
  function sendReports(info) {
    if (info.url.includes("report")) {
      chrome.storage.sync.get('toggle_state', function(is_on) {
        if (is_on.toggle_state == true) {
          parseURL(info.url);
        }
      });
    }
  },
  // filters
  {
    urls: [
      "https://twitter.com/i/*"
    ],
  },
  // extraInfoSpec
  []);