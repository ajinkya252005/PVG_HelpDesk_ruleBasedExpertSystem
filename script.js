// Get references to DOM elements
const chatBox = document.getElementById('chat-box');
const questionInput = document.getElementById('question-input');
const askButton = document.getElementById('ask-button');
const backendUrl = 'http://127.0.0.1:5000/ask';

// Wait for the HTML document to be fully loaded before adding event listeners
document.addEventListener('DOMContentLoaded', () => {
    // Add event listeners
    askButton.addEventListener('click', askQuestion);
    questionInput.addEventListener('keypress', handleKeyPress);
});

// Function to handle the Enter key press
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        askQuestion();
    }
}

// Function to display a message in the chat box
function displayMessage(message, sender = 'bot', className = '') {
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message');
    
    if (sender === 'user') {
        messageElement.classList.add('user-message');
    } else {
        messageElement.classList.add('bot-message');
    }
    
    // Only add the extra class if it is not an empty string
    if (className) {
        messageElement.classList.add(className);
    }
    
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Main function to handle the interaction
async function askQuestion() {
    // --- DEBUGGING STEP: Check if this message appears in the console ---
    console.log("Button clicked, attempting to ask question...");
    
    const question = questionInput.value.trim();
    if (question === '') {
        return; // Do nothing if the input is empty
    }
    
    displayMessage(question, 'user');
    questionInput.value = ''; // Clear the input field

    // Handle "hi" and "bye" on the client side for faster response
    const lowerCaseQuestion = question.toLowerCase();
    if (lowerCaseQuestion === 'hi' || lowerCaseQuestion === 'hello') {
        displayMessage("Hello! How can I help you today?");
        return;
    } else if (lowerCaseQuestion === 'bye' || lowerCaseQuestion === 'goodbye') {
        displayMessage("Goodbye! Have a great day.");
        return;
    }

    // Show a loading message
    const loadingMessageElement = document.createElement('div');
    loadingMessageElement.classList.add('chat-message', 'bot-message', 'loading-message');
    loadingMessageElement.textContent = 'Thinking...';
    chatBox.appendChild(loadingMessageElement);
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        // Send the question to the Flask backend
        const response = await fetch(backendUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: question }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        // Remove the loading message and display the bot's answer
        chatBox.removeChild(loadingMessageElement);
        displayMessage(data.answer, 'bot');

    } catch (error) {
        // Remove the loading message and display an error message
        chatBox.removeChild(loadingMessageElement);
        displayMessage('An error occurred. Please try again.', 'bot');
        console.error('Error fetching data:', error);
    }
}
