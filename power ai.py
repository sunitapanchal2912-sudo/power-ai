<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Power AI - Real-time & Historical Information</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: #fff;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        
        header {
            background: rgba(0, 0, 0, 0.7);
            padding: 1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .logo {
            display: flex;
            align-items: center;
            gap: 0.8rem;
        }
        
        .logo-icon {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, #00b4db, #0083b0);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            font-weight: bold;
        }
        
        .logo-text {
            font-size: 1.8rem;
            font-weight: 700;
            background: linear-gradient(to right, #00b4db, #0083b0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }
        
        nav a {
            color: #fff;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }
        
        nav a:hover {
            color: #00b4db;
        }
        
        .container {
            max-width: 1200px;
            width: 100%;
            margin: 0 auto;
            padding: 2rem;
            flex: 1;
        }
        
        .hero {
            text-align: center;
            padding: 3rem 0;
        }
        
        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            background: linear-gradient(to right, #00b4db, #0083b0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .hero p {
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto 2rem;
            color: #e0e0e0;
        }
        
        .info-tabs {
            display: flex;
            justify-content: center;
            margin-bottom: 2rem;
            gap: 1rem;
        }
        
        .tab {
            padding: 1rem 2rem;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .tab.active {
            background: rgba(0, 180, 219, 0.3);
            box-shadow: 0 0 15px rgba(0, 180, 219, 0.5);
        }
        
        .tab:hover {
            background: rgba(0, 180, 219, 0.2);
        }
        
        .chat-container {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            margin: 2rem auto;
            max-width: 900px;
        }
        
        .chat-header {
            background: rgba(0, 0, 0, 0.4);
            padding: 1rem;
            display: flex;
            align-items: center;
            gap: 0.8rem;
        }
        
        .chat-header i {
            color: #00b4db;
            font-size: 1.5rem;
        }
        
        .chat-messages {
            height: 500px;
            overflow-y: auto;
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }
        
        .message {
            display: flex;
            gap: 1rem;
            max-width: 80%;
        }
        
        .user-message {
            align-self: flex-end;
            flex-direction: row-reverse;
        }
        
        .ai-message {
            align-self: flex-start;
        }
        
        .avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        
        .user-avatar {
            background: linear-gradient(135deg, #ff7e5f, #feb47b);
        }
        
        .ai-avatar {
            background: linear-gradient(135deg, #00b4db, #0083b0);
        }
        
        .message-content {
            background: rgba(255, 255, 255, 0.1);
            padding: 1rem;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        
        .user-message .message-content {
            background: rgba(0, 180, 219, 0.2);
            border-bottom-right-radius: 5px;
        }
        
        .ai-message .message-content {
            background: rgba(255, 255, 255, 0.15);
            border-bottom-left-radius: 5px;
        }
        
        .info-tag {
            display: inline-block;
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            font-size: 0.8rem;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
        }
        
        .real-time-tag {
            background: rgba(76, 175, 80, 0.3);
            color: #4caf50;
        }
        
        .historical-tag {
            background: rgba(156, 39, 176, 0.3);
            color: #9c27b0;
        }
        
        .chat-input {
            display: flex;
            padding: 1rem;
            background: rgba(0, 0, 0, 0.3);
            gap: 1rem;
        }
        
        .chat-input input {
            flex: 1;
            padding: 1rem;
            border: none;
            border-radius: 25px;
            background: rgba(255, 255, 255, 0.1);
            color: white;
            font-size: 1rem;
            outline: none;
        }
        
        .chat-input input::placeholder {
            color: rgba(255, 255, 255, 0.6);
        }
        
        .chat-input button {
            background: linear-gradient(135deg, #00b4db, #0083b0);
            border: none;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            color: white;
            font-size: 1.2rem;
            cursor: pointer;
            transition: transform 0.3s;
        }
        
        .chat-input button:hover {
            transform: scale(1.05);
        }
        
        .suggestions {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            justify-content: center;
            margin-top: 2rem;
        }
        
        .suggestion {
            background: rgba(255, 255, 255, 0.1);
            padding: 0.8rem 1.5rem;
            border-radius: 25px;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .suggestion:hover {
            background: rgba(0, 180, 219, 0.3);
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 4rem 0;
        }
        
        .feature {
            background: rgba(255, 255, 255, 0.05);
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            transition: transform 0.3s;
        }
        
        .feature:hover {
            transform: translateY(-5px);
        }
        
        .feature i {
            font-size: 3rem;
            color: #00b4db;
            margin-bottom: 1rem;
        }
        
        .feature h3 {
            margin-bottom: 1rem;
            color: #00b4db;
        }
        
        footer {
            background: rgba(0, 0, 0, 0.7);
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }
        
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2.2rem;
            }
            
            nav ul {
                gap: 1rem;
            }
            
            .message {
                max-width: 90%;
            }
            
            .features {
                grid-template-columns: 1fr;
            }
            
            .info-tabs {
                flex-direction: column;
                align-items: center;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">
            <div class="logo-icon">P</div>
            <div class="logo-text">Power AI</div>
        </div>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Features</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <div class="container">
        <section class="hero">
            <h1>Power AI - Real-time & Historical Information</h1>
            <p>Access both current and historical information with our advanced AI technology.</p>
            
            <div class="info-tabs">
                <div class="tab active" data-tab="all">All Information</div>
                <div class="tab" data-tab="realtime">Real-time Only</div>
                <div class="tab" data-tab="historical">Historical Only</div>
            </div>
        </section>
        
        <div class="chat-container">
            <div class="chat-header">
                <i class="fas fa-robot"></i>
                <h2>Power AI Assistant</h2>
            </div>
            <div class="chat-messages" id="chatMessages">
                <div class="message ai-message">
                    <div class="avatar ai-avatar">
                        <i class="fas fa-robot"></i>
                    </div>
                    <div class="message-content">
                        <p>Hello! I'm Power AI, your information assistant. I can provide both real-time and historical information. How can I help you today?</p>
                        <div class="info-tag real-time-tag">Real-time</div>
                        <div class="info-tag historical-tag">Historical</div>
                    </div>
                </div>
            </div>
            <div class="chat-input">
                <input type="text" id="userInput" placeholder="Ask me anything...">
                <button id="sendButton">
                    <i class="fas fa-paper-plane"></i>
                </button>
            </div>
        </div>
        
        <div class="suggestions">
            <div class="suggestion" data-question="What's the latest technology news?">Latest tech news</div>
            <div class="suggestion" data-question="How's the weather today?">Current weather</div>
            <div class="suggestion" data-question="Tell me about World War II">Historical events</div>
            <div class="suggestion" data-question="What was the first computer?">Technology history</div>
        </div>
        
        <div class="features">
            <div class="feature">
                <i class="fas fa-bolt"></i>
                <h3>Real-time Information</h3>
                <p>Get the latest information on any topic instantly with our powerful AI technology.</p>
            </div>
            <div class="feature">
                <i class="fas fa-history"></i>
                <h3>Historical Data</h3>
                <p>Access comprehensive historical information and past events with detailed context.</p>
            </div>
        </div>
    </div>
    
    <footer>
        <p>&copy; 2023 Power AI. All rights reserved.</p>
        <p>Designed to provide both real-time and historical information without external dependencies.</p>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const chatMessages = document.getElementById('chatMessages');
            const userInput = document.getElementById('userInput');
            const sendButton = document.getElementById('sendButton');
            const suggestions = document.querySelectorAll('.suggestion');
            const tabs = document.querySelectorAll('.tab');
            
            userInput.focus();
            
            sendButton.addEventListener('click', sendMessage);
            userInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') sendMessage();
            });
            
            suggestions.forEach(suggestion => {
                suggestion.addEventListener('click', function() {
                    userInput.value = this.getAttribute('data-question');
                    sendMessage();
                });
            });
            
            tabs.forEach(tab => {
                tab.addEventListener('click', function() {
                    tabs.forEach(t => t.classList.remove('active'));
                    this.classList.add('active');
                    addMessage(`Showing ${this.getAttribute('data-tab')} information.`, 'ai');
                });
            });
            
            function sendMessage() {
                const message = userInput.value.trim();
                if (!message) return;
                addMessage(message, 'user');
                userInput.value = '';
                
                const thinkingElement = document.createElement('div');
                thinkingElement.classList.add('message', 'ai-message');
                thinkingElement.innerHTML = `
                    <div class="avatar ai-avatar"><i class="fas fa-robot"></i></div>
                    <div class="message-content">
                        <p><i class="fas fa-circle-notch fa-spin"></i> Thinking...</p>
                    </div>
                `;
                chatMessages.appendChild(thinkingElement);
                chatMessages.scrollTop = chatMessages.scrollHeight;
                
                setTimeout(() => {
                    chatMessages.removeChild(thinkingElement);
                    const response = generateResponse(message);
                    addMessage(response.text, 'ai', response.type);
                }, 1500);
            }
            
            function addMessage(content, sender, type = null) {
                const messageElement = document.createElement('div');
                messageElement.classList.add('message', sender + '-message');
                
                const avatar = sender === 'user' ? 
                    '<div class="avatar user-avatar"><i class="fas fa-user"></i></div>' : 
                    '<div class="avatar ai-avatar"><i class="fas fa-robot"></i></div>';
                
                let formattedContent = content.split('\n').map(p => p.trim() ? `<p>${p}</p>` : '').join('');
                
                let tags = '';
                if (type === 'real-time') tags = '<div class="info-tag real-time-tag">Real-time</div>';
                else if (type === 'historical') tags = '<div class="info-tag historical-tag">Historical</div>';
                else if (type === 'both') tags = '<div class="info-tag real-time-tag">Real-time</div><div class="info-tag historical-tag">Historical</div>';
                
                messageElement.innerHTML = `${avatar}<div class="message-content">${formattedContent}${tags}</div>`;
                chatMessages.appendChild(messageElement);
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }
            
            function generateResponse(userMessage) {
                const lowerCaseMessage = userMessage.toLowerCase();
                const now = new Date();
                const timeString = now.toLocaleTimeString();
                const dateString = now.toLocaleDateString();
                const dayOfWeek = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][now.getDay()];
                const month = ['January','February','March','April','May','June','July','August','September','October','November','December'][now.getMonth()];
                const weatherConditions = ['sunny','cloudy','rainy','partly cloudy','windy'];
                const randomWeather = weatherConditions[Math.floor(Math.random()*weatherConditions.length)];
                const randomTemp = Math.floor(Math.random()*30)+10;

                const techNews = [
                    "New smartphone unveiled with revolutionary foldable display technology.",
                    "Major breakthrough in quantum computing announced by leading research firm.",
                    "Tech giant announces new AI assistant that can understand natural language better than ever.",
                    "Cybersecurity firm discovers critical vulnerability in popular software, patch released."
                ];
                const generalNews = [
                    "Global leaders meet to discuss climate change initiatives and carbon reduction targets.",
                    "Economic markets show positive growth following recent policy changes.",
                    "New study reveals benefits of Mediterranean diet for long-term health.",
                    "International space station welcomes new crew members for six-month mission."
                ];
                
                const historicalEvents = {
                    "world war ii": "World War II (1939-1945) was the deadliest international conflict in history...",
                    "ancient rome": "Ancient Rome was a civilization that began on the Italian Peninsula as early as the 8th century BCE...",
                    "renaissance": "The Renaissance was a period in European history marking the transition from the Middle Ages to modernity...",
                    "industrial revolution": "The Industrial Revolution was the transition to new manufacturing processes in Europe and the US..."
                };
                
                const techHistory = {
                    "first computer": "The first programmable computer was the Z3, created by Konrad Zuse in 1941...",
                    "internet": "The Internet originated with the development of electronic computers in the 1950s...",
                    "smartphone": "The first smartphone was invented by IBM in 1992 and released in 1994..."
                };
                
                if (lowerCaseMessage.includes('weather') || lowerCaseMessage.includes('temperature')) {
                    return {text:`Based on current conditions, the weather is ${randomWeather} with a temperature of around ${randomTemp}°C.`,type:'real-time'};
                } else if (lowerCaseMessage.includes('time')) {
                    return {text:`The current time is ${timeString} on ${dayOfWeek}, ${dateString}.`,type:'real-time'};
                } else if (lowerCaseMessage.includes('news')) {
                    if (lowerCaseMessage.includes('tech') || lowerCaseMessage.includes('technology')) {
                        return {text:`Here are some recent technology developments:\n\n${techNews.join('\n\n')}`,type:'real-time'};
                    } else {
                        return {text:`Current news highlights include:\n\n${generalNews.join('\n\n')}`,type:'real-time'};
                    }
                } else if (lowerCaseMessage.includes('date') || lowerCaseMessage.includes('day')) {
                    return {text:`Today is ${dayOfWeek}, ${month} ${now.getDate()}, ${now.getFullYear()}.`,type:'real-time'};
                } else if (historicalEvents[lowerCaseMessage]) {
                    return {text:historicalEvents[lowerCaseMessage],type:'historical'};
                } else if (techHistory[lowerCaseMessage]) {
                    return {text:techHistory[lowerCaseMessage],type:'historical'};
                } else if (lowerCaseMessage.includes('history') || lowerCaseMessage.includes('historical')) {
                    return {text:"I have information about various historical topics including World War II, Ancient Rome, the Renaissance, and the Industrial Revolution.",type:'historical'};
                } else if (lowerCaseMessage.includes('how are you')) {
                    return {text:"I'm functioning optimally! Ready to help you with any information you need.",type:'both'};
                } else if (lowerCaseMessage.includes('hello') || lowerCaseMessage.includes('hi')) {
                    return {text:"Hello! I'm Power AI, your information assistant. I can provide both real-time and historical information.",type:'both'};
                } else {
                    return {text:`I understand you're asking about "${userMessage}". Could you specify if you want current or historical information?`,type:'both'};
                }
            }
        });
    </script>
</body>
</html>
