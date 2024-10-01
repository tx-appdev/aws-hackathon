import "../globals.css";

export const metadata = {
  title: "VCT Hackathon",
  description: "LLM-Powered Esports Assistant for VCT Hackathon 2024",
};

export default function IntroLayout({ children }) {
  return (
    <div>
      <main>{children}</main>
    </div>
  );
}
