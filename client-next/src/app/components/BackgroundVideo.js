import videoSrc from "../public/background-vid.mp4";
import "./backgroundVideo.css";

const BackgroundVideo = () => {
    return ( 
        <div className="video-wrapper">
            <video src={videoSrc} autoPlay muted loop />
        </div>
     );
}
 
export default BackgroundVideo;