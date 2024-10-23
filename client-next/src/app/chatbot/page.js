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

  const handleSendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;
  
    const userMessage = { sender: 'user', text: input };
    setMessages((prevMessages) => [...prevMessages, userMessage]); // Add user message first
  
    try {
      const botResponse = await generateBotResponse(input); // Wait for bot response
      await typeBotMessage(botResponse.text); // Call the typing function
    } catch (error) {
      console.error("Error in bot response:", error);
    }
  
    setInput(''); // Clear the input field
  };
  
  const typeBotMessage = async (messageText) => {
    // Create an empty message for the bot first
    const botMessage = { sender: 'bot', text: '' };
    setMessages((prevMessages) => [...prevMessages, botMessage]); // Add the empty bot message
  
    for (let i = 0; i < messageText.length; i++) {
      await new Promise((resolve) => setTimeout(resolve, 10)); // Typing speed (50ms per letter)
  
      setMessages((prevMessages) => {
        // Create a new array to avoid modifying the original array directly
        const updatedMessages = [...prevMessages];
  
        // Get the last message (the bot message being typed)
        const lastMessage = { ...updatedMessages[updatedMessages.length - 1] };
  
        if (lastMessage.sender === 'bot') {
          // Append the next character
          lastMessage.text += messageText[i];
          updatedMessages[updatedMessages.length - 1] = lastMessage; // Update the last message in the array
        }
  
        return updatedMessages;
      });
    }
  };

  const generateBotResponse = async (input) => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/chat', {
        query: input, // Changed "message" to "query"
      });
      return { sender: 'bot', text: response.data.response };
    } catch (error) {
      console.error("Error fetching data: ", error);
      return { sender: 'bot', text: "Sorry, something went wrong." }; // Fallback response
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
