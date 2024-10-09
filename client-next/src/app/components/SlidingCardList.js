// components/SlidingCardList.js

"use client";

import { useEffect, useRef } from 'react';
import SlidingCard from './SlidingCard';
import './slidingCards.css';
import { useMotionValue } from "framer-motion";
import useMeasure from "react-use-measure";
import { motion, animate } from "framer-motion"

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

export default function SlidingCardList() {
  // const cardListRef = useRef(null);

  // useEffect(() => {
  //   const cardList = cardListRef.current;
  //   let scrollAmount = 0;
  //   const cardWidth = 300 + 20; // Card width + gap

  //   // Function to handle the continuous scrolling
  //   const scrollCards = () => {
  //     scrollAmount += 1; // Control the speed
  //     if (scrollAmount >= cardWidth) {
  //       // Move the first card to the end when it scrolls out of view
  //       cardList.appendChild(cardList.firstElementChild);
  //       scrollAmount = 0;
  //     }
  //     cardList.style.transform = `translateX(-${scrollAmount}px)`;
  //     requestAnimationFrame(scrollCards);
  //   };

  //   // Start the scrolling
  //   scrollCards();

  //   return () => cancelAnimationFrame(scrollCards);
  // }, []);

  let [ref, {width}] = useMeasure();

  const xTranslation = useMotionValue(0);

  useEffect(() => {
    let controls;
    let finalPosition = -width / 2 - 620; //620 - 2 card widths + gap
    controls = animate(xTranslation, [0, finalPosition], {
      ease: 'linear',
      duration: 25,
      repeat: Infinity,
      reapeatType: "loop",
      repeatDelay: 0,
    });
    return controls.stop;
  }, [xTranslation, width])

  return (
    <div className="sliding-card-wrapper">
      <motion.div className="sliding-card-list"  ref = {ref}/*ref={cardListRef}*/ style={{x: xTranslation}} >
        {[...cardsData, ...cardsData, ...cardsData].map((card, index) => (
          <SlidingCard
            key={index}
            title={card.title}
            description={card.description}
            image={card.image}
          />
        ))}
      </motion.div>
    </div>
  );
}
