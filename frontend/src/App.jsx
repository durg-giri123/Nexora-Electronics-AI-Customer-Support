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

    const start = performance.now();

    try {

      const result = await sendMessage(query);

      const end = performance.now();

      const aiMessage = {

        sender: "ai",

        text: result.response,

        agent: result.agent,

        sources: result.sources,

        responseTime: ((end - start) / 1000).toFixed(2),

      };

      setMessages(prev => [...prev, aiMessage]);

    }

    catch {

      setMessages(prev => [

        ...prev,

        {

          sender: "ai",

          text: "Unable to connect to the server.",

          agent: "System",

          sources: [],

          responseTime: null,

        },

      ]);

    }

    finally {

      setLoading(false);

    }

  };

  const handleDownload = () => {

    if (messages.length === 0) return;

    let text = "";

    messages.forEach((msg) => {

      text += `${msg.sender.toUpperCase()}\n`;

      text += `${msg.text}\n\n`;

    });

    const blob = new Blob([text], {
      type: "text/plain",
    });

    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;

    a.download = "Nexora_Chat.txt";

    a.click();

    URL.revokeObjectURL(url);

  };

  const handleClear = () => {

    setMessages([]);

    localStorage.removeItem("nexora_chat");

  };

  return (

    <div className="flex h-screen flex-col bg-slate-950">

      <Header
        onDownload={handleDownload}
        onClear={handleClear}
      />

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