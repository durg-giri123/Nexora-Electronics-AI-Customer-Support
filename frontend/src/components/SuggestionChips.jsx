function SuggestionChips({ onSelect }) {

  const suggestions = [
    "Recommend a laptop for students",
    "How can I claim warranty?",
    "My laptop is overheating",
    "How can I download my invoice?",
    "How long does shipping take?",
    "Refund policy",
  ];

  return (

    <div className="mx-auto mt-4 flex max-w-4xl flex-wrap gap-3">

      {suggestions.map((item) => (

        <button
          key={item}
          onClick={() => onSelect(item)}
          className="rounded-full border border-slate-700 bg-slate-900 px-4 py-2 text-sm text-slate-300 transition hover:border-blue-500 hover:bg-slate-800 hover:text-white"
        >
          {item}
        </button>

      ))}

    </div>

  );

}

export default SuggestionChips;