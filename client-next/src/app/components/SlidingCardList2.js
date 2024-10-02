// components/SlidingCardList.js

"use client";

import { useEffect, useRef } from 'react';
import SlidingCard from './SlidingCard';
import './slidingCards.css';

const cardsData = [
  {
    title: 'Player Stats',
    description: 'Access detailed player stats and performance metrics.',
    image: '/images/player-stats.jpg',
  },
  {
    title: 'Team Synergy',
    description: 'Build teams based on agent roles and past performance.',
    image: '/images/team-synergy.jpg',
  },
  {
    title: 'Agent Skills',
    description: 'Analyze agent abilities and player proficiency.',
    image: '/images/agent-skills.jpg',
  },
  {
    title: 'Win Rates',
    description: 'Discover the teams with the best win rates and strategies.',
    image: '/images/win-rates.jpg',
  },
];

export default function SlidingCardList2() {
  const cardListRef = useRef(null);

  useEffect(() => {
    const cardList = cardListRef.current;
    let scrollAmount = 0;
    const cardWidth = 300 + 20; // Card width + gap

    // Function to handle the continuous scrolling
    const scrollCards = () => {
      scrollAmount += 1; // Increment to scroll right
      if (scrollAmount >= cardWidth) {
        // Move the first card to the end when it scrolls out of view
        cardList.appendChild(cardList.firstElementChild);
        scrollAmount = 0;
      }
      cardList.style.transform = `translateX(${scrollAmount}px)`; // Change direction
      requestAnimationFrame(scrollCards);
    };

    // Start the scrolling
    scrollCards();

    return () => cancelAnimationFrame(scrollCards);
  }, []);

  return (
    <div className="sliding-card-wrapper">
      <div className="sliding-card-list" ref={cardListRef}>
        {cardsData.map((card, index) => (
          <SlidingCard
            key={index}
            title={card.title}
            description={card.description}
            image={card.image}
          />
        ))}

        {/* Duplicate the cards for smoother looping */}
        {cardsData.map((card, index) => (
          <SlidingCard
            key={index + cardsData.length}
            title={card.title}
            description={card.description}
            image={card.image}
          />
        ))}
      </div>
    </div>
  );
}
