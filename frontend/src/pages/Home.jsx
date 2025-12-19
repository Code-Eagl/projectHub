import { useState } from "react";

const API_URL = import.meta.env.VITE_API_URL;

export default function Home() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const checkNews = async () => {
    if (!text.trim()) return;

    setLoading(true);
    const res = await fetch(`${API_URL}/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    const data = await res.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Fake News Detection</h1>

      <textarea
        placeholder="Paste news article here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <button onClick={checkNews}>
        {loading ? "Checking..." : "Check News"}
      </button>

      {result && (
        <div className="result">
          <h2>The News is: {result.label}</h2>
          <p>Fake Probability: {result.fake_probability}%</p>
          <p>Real Probability: {result.real_probability}%</p>
        </div>
      )}
    </div>
  );
}
