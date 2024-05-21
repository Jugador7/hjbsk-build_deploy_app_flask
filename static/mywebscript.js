function performOperation(operation) {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    const url = `http://localhost:8080/${operation}?num1=${encodeURIComponent(num1)}&num2=${encodeURIComponent(num2)}`;

    fetch(url)
        .then(response => response.text())
        .then(data => {
            document.getElementById('system_response').innerText = 'Result: ' + data;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('system_response').innerText = 'Error: Could not perform the operation';
        });
}
