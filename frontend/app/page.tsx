"use client";

import { useState } from "react";

export default function HomePage() {

  const [url, setUrl] = useState("");
  const [question, setQuestion] = useState("");

  const [loading, setLoading] = useState(false);

  const [chunks, setChunks] = useState<string[]>([]);

  async function askQuestion() {

    setLoading(true);

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/chat",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({
            url,
            question,
          }),
        }
      );

      const data = await response.json();

      setChunks(data.chunks || []);

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);

    }
  }

  return (
    <main className="min-h-screen p-10 flex flex-col gap-6">

      <h1 className="text-4xl font-bold">
        Loupe
      </h1>

      <input
        className="border p-3 rounded-lg"
        placeholder="Enter URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />

      <textarea
        className="border p-3 rounded-lg"
        placeholder="Ask a question"
        rows={4}
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button
        onClick={askQuestion}
        className="bg-black text-white rounded-lg px-6 py-3"
      >
        {loading ? "Loading..." : "Ask"}
      </button>

      <div className="flex flex-col gap-4">

        {chunks.map((chunk, index) => (
          <div
            key={index}
            className="border rounded-lg p-4"
          >
            {chunk}
          </div>
        ))}

      </div>

    </main>
  );
}
