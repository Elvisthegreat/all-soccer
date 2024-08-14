// Edit
const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");


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
    commentForm.setAttribute("action", `edit_comment/${commentId}`) // action attribute to know which comment to update

    // Scroll to the comment form
    commentForm.scrollIntoView({ behavior: "smooth" });
  });
}

// Delete section

const deleteConfirm = document.getElementById('deleteConfirm');
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
  deleteConfirm.href = `/official/delete_comment/${slugName}/${commentId}/`;
  
  // Show the modal
  deleteModal.show();
}

// Add click event listeners to each delete button
deleteButtons.forEach(button => {
  button.addEventListener('click', handleDeleteButtonClick);
});



 // Using Enter keyboard button function to send message
 document.getElementsByClassName("answer-box")[0].addEventListener("keydown", function(event) {
  if (event.key === "Enter"){
    event.preventDefault(); // Prevent the default action (if any)
    document.getElementById("commentForm").submit(); // Submit the form
  }
});


