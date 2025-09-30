import React, { useState } from "react";

export default function Home() {
  const [text, setText] = useState("");
  const [sentiment, setSentiment] = useState(null);
  const [loading, setLoading] = useState(false);
  const API = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

  const handleAnalyze = async () => {
    if (!text.trim()) return;
    setLoading(true);
    setSentiment(null);
    try {
      const res = await fetch(`${API}/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      const data = await res.json();
      setSentiment(data.sentiment);
    } catch (e) {
      console.error(e);
      setSentiment("Erreur: impossible de joindre l'API");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Analyse de Sentiment</h1>
      <textarea value={text} onChange={(e) => setText(e.target.value)} placeholder="Tape ton texte..." />
      <button onClick={handleAnalyze} disabled={loading}>{loading ? "Analyse..." : "Analyser"}</button>
      {sentiment && <div className="result">Résultat : <strong>{sentiment}</strong></div>}
    </div>
  );
}
