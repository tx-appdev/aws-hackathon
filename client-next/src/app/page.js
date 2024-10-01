import SlidingCardList from './components/SlidingCardList';
import SlidingCardList2 from './components/SlidingCardList2';
import './styles.css';

export default function Home() {
  return (
    <section className="intro-page">
      <div className="title">
        <h1>VALORANT Esports Manager</h1>
        <p>Build the best VALORANT team with AI-assisted analysis and scouting</p>
        
        {/* Start Now Button */}
        <a href="/data" className="start-button">Start Now</a>
      </div>
      
      <SlidingCardList />
      <SlidingCardList2 />
      <SlidingCardList />
      
      <div className="body"></div>
    </section>
  );
}
