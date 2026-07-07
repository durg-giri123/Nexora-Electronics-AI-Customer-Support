import { Bot, Download, Trash2 } from "lucide-react";

function Header({ onDownload, onClear }) {

  return (

    <header className="border-b border-slate-800 bg-slate-900">

      <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">

        <div className="flex items-center gap-3">

          <div className="rounded-xl bg-blue-600 p-2">

            <Bot className="h-6 w-6 text-white" />

          </div>

          <div>

            <h1 className="text-xl font-bold text-white">
              Nexora Electronics
            </h1>

            <p className="text-sm text-slate-400">
              AI Customer Support
            </p>

          </div>

        </div>

        <div className="flex items-center gap-3">

          <button
            onClick={onDownload}
            className="rounded-lg bg-slate-800 p-2 hover:bg-slate-700"
            title="Download Chat"
          >
            <Download
              className="text-white"
              size={18}
            />
          </button>

          <button
            onClick={onClear}
            className="rounded-lg bg-red-600 p-2 hover:bg-red-700"
            title="Clear Chat"
          >
            <Trash2
              className="text-white"
              size={18}
            />
          </button>

          <span className="rounded-full bg-emerald-600 px-3 py-1 text-sm font-medium text-white">
            Online
          </span>

        </div>

      </div>

    </header>

  );

}

export default Header;