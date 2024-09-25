import "./globals.css";

export const metadata = {
  title: "VCT Hackathon",
  description: "LLM model for VCT Hackathon 2024",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
