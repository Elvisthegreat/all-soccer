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


