function calcHypo() {
    var side1 = parseFloat(document.getElementById('side1').value);
    var side2 = parseFloat(document.getElementById('side2').value);

    if (isNaN(side1) || isNaN(side2)) {
        document.getElementById('hypoResult').innerHTML = "O valor digitado é inválido.";
    } else {
        var hypo = Math.sqrt(side1 * side1 + side2 * side2);
        document.getElementById('hypoResult').innerHTML = "O valor da hipotenusa é: " + hypo.toFixed(2);
    }
}
