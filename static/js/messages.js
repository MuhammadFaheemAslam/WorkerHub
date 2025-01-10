// static/js/messages.js
document.addEventListener('DOMContentLoaded', function () {
    // Check if the modal exists
    const messageModal = document.getElementById('messageModal');
    if (messageModal) {
        // Show the modal
        const modal = new bootstrap.Modal(messageModal);
        modal.show();

        // Automatically close after 20 seconds
        setTimeout(() => {
            modal.hide();
        }, 20000); // 20 seconds
    }

    // Event delegation for the dynamically loaded media items
    const mediaContainer = document.querySelector('#edit_post'); // Parent container of media items
    if (mediaContainer) {
        mediaContainer.addEventListener('click', function (event) {
            // Check if the clicked element is a delete button
            if (event.target && event.target.classList.contains('btn-close')) {
                const mediaItem = event.target.closest('.col-6');
                const mediaId = event.target.getAttribute('data-media-id'); // Get media ID from data attribute
                
                // Find the hidden input and mark it for deletion
                const hiddenInput = mediaItem.querySelector('.delete-media');
                if (hiddenInput) {
                    hiddenInput.style.display = 'block'; // Unhide the input to mark for deletion
                }

                // Optionally, you can also add a class for styling (e.g., red background) to indicate it's marked for deletion
                mediaItem.classList.add('deleted');

                // Remove the media item from the DOM (for visual feedback)
                mediaItem.remove();
            }
        });
    }
});
