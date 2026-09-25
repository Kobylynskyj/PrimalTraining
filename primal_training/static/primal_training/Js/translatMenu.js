
function toggleLangMenu() {
  document.getElementById("lang-menu").classList.toggle("show");
}


function submitLang(langCode) {
  document.getElementById("selected-language-input").value = langCode;
  document.getElementById("custom-lang-form").submit();
}


window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (let i = 0; i < dropdowns.length; i++) {
        let openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
};