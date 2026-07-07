import { useEffect, useState } from "react";

import AgentBadge from "./AgentBadge";
import SourceChip from "./SourceChip";

import ReactMarkdown from "react-markdown";

import {
  Bot,
  User,
  Copy,
  Check,
  ThumbsUp,
  ThumbsDown,
} from "lucide-react";

function Message({ message }) {

  const isUser = message.sender === "user";

  const [displayText, setDisplayText] = useState(
    isUser ? message.text : ""
  );

  const [copied, setCopied] = useState(false);

  const [feedback, setFeedback] = useState(null);

  useEffect(() => {

    if (isUser) return;

    let index = 0;

    setDisplayText("");

    const interval = setInterval(() => {

      index++;

      setDisplayText(
        message.text.slice(0, index)
      );

      if (index >= message.text.length) {

        clearInterval(interval);

      }

    }, 8);

    return () => clearInterval(interval);

  }, [message.text, isUser]);

  const copyMessage = async () => {

    try {

      await navigator.clipboard.writeText(message.text);

      setCopied(true);

      setTimeout(() => {

        setCopied(false);

      }, 2000);

    } catch (err) {

      console.error(err);

    }

  };

  return (

    <div
      className={`flex gap-3 ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >

      {!isUser && (

        <div className="mt-1">

          <div className="rounded-full bg-blue-600 p-2">

            <Bot
              size={20}
              className="text-white"
            />

          </div>

        </div>

      )}

      <div
        className={`max-w-3xl rounded-2xl p-5 ${
          isUser
            ? "bg-blue-600 text-white"
            : "bg-slate-800 text-white"
        }`}
      >

        {

          isUser

          ?

          <p>{message.text}</p>

          :

          <div className="prose prose-invert max-w-none">

            <ReactMarkdown>

              {displayText}

            </ReactMarkdown>

          </div>

        }

        {

          !isUser && (

            <>

              <div className="mt-4">

                <AgentBadge
                  agent={message.agent}
                />

              </div>

              <div className="mt-3 flex flex-wrap gap-2">

                {

                  message.sources?.map((source) => (

                    <SourceChip
                      key={source}
                      source={source}
                    />

                  ))

                }

              </div>

              {message.responseTime && (

                <div className="mt-3 text-xs text-slate-400">

                  ⚡ Responded in {message.responseTime} sec

                </div>

              )}

              <div className="mt-4 flex gap-5">

                <button
                  onClick={copyMessage}
                  title="Copy"
                >

                  {

                    copied

                    ?

                    <Check
                      size={18}
                      className="text-green-400"
                    />

                    :

                    <Copy
                      size={18}
                      className="text-slate-400 hover:text-white"
                    />

                  }

                </button>

                <button
                  onClick={() => setFeedback("up")}
                  title="Helpful"
                >

                  <ThumbsUp
                    size={18}
                    className={
                      feedback === "up"
                        ? "text-green-400"
                        : "text-slate-400 hover:text-green-400"
                    }
                  />

                </button>

                <button
                  onClick={() => setFeedback("down")}
                  title="Not Helpful"
                >

                  <ThumbsDown
                    size={18}
                    className={
                      feedback === "down"
                        ? "text-red-400"
                        : "text-slate-400 hover:text-red-400"
                    }
                  />

                </button>

              </div>

            </>

          )

        }

      </div>

      {

        isUser && (

          <div className="mt-1">

            <div className="rounded-full bg-blue-600 p-2">

              <User
                size={20}
                className="text-white"
              />

            </div>

          </div>

        )

      }

    </div>

  );

}

export default Message;