import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <img class="object-contain h-48 rounded-[12px]" src="https://upload.wikimedia.org/wikipedia/commons/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg" />
      <p class="font-mono p-6">Who painted this work ?</p>

<div>
  <input class="placeholder:italic placeholder:text-slate-500 block bg-black w-full border rounded-md py-2 pl-9 pr-3  focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 sm:text-sm" placeholder="Search for anything..."/>
</div>

<div class="flex flex-row justify-center mt-4">
  <button class="p-6 place-items-end bg-sky-500 hover:bg-sky-700 text-white font-bold py-2 px-4 rounded">Submit</button>
</div>

<div class="font-sans flex flex-row justify-between p-6 text-green-500	">
  Bravo !
</div>

    <div class="p-16">
<button class="grid-rows-3 bg-sky-500 hover:bg-sky-700 text-white font-bold p-2 px-4 rounded-full" onClick={() => window.location.reload(false)}>Refresh</button>
  </div>
      </header>
    </div>
  );
}

export default App;
