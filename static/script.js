const fileInput = document.querySelector('#custom-file-input');
const imagePreview = document.querySelector('.image-preview');
const menuDropdown = document.getElementById('dropdown__menu');
const dropDownOpt = document.getElementById('dropdown__opt');
const dropdownAtivar = document.getElementById('dropdown__Ativar');
const dropdownAtivo = document.getElementById('dropdown__Ativo');
const conteudo = document.getElementById('conteudo__principal');
var mostrarDropdown = false

window.addEventListener('load', function(){
menuDropdown.addEventListener('click', function(){
    acionaDropdown()
    
})

conteudo.addEventListener('click', function(){
  if(mostrarDropdown){
    acionaDropdown()
  }
})
 
function acionaDropdown(){
    mostrarDropdown = !mostrarDropdown
    console.log(mostrarDropdown);


    dropDownOpt.classList.toggle('hidden')
    dropdownAtivo.classList.toggle('hidden')
    dropdownAtivar.classList.toggle('hidden')
   
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