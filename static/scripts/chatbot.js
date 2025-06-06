document.addEventListener('DOMContentLoaded', function () {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let chatHistory = [];

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const message = userInput.value.trim();
        if (!message) return;

        // 사용자 메시지
        addMessage(message, 'user');
        userInput.value = '';

        // 로딩 메시지
        const loadingMessage = addMessage('답변 생성 중...', 'bot');

        // 누적대화
        const historyText = chatHistory.map(turn =>
            `사용자: ${turn.q}\nAI: ${turn.a}`
        ).join("\n");

        const historyPrompt = `
[이전 대화]
${historyText}

[질문]
${message}
`;

        try {
            const response = await fetch(chatForm.dataset.apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                // body: JSON.stringify({ prompt: message })
                body: JSON.stringify({ prompt: historyPrompt })
            });

            const data = await response.json();
            loadingMessage.textContent = data.response;
            chatHistory.push({ q: message, a: data.response });
        } catch (error) {
            loadingMessage.textContent = '오류가 발생했습니다.';
        }

        chatBox.scrollTop = chatBox.scrollHeight;
    });

    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `chat-message ${sender}`;
        messageDiv.textContent = text;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
        return messageDiv;
    }
});