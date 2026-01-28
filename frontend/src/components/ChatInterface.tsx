import React from 'react';

const ChatInterface: React.FC = () => {
    return (
        <div>
            <h1>Chat Interface</h1>
            <div className="chat-window">
                <div className="messages"></div>
                <input type="text" placeholder="Type a message..." />
                <button>Send</button>
            </div>
        </div>
    );
};

export default ChatInterface;