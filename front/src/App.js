import "./App.css";
import { useState, useEffect } from "react";

function App() {
  const [question, setQuestion] = useState({});
  const [answer, setAnswer] = useState("");
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [solution, setSolution] = useState("");



  useEffect(() => {
    fetch("http://localhost:8080/quizz")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setIsSubmitted(false)
        setSolution("")
        setQuestion(data);
      })
      .catch((err) => {
        console.log(err.message);
      });
  }, []);

  const handleChange = (event) => {
    setAnswer(event.target.value);
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      submit();
    }
  };

  const checkIfSolution = () => {
    if (typeof question.answer == "string") {
      if (answer.toLowerCase() === question.answer.toLowerCase()) {
        setSolution("True")
      } else{
        setSolution("False")
      }
    } else {
      for (let sol of question.answer) {
        if (answer.toLowerCase() === sol.toLowerCase()) {
          setSolution("True")
          return
        }
      }
      setSolution("False")
    }
  }

  const submit = () => {
    if (isSubmitted === false && answer.length > 0) {
      setIsSubmitted(true)
      checkIfSolution()
    }
  };



  return (
    <div className="App">
      <header className="App-header">
        <img
          className="object-contain rounded-[12px] blur-sm"
          src={question.url}
          alt="thumbnail"
        />
        <p className="font-mono p-6">{question.question}</p>

        <div>
          <input
            className="placeholder:italic placeholder:text-slate-500 block bg-black w-full border rounded-md py-2 pl-9 pr-3  focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 sm:text-sm"
            placeholder="Search for anything..."
            onChange={handleChange}
            onKeyDown={handleKeyDown}
            value={answer}
          />
        </div>

        <div className="flex flex-row justify-center mt-4">
          <button
            className="p-6 place-items-end bg-sky-500 hover:bg-sky-700 text-white font-bold py-2 px-4 rounded"
            onClick={submit}
          >
            Submit
          </button>
        </div>

        <div className="font-sans flex flex-row justify-between p-3">
          <div className={`${solution === "True" ? "text-green-500" : "text-red-500"}`}>
          { solution }
          </div>
        </div>

        <div className="p-16">
          <button
            className="grid-rows-3 bg-sky-500 hover:bg-sky-700 text-white font-bold p-2 px-4 rounded-full"
            onClick={() => window.location.reload(false)}
          >
            Refresh
          </button>
        </div>
      </header>
    </div>
  );
}

export default App;
