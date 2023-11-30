import React, {useState} from "react";
import './HamburgerMenu.css';

const HamburgerMenu = () => {
    const [isOpen, setIsOpen] = useState(false);

    const toggleMenu = () => {
        setIsOpen(!isOpen);
    }

    return (
        <div className="hamburger-menu">
          <div className={`menu-icon ${isOpen ? 'open' : ''}`} onClick={toggleMenu}>
            <div className="bar1"></div>
            <div className="bar2"></div>
            <div className="bar3"></div>
          </div>
          {isOpen && (
            <div className="menu-links">
              <a href="/parks">Parks</a>
              <a href="/neighborhoods">Neighborhoods</a>
              <a href="/amenities">Amenities</a>
            </div>
          )}
        </div>
      );
}

export default HamburgerMenu