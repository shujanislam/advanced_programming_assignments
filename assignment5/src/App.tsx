import { useState } from "react";

const TodoApp = () => {
  const [list, setList] = useState<string[]>([]);
  const [text, setText] = useState("");

  const handleAdd = () => {
    const value = text.trim();
    if (!value) return;
    setList((prev) => prev.concat(value));
    setText("");
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      handleAdd();
    }
  };

  return (
    <section>
      <h3>📝 Todo List</h3>

      <div className="input-container">
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Enter a task..."
        />

        <button type="button" onClick={handleAdd}>
          Add
        </button>
      </div>

      {list.length === 0 ? (
        <div className="empty-state">No tasks yet. Add one to get started!</div>
      ) : (
        <ul>
          {list.map((item, i) => (
            <li key={`${item}-${i}`}>{item}</li>
          ))}
        </ul>
      )}
    </section>
  );
};

export default TodoApp;
