// Edit section

// Each edit button has a data attribute 'data-comment_id' with the comment's ID
const editButtons = document.querySelectorAll('.btn-edit');

// Function to handle the edit button click event
function handleEditButtonClick(event) {
  // Retrieve the comment ID from the data attribute of the clicked button
  const commentId = event.target.getAttribute('data-comment_id');
  
  // Find the comment text element by its ID
  const commentTextElement = document.getElementById('comment' + commentId);
  
  // Extract the text content of the comment
  const commentText = commentTextElement.textContent || commentTextElement.innerText;
  
  // Set the text content as the value of the comment form's textarea
  document.getElementById('id_body').value = commentText;
  
  // Optionally, scroll to the comment form and focus the textarea
  document.getElementById('commentForm').scrollIntoView();
  document.getElementById('id_body').focus();
}

// Add click event listeners to each edit button
editButtons.forEach(button => {
  button.addEventListener('click', handleEditButtonClick);
});



 // Using Enter keyboard button function to send message
document.getElementsByClassName("answer-box")[0].addEventListener("keydown", function(event) {
  if (event.key === "Enter"){
    event.preventDefault(); // Prevent the default action (if any)
    document.getElementById("commentForm").submit(); // Submit the form
  }
});




// Delete section

const deleteConfirm = document.getElementById('deleteConfirm')
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.querySelectorAll('.btn-delete');

// Function to handle the delete button click event
function handleDeleteButtonClick(event) {
  // Prevent the default button action
  event.preventDefault();
  
  // Retrieve the comment ID from the data attribute of the clicked button
  const commentId = event.target.getAttribute('data-comment_id');
  const slugName = event.target.getAttribute('data-slug_name');
  
  // Update the href of the delete confirmation button in the modal
  deleteConfirm.href = `/official/delete_comment/${slugName}/${commentId}/`; // Update this URL to your comment deletion endpoint
  
  // Show the modal
  deleteModal.show();
}

// Add click event listeners to each delete button
deleteButtons.forEach(button => {
  button.addEventListener('click', handleDeleteButtonClick);
});



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


