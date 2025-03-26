function calculate() { // Custom function
    const cost = parseFloat(document.getElementById("cost").value); // the variable is called with a constant, which gets the input as floating, detecting the id "cost" and its value.
    const liters = parseFloat(document.getElementById("liters").value);
    
    document.getElementById('result').textContent = // gets the id "result" and adds text content the following result of cost multiplied by litres, with a decimal after two decimal points.
        `Total: $${(cost * liters).toFixed(2)}`;
}