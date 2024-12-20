function sendMessage() {  
            
    const userInputElement = document.getElementById("userInput");  
    const userInput = userInputElement.value;  

    // Hiển thị tin nhắn của người dùng  
    const messagesDiv = document.getElementById("messages");  
    messagesDiv.innerHTML += `<div><strong>Bạn:</strong> ${userInput}</div>`;  
    userInputElement.value = '';
    // Gửi tin nhắn đến server  
    fetch('/chat', {  
        method: 'POST',  
        headers: {  
            'Content-Type': 'application/json',  
        },  
        body: JSON.stringify({ message: userInput })  
    })  
    .then(response => response.json())  
    .then(data => {  
        messagesDiv.innerHTML += `<div><strong>AI:</strong> ${data.response}</div>`;  
         // Xóa ô nhập sau khi nhận phản hồi  
    })  
    .catch(error => {  
        console.error('Lỗi:', error);  
    });  
}  

document.getElementById("sendButton").addEventListener("click", sendMessage);  

// Thêm sự kiện lắng nghe phím Enter  
document.getElementById("userInput").addEventListener("keypress", function(event) {  
    if (event.key === "Enter") {  
        event.preventDefault(); // Ngăn chặn hành động mặc định của phím Enter  
        sendMessage(); // Gọi hàm gửi tin nhắn khi nhấn Enter  
    }  
});  


function w(){
    alert("hiiii")
}