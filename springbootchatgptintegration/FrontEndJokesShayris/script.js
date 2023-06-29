document.addEventListener("DOMContentLoaded", function() {
    // Get the form element
    var contentForm = document.getElementById("contentForm");
  
    // Add event listener to the form submission
    contentForm.addEventListener("submit", function(event) {
      event.preventDefault();
  
      // Get the selected content type and keyword
      var contentType = document.getElementById("content").value;
      var keyword = document.getElementById("keyword").value;
  
      // Make an API call with the selected content type and keyword
      generateContent(contentType, keyword);
    });
  
    // Function to make an API call and generate content
    function generateContent(contentType, keyword) {
      // Set the API endpoint based on the content type
      var endpoint;
      if (contentType === "shayari") {
        endpoint = `http://localhost:8080/bot/shayari?keyword=${keyword}`;
      } else if (contentType === "jokes") {
        endpoint = `http://localhost:8080/bot/jokes?topic=${keyword}`;
      } else if (contentType === "quotes") {
        endpoint = `http://localhost:8080/bot/quotes?topic=${keyword}`;
      } else if (contentType === "stories") {
        endpoint = `http://localhost:8080/bot/stories?topic=${keyword}`;
      }
  
      // Make an API call to the backend using fetch
      fetch(endpoint)
        .then(function(response) {
           // console.log(response); 
          return response.text();
        })
        .then(function(data) {
          // Display the generated content in the output div
         // console.log(data); 
          var contentOutput = document.getElementById("contentOutput");
          contentOutput.innerHTML = data;
          contentOutput.classList.remove("hidden");
        })
        .catch(function(error) {
          console.log("Error:", error);
        });
    }
  });
  