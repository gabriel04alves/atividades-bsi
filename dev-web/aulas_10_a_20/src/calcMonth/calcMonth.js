function convertMonth() {
    const monthNumber = parseInt(document.getElementById('monthNumber').value);

    if (isNaN(monthNumber) || monthNumber < 1 || monthNumber > 12) {
        document.getElementById('monthResult').innerHTML = "Número inválido. Tente novamente com um valor entre 1 e 12.";
        return;
    }

    let monthName = "";
    switch (monthNumber) {
        case 1:
            monthName = "Janeiro";
            break;
        case 2:
            monthName = "Fevereiro";
            break;
        case 3:
            monthName = "Março";
            break;
        case 4:
            monthName = "Abril";
            break;
        case 5:
            monthName = "Maio";
            break;
        case 6:
            monthName = "Junho";
            break;
        case 7:
            monthName = "Julho";
            break;
        case 8:
            monthName = "Agosto";
            break;
        case 9:
            monthName = "Setembro";
            break;
        case 10:
            monthName = "Outubro";
            break;
        case 11:
            monthName = "Novembro";
            break;
        case 12:
            monthName = "Dezembro";
            break;
    }

    document.getElementById('monthResult').innerHTML = "O mês " + monthNumber + " é " + monthName;
}
