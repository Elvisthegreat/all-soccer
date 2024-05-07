// Vote section

// Initialize counts for each button or load them from localStorage
let countGreen = localStorage.getItem('countGreen') ? parseInt(localStorage.getItem('countGreen')) : 0;
let countBlue = localStorage.getItem('countBlue') ? parseInt(localStorage.getItem('countBlue')) : 0;
let countRed = localStorage.getItem('countRed') ? parseInt(localStorage.getItem('countRed')) : 0;

// Update button content with the current count from localStorage
document.getElementById('div-green-colorBarca').innerHTML = `${countGreen} %<br><span>Home</span>`;
document.getElementById('div-blue-colorDBP').innerHTML = `${countBlue} %<br><span>Draw</span>`;
document.getElementById('div-red-colorPsg').innerHTML = `${countRed} %<br><span>Away</span>`;


// Define functions to increment each count, update the respective button content, and save to localStorage
function incrementCountGreen() {
    countGreen += 1;
    localStorage.setItem('countGreen', countGreen);
    document.getElementById('div-green-colorBarca').innerHTML = `${countGreen} %<br><span>Home</span>`;
}

function incrementCountBlue() {
    countBlue += 1;
    localStorage.setItem('countBlue', countBlue);
    document.getElementById('div-blue-colorDBP').innerHTML = `${countBlue} %<br><span>Draw</span>`;
}

function incrementCountRed() {
    countRed += 1;
    localStorage.setItem('countRed', countRed);
    document.getElementById('div-red-colorPsg').innerHTML = `${countRed} %<br><span>Away</span>`;
}

// Attach event listeners to each button for the respective function
document.getElementById('div-green-colorBarca').addEventListener('click', incrementCountGreen);
document.getElementById('div-blue-colorDBP').addEventListener('click', incrementCountBlue);
document.getElementById('div-red-colorPsg').addEventListener('click', incrementCountRed);


