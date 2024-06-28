document.addEventListener('DOMContentLoaded', () => {
    const input = document.querySelector('.text');
    const button = document.querySelector('.btn');

    button.addEventListener('click', () => {
        const fetchResponse = async () => {
            const message = input.value;
            const csrfToken = document.getElementById('csrfToken').value; // Get token from hidden field

            const response = await fetch("/response", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken, // Include CSRF token in header
                },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();
            return data.response;
        };

        fetchResponse().then(response => {
            alert(response); // Display response in alert box
        }).catch(error => {
            console.error('Error:', error);
        });
    });
});

