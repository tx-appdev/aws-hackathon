import SlidingCardList from '../components/SlidingCardList';
import SlidingCardList2 from '../components/SlidingCardList2';
import './intro.css';

export default function IntroPage() {
  return (  
    <div className="container">
      <div className="video-wrapper">
        <video width="100vw" height="100vh" autoPlay muted loop className="background-clip">
          <source src="/background-vid.mp4" type="video/mp4" controls />
          Your browser does not support the video tag.
        </video>
      </div>

      <div className="intro-page">
        <div className="title">
          <h1>VALORANT Esports Manager</h1>
          <p>Build the best VALORANT team with AI-assisted analysis and scouting.</p>
        </div>
        <SlidingCardList />
        <SlidingCardList2 />
        <SlidingCardList />
        <div className="body">

        </div>
      </div>
    </div>
  );
}
