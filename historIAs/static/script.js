function updateRemoveButtons() {
    const RemoveButtons = document.querySelectorAll('.ingredient-row .btn-danger')
    if (document.querySelectorAll('.titulo-row').length <= 1) {
        RemoveButtons.forEach(button => button.disabled = true)
    } else {
        RemoveButtons.forEach(button => button.disabled = false)
    }
}
async function submitForm() {
    const tituloInputs = document.getElementsByClassName('titulo')
    const titulos = [];
    for (let i = 0; i < tituloInputs.length; i++) {
        if (tituloInputs[i].value) {
            titulos.push(tituloInputs[i].value)
        }
    }

    if (titulos.length < 1) {
        alert('Por favor, preencha o campo!')
        return
    }

    const data = {
        titulos: titulos
    }

    try {
        const response = await fetch('/historia', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })

        const result = await response.json()

        const responseDiv = document.getElementById('response')
        if (result) {
            console.table(result)
            const resultado = result.join('')
            responseDiv.innerHTML = resultado
        } else if (typeof result === "string") {
            responseDiv.innerHTML = result
        } else {
            responseDiv.innerHTML = `<p>Erro: ${result.Erro}</p>`
        }
        responseDiv.style.display = 'block'
    } catch (error) {
        const responseDiv = document.getElementById('response')
        responseDiv.innerHTML = `<p>Erro: ${error.message}</p>`
        responseDiv.style.display = 'block'
    }
}

document.addEventListener('DOMContentLoaded', updateRemoveButtons)