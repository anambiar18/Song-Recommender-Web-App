import './App.css';
import TextBox from './TextBox';
import ArtistBox from './ArtistBox';

function App() {

  return (
    <div className="App">
      <header className="App-header">
        <p>
          How are you doing today? Let us know and we will recommend some songs
        </p>
        <TextBox />
        <p>
          Indicate an artist of your choice to help us narrow our results
        </p>
        <ArtistBox />
      </header>
    </div>
  );

}

export default App;
