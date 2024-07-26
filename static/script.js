document.addEventListener('DOMContentLoaded', function () {
    const uploadTypeRadios = document.getElementsByName('upload_type');
    const photoOptions = document.getElementById('photo-options');
    const videoOptions = document.getElementById('video-options');

    uploadTypeRadios.forEach(radio => {
        radio.addEventListener('change', function () {
            if (this.value === 'Photos') {
                photoOptions.style.display = 'block';
                videoOptions.style.display = 'none';
            } else {
                photoOptions.style.display = 'none';
                videoOptions.style.display = 'block';
            }
        });
    });

    const photoSourceRadios = document.getElementsByName('photo_source');
    const galleryUpload = document.getElementById('gallery-upload');
    const cameraUpload = document.getElementById('camera-upload');

    photoSourceRadios.forEach(radio => {
        radio.addEventListener('change', function () {
            if (this.value === 'Upload from gallery') {
                galleryUpload.style.display = 'block';
                cameraUpload.style.display = 'none';
            } else {
                galleryUpload.style.display = 'none';
                cameraUpload.style.display = 'block';
            }
        });
    });

    const imageUpload = document.getElementById('image-upload');
    const uploadedImage = document.getElementById('uploaded-image');
    imageUpload.addEventListener('change', function () {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                uploadedImage.src = e.target.result;
                uploadedImage.style.display = 'block';
            };
            reader.readAsDataURL(file);
        }
    });

    const captureBtn = document.getElementById('capture-btn');
    const capturedImage = document.getElementById('captured-image');
    captureBtn.addEventListener('click', function () {
        // Simulate camera capture - for real applications use appropriate camera API
        capturedImage.src = 'path_to_captured_image.jpg';
        capturedImage.style.display = 'block';
    });

    const videoUpload = document.getElementById('video-upload');
    const uploadedVideo = document.getElementById('uploaded-video');
    videoUpload.addEventListener('change', function () {
        const file = this.files[0];
        if (file) {
            const url = URL.createObjectURL(file);
            uploadedVideo.src = url;
            uploadedVideo.style.display = 'block';
        }
    });

    const detectBtn = document.getElementById('detect-btn');
    detectBtn.addEventListener('click', function (event) {
        event.preventDefault();
        const form = document.getElementById('upload-form');
        const formData = new FormData(form);
        
        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.blob())
        .then(blob => {
            const url = URL.createObjectURL(blob);
            const outputImage = document.getElementById('output-image');
            outputImage.src = url;
            outputImage.style.display = 'block';
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
