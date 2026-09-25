const burgerBtn = document.getElementById("burgerBtn")
const HeaderNav = document.querySelector(".Header__nav")


burgerBtn.addEventListener("click", () => {
    HeaderNav.classList.toggle("is-open")
    burgerBtn.classList.toggle("is-active")
})

