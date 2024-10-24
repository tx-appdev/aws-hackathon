import "./globals.css";
import Footer from './components/Footer';
import Menu from './components/Menu/menu';

import SmoothScroll from "./components/SmoothScroll";

export const metadata = {
  title: "VCT X AWS Hackathon",
  description: "LLM-Powered Esports Assistant for VCT X AWS Hackathon 2024",
};

export default function RootLayout({ children }) {
  return (
    <SmoothScroll>
      <html lang="en">
        <body>
          <Menu />
          <main>{children}</main>
          <Footer />
        </body>
      </html>
    </SmoothScroll>
  );
}
