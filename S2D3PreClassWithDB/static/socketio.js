// // Establish a connection with the server
// const socket = io();
// // Listen for 'order_status_update' event
// socket.on('order_status_update', function (data) {
//     console.log("Connected")
//     const orderElement = document.getElementById(`order-status-${data.order_id}`);
//     if (orderElement) {
//         orderElement.textContent = data.status;
//     }
// });

function updateOrderStatus(orderId) {
    const selectElement = document.getElementById('status-' + orderId);
    const newStatus = selectElement.value;

    fetch(`/order/${orderId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            status: newStatus
        })
    })
        .then(response => {
            if (response.ok) {
                alert('Order status updated successfully');
                // Refresh the page or perform any other necessary action
            } else {
                console.log(response)
                alert('Failed to update order status');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred');
        });
}