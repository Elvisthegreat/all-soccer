// Initialize counts for each button
let countGreen = 0;
let countBlue = 0;
let countRed = 0;

// Define functions to increment each count and update the respective button content
function incrementCountGreen() {
    countGreen += 1;
    let button1 = document.getElementById('div-green-color');
    button1.innerHTML = `${countGreen} %<br><span>Home</span>`;
}

function incrementCountBlue() {
    countBlue += 1;
    let button2 = document.getElementById('div-blue-color');
    button2.innerHTML = `${countBlue} %<br><span>Draw</span>`;
}

function incrementCountRed() {
    countRed += 1;
    let button3 = document.getElementById('div-red-color');
    button3.innerHTML = `${countRed} %<br><span>Away</span>`;
}

// Attach event listeners to each button for the respective function
document.getElementById('div-green-color').addEventListener('click', incrementCountGreen);
document.getElementById('div-blue-color').addEventListener('click', incrementCountBlue);
document.getElementById('div-red-color').addEventListener('click', incrementCountRed);
