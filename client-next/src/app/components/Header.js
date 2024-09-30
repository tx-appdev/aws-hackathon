import Link from 'next/link'; // Import the Link component
import "./header.css"; // Import your CSS styles

export default function Header() {
  return (
    <header className="header">
      <div className="header-container">
        <h1>Esports Manager</h1>
        <nav>
          <Link href="/" className="nav-link">Home</Link>
          <Link href="/intro" className="nav-link">Intro</Link>
        </nav>
      </div>
    </header>
  );
}
