const fileInput = document.querySelector('#custom-file-input');
const imagePreview = document.querySelector('.image-preview');
const menuDropdown = document.getElementById('dropdown__menu');
const dropDownOpt = document.getElementById('dropdown__opt');
const dropdownImage = document.getElementsByClassName('dropdown__image');
var mostrarDropdown = false

window.addEventListener('load', function(){
menuDropdown.addEventListener('click', function(){
    acionaDropdown()
})

function acionaDropdown(){
    mostrarDropdown = !mostrarDropdown
    if(mostrarDropdown){
        dropDownOpt.classList.remove('hidden')
    }else{
        dropDownOpt.classList.add('hidden')
    }
}

})

fileInput.addEventListener('change', () => {
  const file = fileInput.files[0];
  const reader = new FileReader();

  reader.addEventListener('load', () => {
    imagePreview.src = reader.result;
  });

  reader.readAsDataURL(file);
});