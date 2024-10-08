// pages/chatbot.js
"use client";

import React, { useState } from 'react';
import styles from './Chatbot.css';

export default function ChatbotPage() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSendMessage = (e) => {
    e.preventDefault();
    if (!input.trim()) return; // Ignore empty input

    const userMessage = { sender: 'user', text: input };
    const botResponse = generateBotResponse(input);

    setMessages([...messages, userMessage, botResponse]);
    setInput(''); // Clear the input field
  };

  const generateBotResponse = (input) => {
    // Basic bot response logic (you can improve this)
    const botReplies = [
      "I'm here to help!",
      'Tell me more.',
      'How can I assist you today?',
      'I can answer your questions!',
    ];

    const randomReply =
      botReplies[Math.floor(Math.random() * botReplies.length)];
    return { sender: 'bot', text: randomReply };
  };

  return (
    <div className={styles.chatbotPage}>
      <div className={styles.chatWindow}>
        <div className={styles.messages}>
          {messages.map((msg, index) => (
            <div
              key={index}
              className={msg.sender === 'user' ? styles.userMessage : styles.botMessage}
            >
              {msg.text}
            </div>
          ))}
        </div>
        <form onSubmit={handleSendMessage} className={styles.inputContainer}>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type a message..."
            className={styles.messageInput}
          />
          <button type="submit" className={styles.sendButton}>
            Send
          </button>
        </form>
      </div>
    </div>
  );
}
