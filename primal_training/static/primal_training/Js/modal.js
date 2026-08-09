document.addEventListener('DOMContentLoaded',() =>  {
    const modal = document.getElementById('reservationModal')
    const closeBtn = document.querySelector('.close-btn')
    const modalClassId = document.getElementById('modalClassId')
    const modalTite = document.getElementById('modalTitle')
    const   openBtns = document.querySelectorAll('.open-modal-btn')

    const modalForm = document.querySelector('.modal-form')
    

    openBtns.forEach( btn =>{
        btn.addEventListener("click" ,() => {
            const classId = btn.dataset.classId
            const classTitle = btn.dataset.classTitle

            modalClassId.value = classId
            modalTite.innerHTML = `BOOK: <span>${classTitle}</span>`

            modal.classList.add("active")
        })
    })

    closeBtn.addEventListener('click', () => {
        modal.classList.remove('active')
    })


    modalForm.addEventListener('submit', (e) => {
        e.preventDefault()

        console.log("Form send!");
    })
})