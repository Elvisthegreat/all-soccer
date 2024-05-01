// Edit
const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

// Delete
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("data-comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`); // action attribute to know which comment to update
  });
}


/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("data-comment_id");
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
  });
}




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


