window.onload = function(){ 
  let gotositebutton = document.getElementById('gotositebutton');
  let togglestatebutton = document.getElementById('togglestatebutton');

  chrome.storage.sync.get('toggle_state', function(is_on) {
      if (is_on.toggle_state == false) {
        togglestatebutton.innerHTML = 'Enable Semaphore'
      }
      else {
        togglestatebutton.innerHTML = 'Disable Semaphore'
      }
    });

  gotositebutton.onclick = function(element) {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.tabs.create({
       url: "https://semaphore-staging.herokuapp.com/my_flags"
      });
  })};



  togglestatebutton.onclick = function(element) {
    chrome.storage.sync.get('toggle_state', function(is_on) {
      let newstate = !is_on.toggle_state;
      chrome.storage.sync.set({'toggle_state': newstate});
      if (newstate == false) {
        togglestatebutton.innerHTML = 'Enable Semaphore'
        window.close();
      }
      else {
        togglestatebutton.innerHTML = 'Disable Semaphore'
      }
    });
  }; 
};

