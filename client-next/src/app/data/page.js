import Link from 'next/link';

export default function HomePage() {
  return (
    <section>
      <h1>Welcome to the Esports Manager</h1>
      <p>Your AI-powered assistant for VALORANT esports team building and scouting.</p>
      <Link href="/intro">
        <button>Get Started</button>
      </Link>
    </section>
  );
}
