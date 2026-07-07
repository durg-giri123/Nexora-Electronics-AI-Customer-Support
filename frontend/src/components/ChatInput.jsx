import { useState } from "react";
import { SendHorizonal } from "lucide-react";

function ChatInput({ onSend, loading }) {

  const [query, setQuery] = useState("");

  const handleSubmit = () => {

    if (!query.trim()) return;

    onSend(query);

    setQuery("");

  };

  return (

    <div className="border-t border-slate-800 bg-slate-950 p-5">

      <div className="mx-auto flex max-w-5xl gap-3">

        <textarea

          rows={1}

          value={query}

          onChange={(e) => setQuery(e.target.value)}

          onKeyDown={(e) => {

            if (e.key === "Enter" && !e.shiftKey) {

              e.preventDefault();

              handleSubmit();

            }

          }}

          placeholder="Ask anything about Nexora products..."

          className="flex-1 resize-none rounded-xl border border-slate-700 bg-slate-900 px-5 py-4 text-white outline-none transition focus:border-blue-500"

        />

        <button

          onClick={handleSubmit}

          disabled={loading}

          className="rounded-xl bg-blue-600 px-6 text-white transition hover:bg-blue-700 disabled:opacity-50"

        >

          <SendHorizonal />

        </button>

      </div>

    </div>

  );

}

export default ChatInput;