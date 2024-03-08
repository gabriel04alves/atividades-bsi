document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const unit = document.querySelector('#unit');
    const temperature = document.querySelector('#temperature');
    const result = document.querySelector('#result');
    
    form.addEventListener('submit', (event) => {
        event.preventDefault();
        const valueT = parseFloat(temperature.value);
        const unitSelected = unit.value;
        
        let convertedTemp;
    
        if(unitSelected === 'fahrenheit') {
            convertedTemp = (valueT - 32) * 5 / 9;
            result.textContent = `${valueT} °F são equivalentes a ${convertedTemp.toFixed(1)} °C`;
        } else {
            convertedTemp = (valueT * 9 / 5) + 32;
            result.textContent = `${valueT} °C são equivalentes a ${convertedTemp.toFixed(1)} °F`;
        }
    });
});
