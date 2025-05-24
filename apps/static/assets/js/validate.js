function validateName(){
    let name = document.getElementById('name').value;
    const pattern = /^[a-zA-Z0-9_.-]+$/;

    if (!pattern.test(name)) {
        showError('name');
    } else {
        resetError('name')
    }
}


function showError(inputField){
    let field = document.getElementById(inputField);
    field.classList.add('error');
}

function resetError(id) {
    let field = document.getElementById(id);
    field.classList.remove('error');
}