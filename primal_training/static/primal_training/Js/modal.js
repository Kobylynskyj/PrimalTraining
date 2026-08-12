document.addEventListener('DOMContentLoaded',() =>  {
    const modal = document.getElementById('reservationModal')
    const closeBtn = document.querySelector('.close-btn')
    const modalClassId = document.getElementById('modalClassId')
    const modalTite = document.getElementById('modalTitle')
    const   openBtns = document.querySelectorAll('.open-modal-btn')

    const modalForm = document.querySelector('.modal-form')
    
    const closeModal = () => {
        modal.classList.remove('active');
        document.body.classList.remove('no-scroll');
    };


    openBtns.forEach( btn =>{
        btn.addEventListener("click" ,() => {
            const classId = btn.dataset.classId
            const classTitle = btn.dataset.classTitle

            modalClassId.value = classId
            modalTite.innerHTML = `BOOK: <span>${classTitle}</span>`

            modal.classList.add("active")
            document.body.classList.add("no-scroll");
        })
    })


    closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    


if (modalForm) {
    const requiredInputs = modalForm.querySelectorAll('input[required]');
        requiredInputs.forEach (input  => {
            const parentField = input.parentElement;
            const label = parentField.querySelector('label')
            let errorMsg = parentField.querySelector('.error-text');

            input.addEventListener('input', () => {
                if(input.value.trim() !== '') {
                    input.style.borderColor = '';
                    input.style.backgroundColor = '';

                    const parentField = input.parentElement;
                    const errorMsg = parentField.querySelector('.error-text');
                    
                    if(label) {
                        label.style.color = ''
                    }

                    if(errorMsg) {
                        errorMsg.remove()
                    }
                }
            })
        })


        modalForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(modalForm);
            let isValid = true
            
            requiredInputs.forEach(input => {
                const parentField = input.parentElement;
                const label = parentField.querySelector('label');
                let errorMsg = parentField.querySelector('.error-text');
                if(input.value.trim() === '') {
                    isValid = false
                    input.style.borderColor = "#ff3333"
                    input.style.backgroundColor = "#fff0f0"
                    if(label) {
                        label.style.color = '#ff3333'
                    }

                    if(!errorMsg) {
                        errorMsg = document.createElement('span');
                        errorMsg.className = 'error-text';
                        errorMsg.style.color = '#ff3333';
                        errorMsg.style.fontSize = '11px';
                        errorMsg.style.fontWeight = '700';
                        errorMsg.style.marginTop = '4px';
                        parentField.appendChild(errorMsg);
                        const labelText = label ? label.textContent.trim() : 'field';
                        errorMsg.textContent = ` Please enter ${labelText}`
                    }
                } else {
                    input.style.borderColor = ''
                    input.style.backgroundColor = ''

                    if(label) {
                        label.style.color = ''
                    }

                    if(errorMsg) {
                        errorMsg.remove()
                    }
                }
            })

            if(!isValid){
                return;
            }


            try {
                const response = await fetch(modalForm.action, {
                    method: "POST",
                    body: formData,
                    headers: {
                        'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                    }
                });

                if (response.ok) {
                    window.location.href = response.url;
                } else {
                    alert('Error creating reservation');
                }
            } catch (error) {
                const data = await response.json()
                alert(data.error || 'Error creating reservation')
            }
        });
    }
});
    
    
