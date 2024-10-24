import SlidingCardList from './components/SlidingCardList';
import SlidingCardList2 from './components/SlidingCardList2';
import BackgroundVideo from './components/BackgroundVideo';
import ProductSection from './components/ProductSection.js';
import homePageSrc from "./public/homePage.mp4";
import menuSrc from "./public/menu.mp4";
import chatPageSrc from "./public/chatPage.mp4";
import Link from 'next/link'; // Import the Link component
import './styles.css';

export default function HomePage() {
  return (
    <section className="intro-page">
      <BackgroundVideo />
      <div className="title">
        <h1>VALORANT Esports Manager</h1>
        <p>Build the best VALORANT team with AI-assisted analysis and scouting</p>
        
        {/* Start Now Button */}
        <Link href="/chatbot" className="nav-link">
        <button className="btn btn--light">
          <span className="btn__inner">
            <span className="btn__slide"></span>
            <span className="btn__content">
            START NOW
              </span>
          </span>
        </button>
        </Link>
      </div>
      
      <SlidingCardList />
      <SlidingCardList2 />
      <SlidingCardList />
      
      <div className="body"></div>
      <ProductSection 
        title="AI-Powered Insights"
        description="Leverage AI to analyze player performace and get personalized insights for professional VALORANT teams."
        video= {homePageSrc}
        imageLeft={true}  // Set to false if you want the image on the right
      />
      <ProductSection 
        title="Intuitive Layout"
        description="Navigate our next-gen digital assistant with a seamless user experience."
        video= {menuSrc}
        imageLeft={false}  // Set to false if you want the image on the right
      />
      <ProductSection 
        title="Next-Gen Optimization"
        description="Create professional teams that break the meta and provide a competitve edge."
        video= {chatPageSrc}
        imageLeft={true}  // Set to false if you want the image on the right
      />
    </section>
  );
}
