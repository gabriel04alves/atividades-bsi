function divisibilityChecker(x, y) {
    if (y === 0) {
        return "Não é possível dividir um número por 0!";
    } 

    if (x % y === 0) {
        return 1;
    } else {
        return 0;
    }
}

function checkDivisibility() {
    const inputX = parseInt(document.getElementById('inputX').value);
    const inputY = parseInt(document.getElementById('inputY').value);

    if (isNaN(inputX) || isNaN(inputY)) {
        document.getElementById('divisibilityResult').innerHTML = "Valor inválido. Tente novamente.";
        return;
    }

    const result = divisibilityChecker(inputX, inputY);

    if (result === "Inválido!") {
        document.getElementById('divisibilityResult').innerHTML = result;
    } else if (result === 1) {
        document.getElementById('divisibilityResult').innerHTML = inputX + " é divísivel por " + inputY;
    } else {
        document.getElementById('divisibilityResult').innerHTML = inputX + " não é divísivel por " + inputY;
    }
}
