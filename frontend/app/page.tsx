"use client"

import { useState } from "react"

import ReactMarkdown from "react-markdown"

export default function Page() {
  const [url, setUrl] = useState("")
  const [question, setQuestion] = useState("")
  const [loading, setLoading] = useState(false)

  const [showUrlInput, setShowUrlInput] =
    useState(false)

  const [messages, setMessages] = useState<
    {
      role: string
      content: string
    }[]
  >([])

  async function handleSubmit() {
    if (!url || !question || loading) {
      return
    }

    setMessages((prev) => [
      ...prev,

      {
        role: "user",
        content: question,
      },

      {
        role: "assistant",
        content: "",
      },
    ])

    setLoading(true)

    try {
      const response = await fetch(
        process.env.NEXT_PUBLIC_API_URL +
          "/chat",

        {
          method: "POST",

          headers: {
            "Content-Type":
              "application/json",
          },

          body: JSON.stringify({
            url,
            question,
          }),
        }
      )

      if (!response.body) {
        throw new Error(
          "No response body"
        )
      }

      const reader =
        response.body.getReader()

      const decoder =
        new TextDecoder()

      let finalText = ""

      while (true) {
        const { done, value } =
          await reader.read()

        if (done) {
          break
        }

        const chunk = decoder.decode(
          value || new Uint8Array()
        )

        finalText += chunk

        setMessages((prev) => {
          const updated = [...prev]

          updated[
            updated.length - 1
          ] = {
            role: "assistant",
            content: finalText,
          }

          return updated
        })
      }
    } catch (err) {
      console.error(err)

      setMessages((prev) => {
        const updated = [...prev]

        updated[
          updated.length - 1
        ] = {
          role: "assistant",
          content:
            "Failed to generate response.",
        }

        return updated
      })
    }

    setLoading(false)

    setQuestion("")
  }

  return (
  <main className="relative flex h-[100dvh] flex-col overflow-hidden bg-black text-zinc-100">
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,rgba(120,119,198,0.12),transparent_40%)]" />

      <header className="relative z-20 border-b border-zinc-900 bg-black/60 backdrop-blur-xl">
        <div className="flex h-16 items-center justify-between px-4 sm:px-6">
          <h1 className="text-xl font-semibold tracking-tight sm:text-2xl">
            Loupe
          </h1>

          <div className="flex items-center gap-2 sm:gap-3">
            {showUrlInput && (
              <div className="flex max-w-[180px] items-center overflow-hidden rounded-2xl border border-zinc-800 bg-zinc-900/80 transition focus-within:border-violet-500 sm:max-w-none">
                <input
                  type="text"
                  value={url}
                  onChange={(e) =>
                    setUrl(e.target.value)
                  }
                  placeholder="docs url"
                  className="w-32 bg-transparent px-3 py-2 text-xs outline-none sm:w-80 sm:px-4 sm:text-sm"
                />

                <button
                  onClick={() => {
                    setShowUrlInput(
                      false
                    )
                  }}
                  className="border-l border-zinc-800 px-3 py-2 text-zinc-400 transition hover:bg-zinc-800 hover:text-white"
                >
                  ↵
                </button>
              </div>
            )}

            <button
              onClick={() =>
                setShowUrlInput(
                  !showUrlInput
                )
              }
              className={`rounded-2xl border px-3 py-2 text-xs transition sm:px-4 sm:text-sm ${
                url
                  ? "border-violet-500/40 bg-violet-500/10 text-violet-300"
                  : "border-zinc-800 bg-zinc-900/70 hover:border-violet-500"
              }`}
            >
              {url
                ? "Loaded"
                : "Docs"}
            </button>
          </div>
        </div>
      </header>

      <div className="relative flex min-h-0 flex-1 flex-col overflow-hidden">
        {messages.length === 0 && (
          <div className="pointer-events-none absolute inset-0 flex items-center justify-center px-6">
            <div className="mb-24 text-center">
              <h2 className="text-3xl font-semibold tracking-tight text-zinc-200 sm:text-5xl">
                Agentic documentation
                retrieval
              </h2>

              <p className="mt-4 text-sm text-zinc-500 sm:mt-5 sm:text-lg">
                Ask questions across
                complex technical docs
              </p>
            </div>
          </div>
        )}

        <div className="relative z-10 flex-1 overflow-y-auto">
          <div className="mx-auto flex w-full max-w-5xl flex-col gap-6 px-4 py-6 sm:gap-8 sm:px-6 sm:py-10">
            {messages.map(
              (message, index) => (
                <div
                  key={index}
                  className={`flex ${
                    message.role ===
                    "user"
                      ? "justify-end"
                      : "justify-start"
                  }`}
                >
                  <div
                    className={`rounded-3xl border px-4 py-4 shadow-2xl backdrop-blur sm:px-6 sm:py-5 ${
                      message.role ===
                      "user"
                        ? "max-w-[90%] border-violet-500/20 bg-violet-600 text-white sm:max-w-2xl"
                        : "max-w-[95%] border-zinc-800 bg-zinc-900/80 sm:max-w-4xl"
                    }`}
                  >
                    {message.role ===
                    "assistant" ? (
                      <div className="prose prose-invert max-w-none text-sm leading-7 prose-headings:text-zinc-100 prose-p:text-zinc-300 prose-strong:text-white prose-code:text-violet-300 prose-pre:overflow-x-auto prose-pre:rounded-2xl prose-pre:border prose-pre:border-zinc-700 prose-pre:bg-black/70 sm:text-base sm:leading-8">
                        <ReactMarkdown>
                          {
                            message.content
                          }
                        </ReactMarkdown>

                        {loading &&
                          index ===
                            messages.length -
                              1 && (
                            <span className="animate-pulse text-violet-400">
                              ▋
                            </span>
                          )}
                      </div>
                    ) : (
                      <p className="whitespace-pre-wrap text-sm leading-7 sm:text-base sm:leading-8">
                        {
                          message.content
                        }
                      </p>
                    )}
                  </div>
                </div>
              )
            )}
          </div>
        </div>

        <div className="relative z-20 border-t border-zinc-900 bg-black/70 backdrop-blur-2xl">
          <div className="mx-auto flex w-full max-w-4xl justify-center px-3 py-4 sm:px-6 sm:py-6">
            <div className="flex w-full items-end gap-2 sm:gap-3">
              <textarea
                placeholder="Ask about the docs..."
                value={question}
                onChange={(e) =>
                  setQuestion(
                    e.target.value
                  )
                }
                rows={1}
                className="flex-1 resize-none rounded-full border border-zinc-800 bg-zinc-900/80 px-5 py-4 text-sm leading-6 outline-none transition focus:border-violet-500 sm:px-6 sm:py-5 sm:text-base"
              />

              <button
                onClick={handleSubmit}
                disabled={loading}
                className="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-violet-600 text-lg text-white transition hover:bg-violet-500 disabled:cursor-not-allowed disabled:opacity-50 sm:h-14 sm:w-14 sm:text-xl"
              >
                ↑
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>
  )
}
