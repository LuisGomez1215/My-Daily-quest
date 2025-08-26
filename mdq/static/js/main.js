(function(d) {
    // Enable Boostrap alert close buttons
    const alertBtns = document.querySelectorAll('[data-bs-dismiss=alert]')
    alertBtns.forEach(btn => {
        btn.addEventListener('click', e => {
            const el = e.target.closest('.alert')
            if (el) el.parentNode.removeChild(el)
        })
    })
})(document)