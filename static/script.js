const fileInput = document.querySelector('#custom-file-input');
const imagePreview = document.querySelector('.image-preview');

fileInput.addEventListener('change', () => {
  const file = fileInput.files[0];
  const reader = new FileReader();

  reader.addEventListener('load', () => {
    imagePreview.src = reader.result;
  });

  reader.readAsDataURL(file);
});