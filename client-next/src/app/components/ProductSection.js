import React from 'react';
import './ProductSection.css';

const ProductSection = ({ title, description, video, imageLeft = true }) => {
  return (
    <div className="product-section">
      <div className={`content-container ${imageLeft ? 'image-left' : 'image-right'}`}>
        {/*Video Section */}
        <div className="image-container">
          <video className="product-video"src={video} autoPlay muted loop />
        </div>

        {/* Text Section */}
        <div className="text-container">
          <h2 className="product-title">{title}</h2>
          <p className="product-description">{description}</p>
        </div>
      </div>
    </div>
  );
};

export default ProductSection;

