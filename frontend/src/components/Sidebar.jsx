import { useState, useEffect } from "react";

import Header from "./components/Header";
import ChatBox from "./components/ChatBox";
import ChatInput from "./components/ChatInput";

import { sendMessage } from "./services/api";

function App() {

  const [messages, setMessages] = useState(() => {

    const saved = localStorage.getItem("nexora_chat");

    return saved ? JSON.parse(saved) : [];

  });

  const [loading, setLoading] = useState(false);

  useEffect(() => {

    localStorage.setItem(
      "nexora_chat",
      JSON.stringify(messages)
    );

  }, [messages]);

  const handleSend = async (query) => {

    if (!query.trim()) return;

    const userMessage = {
      sender: "user",
      text: query,
    };

    setMessages(prev => [...prev, userMessage]);

    setLoading(true);

    try {

      const result = await sendMessage(query);

      const aiMessage = {
        sender: "ai",
        text: result.response,
        agent: result.agent,
        sources: result.sources,
      };

      setMessages(prev => [...prev, aiMessage]);

    } catch {

      setMessages(prev => [

        ...prev,

        {

          sender: "ai",

          text: "Unable to connect to the server.",

          agent: "System",

          sources: [],

        },

      ]);

    }

    finally {

      setLoading(false);

    }

  };

  const handleClear = () => {

    setMessages([]);

    localStorage.removeItem("nexora_chat");

  };

  return (

    <div className="flex h-screen flex-col bg-slate-950">

      <Header onClear={handleClear} />

      <main className="flex flex-1 flex-col justify-between">

        <ChatBox

          messages={messages}

          loading={loading}

          onSuggestionClick={handleSend}

        />

        <ChatInput

          onSend={handleSend}

          loading={loading}

        />

      </main>

    </div>

  );

}

export default App;