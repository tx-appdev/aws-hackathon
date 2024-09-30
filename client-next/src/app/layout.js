import "./globals.css";
import Header from './components/Header';
import Footer from './components/Footer';

export const metadata = {
  title: "VCT Hackathon",
  description: "LLM-Powered Esports Assistant for VCT Hackathon 2024",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <Header />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
