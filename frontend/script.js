document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("modal");
    const modalImage = document.getElementById("modal-image");
    const closeBtn = document.getElementsByClassName("close")[0];

    // Function to open modal with clicked image
    function openModal(imageUrl) {
        modal.style.display = "block";
        modalImage.src = imageUrl;
    }

    // Function to close modal
    function closeModal() {
        modal.style.display = "none";
    }

    // Event listener for image clicks
    const galleryItems = document.querySelectorAll(".gallery-item");
    galleryItems.forEach(item => {
        item.addEventListener("click", function () {
            const imageUrl = this.querySelector("img").src;
            openModal(imageUrl);
        });
    });

    // Event listener for close button click
    closeBtn.addEventListener("click", closeModal);

    // Event listener for clicking outside the modal to close it
    window.addEventListener("click", function (event) {
        if (event.target == modal) {
            closeModal();
        }
    });
});
