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