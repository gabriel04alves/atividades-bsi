function sumIntegersInRange(n1, n2) {
    let sum = 0;
    for (let i = n1; i <= n2; i++) {
        sum += i;
    }
    return sum;
}

function calculateSum() {
    const n1 = parseInt(document.getElementById('n1').value);
    const n2 = parseInt(document.getElementById('n2').value);

    if (isNaN(n1) || isNaN(n2)) {
        document.getElementById('sumResult').innerHTML = "Valores inválidos. Tente novamente.";
        return;
    }

    const result = sumIntegersInRange(n1, n2);
    document.getElementById('sumResult').innerHTML = "A soma dos valores inteiros de " + n1 + " até " + n2 + " é: " + result;
}
