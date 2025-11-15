
    document.addEventListener('DOMContentLoaded', () => {
        const openModalBtn = document.getElementById('openApplyModal');
        const closeModalBtn = document.getElementById('closeApplyModal');
        const modalBackdrop = document.getElementById('applyModal');
        const resumeInput = document.getElementById('resume');
        const fileNameDisplay = document.getElementById('file-name-display');

        // --- Modal Controls ---

        // Show the modal
        openModalBtn.addEventListener('click', () => {
            modalBackdrop.classList.add('show');
        });

        // Hide the modal with the 'X' button
        closeModalBtn.addEventListener('click', () => {
            modalBackdrop.classList.remove('show');
        });

        // Hide the modal by clicking on the backdrop
        modalBackdrop.addEventListener('click', (event) => {
            // Check if the click is on the backdrop itself, not the content
            if (event.target === modalBackdrop) {
                modalBackdrop.classList.remove('show');
            }
        });

        // --- File Input Display ---
        resumeInput.addEventListener('change', () => {
            if (resumeInput.files.length > 0) {
                fileNameDisplay.textContent = `Selected file: ${resumeInput.files[0].name}`;
            } else {
                fileNameDisplay.textContent = '';
            }
        });
    });