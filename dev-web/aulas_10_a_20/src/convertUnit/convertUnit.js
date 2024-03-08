function convertpolToCm(pol) {
    const cm = pol * 2.54;
    return cm;
}

function convert() {
    const polInput = document.getElementById("pol");
    const resultElement = document.getElementById("result");

    if (polInput.value === "") {
        resultElement.textContent = "Por favor, insira um valor em polegadas.";
        return;
    }

    const pol = parseFloat(polInput.value);
    if (isNaN(pol)) {
        resultElement.textContent = "Por favor, insira um valor numérico válido.";
        return;
    }

    const cm = convertpolToCm(pol);
    resultElement.textContent = `${pol} polegadas é igual a ${cm.toFixed(2)} centímetros.`;
}
