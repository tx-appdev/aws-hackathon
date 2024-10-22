// pages/chatbot.js
"use client";

import React, { useState } from 'react';
import styles from './Chatbot.module.css';
import axios from 'axios';

export default function ChatbotPage() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [chatLogs, setChatLogs] = useState([]);
  const [currentChat, setCurrentChat] = useState(''); // Tracks current chat log

  const handleSendMessage = (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { sender: 'user', text: input };
    const botResponse = generateBotResponse(input);

    const updatedMessages = [...messages, userMessage, botResponse];
    setMessages(updatedMessages);
    setChatLogs((prevLogs) => {
      const newLogs = { ...prevLogs, [currentChat]: updatedMessages };
      return newLogs;
    });
    setInput(''); // Clear the input field
  };

  const generateBotResponse = async (input) => {
    try {
      const response = await axios.post('http://localhost:5000/chat', {
        message: input,
      });
      return { sender: 'bot', text: response.data.response };
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const startNewChat = () => {
    const newChatId = `Chat ${Object.keys(chatLogs).length + 1}`;
    setCurrentChat(newChatId);
    setMessages([]); // Reset messages for new chat
  };

  const handleSelectChat = (chatId) => {
    setCurrentChat(chatId);
    setMessages(chatLogs[chatId] || []);
  };

  return (
    <div className={styles.chatbotContainer}>
      <aside className={styles.sidebar}>
        <button className={styles.newChatButton} onClick={startNewChat}>
          New Chat
        </button>
        <ul className={styles.chatLogList}>
          {Object.keys(chatLogs).map((chatId) => (
            <li
              key={chatId}
              className={styles.chatLogItem}
              onClick={() => handleSelectChat(chatId)}
            >
              {chatId}
            </li>
          ))}
        </ul>
      </aside>

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
