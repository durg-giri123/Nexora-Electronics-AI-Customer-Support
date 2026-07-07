import { useEffect, useRef } from "react";
import Message from "./Message";

const suggestions = [
  "Recommend a laptop for students",
  "How can I claim my warranty?",
  "How can I download my invoice?",
  "My laptop is overheating.",
  "How long does shipping take?"
];

function ChatBox({ messages, loading, onSuggestionClick }) {

  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  if (messages.length === 0) {

    return (

      <div className="flex flex-1 items-center justify-center px-6">

        <div className="text-center">

          <h2 className="mb-4 text-5xl font-bold text-white">
            🤖 Nexora AI
          </h2>

          <p className="mb-8 text-lg text-slate-400">
            Your intelligent customer support assistant
          </p>

          <div className="grid gap-3">

            {suggestions.map((item) => (

              <button
                key={item}
                onClick={() => onSuggestionClick(item)}
                className="rounded-xl bg-slate-900 p-4 text-left text-white transition hover:bg-blue-600"
              >
                {item}
              </button>

            ))}

          </div>

        </div>

      </div>

    );

  }

  return (

    <div className="flex-1 overflow-y-auto px-6 py-6">

      <div className="mx-auto flex max-w-5xl flex-col gap-5">

        {messages.map((message, index) => (

          <Message
            key={index}
            message={message}
          />

        ))}

        {loading && (

          <div className="flex items-center gap-3 rounded-xl bg-slate-900 p-4 w-fit">

            🤖 Nexora AI is typing...

          </div>

        )}

        <div ref={bottomRef}></div>

      </div>

    </div>

  );

}

export default ChatBox;