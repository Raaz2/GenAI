// Get the necessary elements
const codeInput = document.getElementById('codeInput');
const languageSelect = document.getElementById('languageSelect');
const convertBtn = document.getElementById('convertBtn');
const debugBtn = document.getElementById('debugBtn');
const qualityCheckBtn = document.getElementById('qualityCheckBtn');
const codeOutput = document.getElementById('codeOutput');


// Function to handle the conversion
function convertCode() {
    const code = codeInput.value;
    const selectedLanguage = languageSelect.value;
    // Make a request to your backend API to convert the code
    // Replace 'YOUR_BACKEND_URL' with the actual URL of your backend endpoint
    fetch(`http://localhost:8080/convertor/${selectedLanguage}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
              "topic": `${code}`
        })
    })
    .then(response => response.text())
    .then(convertedCode => {
        codeOutput.textContent = convertedCode;
    })
    .catch(error => {
        console.error('Error:', error);
        codeOutput.textContent = 'An error occurred during code conversion.';
    });
}

// Attach event listener to the Convert button
convertBtn.addEventListener('click', convertCode);


// Function to handle the debug button click
function debugCode() {
  // Add your debug logic here
  console.log('Debug button clicked');
  const code = codeInput.value;
    // Make a request to your backend API to convert the code
    // Replace 'YOUR_BACKEND_URL' with the actual URL of your backend endpoint
    fetch(`http://localhost:8080/convertor/debug`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
              "topic": `${code}`
        })
    })
    .then(response => response.text())
    .then(convertedCode => {
        codeOutput.textContent = convertedCode;
    })
    .catch(error => {
        console.error('Error:', error);
        codeOutput.textContent = 'An error occurred during code conversion.';
    });
}

// Function to handle the quality check button click
function qualityCheckCode() {
  // Add your quality check logic here
  console.log('Quality Check button clicked');
  const code = codeInput.value;
    // Make a request to your backend API to convert the code
    // Replace 'YOUR_BACKEND_URL' with the actual URL of your backend endpoint
    fetch(`http://localhost:8080/convertor/quality`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
              "topic": `${code}`
        })
    })
    .then(response => response.text())
    .then(convertedCode => {
        codeOutput.textContent = convertedCode;
    })
    .catch(error => {
        console.error('Error:', error);
        codeOutput.textContent = 'An error occurred during code conversion.';
    });
}

// Attach event listeners to the buttons
convertBtn.addEventListener('click', convertCode);
debugBtn.addEventListener('click', debugCode);
qualityCheckBtn.addEventListener('click', qualityCheckCode);