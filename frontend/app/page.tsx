"use client";

import { useState } from "react";
import { Send, Sparkles } from "lucide-react";

type Message = {
  role: "user" | "assistant";
  content: string;
};

export default function HomePage() {

  const [url, setUrl] = useState("");

  const [input, setInput] = useState("");

  const [loading, setLoading] = useState(false);

  const [messages, setMessages] = useState<Message[]>([]);

  async function sendMessage() {

    if (!input.trim()) return;

    const question = input;

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: question,
      },
    ]);

    setInput("");

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

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            data.answer ||
            "No answer returned.",
        },
      ]);

    } catch {

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "Failed to contact backend.",
        },
      ]);

    } finally {

      setLoading(false);

    }
  }

  return (

    <main
      className="
        h-screen
        bg-black
        text-white
        flex
        flex-col
      "
    >

      {/* Header */}

      <div
        className="
          border-b
          border-zinc-800
          px-4
          md:px-8
          py-5
          flex
          items-center
          justify-between
        "
      >

        <div className="flex items-center gap-4">

          <div
            className="
              h-12
              w-12
              rounded-2xl
              bg-violet-600
              flex
              items-center
              justify-center
              text-xl
              font-bold
            "
          >
            L
          </div>

          <div>

            <h1 className="text-2xl font-bold">
              Loupe
            </h1>

            <p className="text-sm text-zinc-500">
              Agentic Link RAG
            </p>

          </div>

        </div>

      </div>

      {/* URL Input */}

      <div
        className="
          border-b
          border-zinc-800
          px-4
          md:px-8
          py-4
        "
      >

        <div className="max-w-5xl mx-auto">

          <input
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Paste webpage URL..."
            className="
              w-full
              rounded-2xl
              border
              border-zinc-800
              bg-zinc-900
              px-5
              py-4
              outline-none
              placeholder:text-zinc-500
              focus:border-violet-500
              transition
            "
          />

        </div>

      </div>

      {/* Chat Area */}

      <div
        className="
          flex-1
          overflow-y-auto
          px-4
          py-8
        "
      >

        {messages.length === 0 ? (

          <div
            className="
              h-full
              flex
              items-center
              justify-center
            "
          >

            <div
              className="
                max-w-3xl
                text-center
              "
            >

              <div
                className="
                  mx-auto
                  mb-8
                  h-20
                  w-20
                  rounded-3xl
                  bg-violet-600/20
                  border
                  border-violet-500/20
                  flex
                  items-center
                  justify-center
                "
              >
                <Sparkles className="h-10 w-10 text-violet-400" />
              </div>

              <h2
                className="
                  text-4xl
                  md:text-7xl
                  font-bold
                  leading-tight
                  mb-6
                "
              >
                Ask anything
                about a webpage
              </h2>

              <p
                className="
                  text-zinc-500
                  text-base
                  md:text-xl
                  leading-8
                "
              >
                Loupe extracts, retrieves and answers
                questions grounded in webpage content.
              </p>

            </div>

          </div>

        ) : (

          <div
            className="
              mx-auto
              flex
              max-w-5xl
              flex-col
              gap-6
            "
          >

            {messages.map((message, index) => (

              <div
                key={index}
                className={`
                  flex
                  ${message.role === "user"
                    ? "justify-end"
                    : "justify-start"}
                `}
              >

                <div
                  className={`
                    max-w-[90%]
                    md:max-w-[75%]
                    rounded-3xl
                    px-5
                    py-4
                    leading-8
                    whitespace-pre-wrap
                    text-sm
                    md:text-base
                    ${
                      message.role === "user"
                        ? "bg-violet-600 text-white"
                        : "bg-zinc-900 border border-zinc-800 text-zinc-100"
                    }
                  `}
                >
                  {message.content}
                </div>

              </div>

            ))}

            {loading && (

              <div className="flex justify-start">

                <div
                  className="
                    rounded-3xl
                    border
                    border-zinc-800
                    bg-zinc-900
                    px-5
                    py-4
                    text-zinc-400
                  "
                >
                  Thinking...
                </div>

              </div>

            )}

          </div>

        )}

      </div>

      {/* Input */}

      <div
        className="
          border-t
          border-zinc-800
          px-4
          md:px-8
          py-5
        "
      >

        <div
          className="
            mx-auto
            flex
            max-w-5xl
            gap-4
          "
        >

          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask anything..."
            rows={2}
            className="
              flex-1
              resize-none
              rounded-3xl
              border
              border-zinc-800
              bg-zinc-900
              px-5
              py-4
              outline-none
              placeholder:text-zinc-500
              focus:border-violet-500
              transition
            "
          />

          <button
            onClick={sendMessage}
            disabled={loading}
            className="
              h-14
              w-14
              shrink-0
              rounded-2xl
              bg-violet-600
              hover:bg-violet-500
              transition
              flex
              items-center
              justify-center
            "
          >
            <Send size={18} />
          </button>

        </div>

      </div>

    </main>
  );
}
