import { useState } from "react";
import {fetchSpotifyApi} from '../../api/spotifyAPIDemo';

const Dashboard = () => {
    const types = [
        'album',
        'artist',
        'playlist',
        'track',
        'show',
        'episode',
        'audiobook',
      ];
    
      const [form, setForm] = useState({
        search: '',
        artist: '',
      });
    
      const [results, setResults] = useState([]);
      const [typeSelected, setTypeSelected] = useState('');
    
    
      const handleSearch = async () => {
        const params = new URLSearchParams();
    
        params.append(
          'q',
          encodeURIComponent(`remaster track:${form.search} artist:${form.artist}`)
        );
        params.append('type', typeSelected);
    
        const queryString = params.toString();
        const url = 'https://api.spotify.com/v1/search';
    
        const updateUrl = `${url}?${queryString}`;
        const token = `Bearer ${localStorage.getItem('token')}`;
    
        const response = await fetchSpotifyApi(
          updateUrl,
          'GET',
          null,
          'application/json',
          token
        );
        
        console.log(response);
        setResults(response.tracks.items);
      };
    
    
    
      const handlePlayMusic = async (song) => {
        const token = `Bearer ${localStorage.getItem('token')}`;
        const data = {
          uris: [song],
        };
    
        const id_device = "463b1d018032942945311c9e8af024ef6f94e812";
    
        const playSong = await fetchSpotifyApi(
          `https://api.spotify.com/v1/me/player/play?device_id=${id_device}`,
          'PUT',
          JSON.stringify(data),
          'application/json',
          token
        );
        console.log(playSong);
      };
    
      const handleChange = (e) => {
        const newValues = {
          ...form,
          [e.target.name]: e.target.value,
        };
        console.log(newValues);
        setForm(newValues);
      };
    
      const handleSelectChange = (e) => {
        console.log(e.target.value);
        setTypeSelected(e.target.value);
      };
    
      const handleGetToken = async () => {
        // stored in the previous step
        const urlParams = new URLSearchParams(window.location.search);
        let code = urlParams.get('code');
        let codeVerifier = localStorage.getItem('code_verifier');
        console.log({ codeVerifier });
        const url = 'https://accounts.spotify.com/api/token';
        const clientId = '71264d7f154d4fc08be6de792e77f2b8';
        const redirectUri = 'http://localhost:5173/';
        const payload = {
          method: 'POST',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
          body: new URLSearchParams({
            client_id: clientId,
            grant_type: 'authorization_code',
            code,
            redirect_uri: redirectUri,
            code_verifier: codeVerifier,
          }),
        };
    
        const body = await fetch(url, payload);
        const response = await body.json();
    
        localStorage.setItem('token', response.access_token);
      };
    
      const getDeviceID = async () => {
        const token = `Bearer ${localStorage.getItem('token')}`;
        const response = await fetchSpotifyApi(
        'https://api.spotify.com/v1/me/player/devices',
        'GET',
        null,
        'application/json',
        token
      );
      console.log(response);
      return response.devices[0].id;
    };

  return (
    
    <div class="grid justify-center flex flex-col bg-gradient-to-b from-green-600 to-neutral-900">
        <div class="text-center text-4xl mt-5 text-zinc-50 bg-zinc-900 rounded-xl">
        <span class="bg-clip-text text-transparent bg-gradient-to-t from-slate-50 to-slate-700">
            Spotifai
        </span>
        </div>
        <div class="flex justify-center text-2xl mt-5">
        <input
            placeholder= "Track"
            type = "text"
            name = "track"
            value ={form.track}
            onChange={handleChange}
            class="bg-zinc-800 rounded-xl indent-3 text-zinc-50"
        />
        <input
            placeholder= "Artist"
            type = "artist"
            name = "artist"
            value ={form.artist}
            onChange={handleChange}
            class="ml-2 bg-zinc-800 rounded-xl indent-3 text-zinc-50"
        />
        </div>
        <div class="flex justify-center text-xl mt-3">
            <select name="types" onChange={handleSelectChange} class="ml-2 bg-zinc-800 rounded-xl indent-2 text-slate-400">
                {types.map((item)=>(
                <option key={item} value={item}>
                    {item}
                    </option>
                ))}
            </select>
            <button onClick={handleSearch} class="ml-2 bg-zinc-800 w-100 rounded-xl whitespace text-slate-400" >   
                <span class="ml-3 mr-3">Search </span>   
            </button>

            <button onClick={handleGetToken} class="ml-2 bg-zinc-800 w-100 rounded-xl whitespace text-slate-400" >   
                <span class="ml-3 mr-3">Get Token </span>   
            </button>


            <button onClick={getDeviceID} class="ml-2 bg-zinc-800 w-100 rounded-xl whitespace text-slate-400" >   
                <span class="ml-3 mr-3">Device ID </span>   
            </button>

        </div>
        {results.length > 0 && (
                <div> 
                    {results.map((item,idx) =>(
                        <div key ={item.id} class="bg-cover bg-gradient-to-t from-neutral-700 to-neutral-800 rounded-xl flex flex-row text-xl mt-4 mb-4">
                            <div class="mt-12 ml-5 mr-5 text-zinc-50">
                                {idx + 1 }
                            </div>
                            <div class="mt-4 mb-4">
                                <img src={item.album.images[0].url} style={{width:"100px", height: "100px"}}/>
            
                            </div>
                            <div class="mt-12 ml-5 mr-5 text-zinc-50">
                                {item.name}
                            </div>
                            <button class="mt-10 rounded-xl bg-zinc-100 w-40 h-10 text-3xl"onClick={() => handlePlayMusic(item.uri)}>
                                ▶
                            </button>
                        </div>
            
                    ))}
                </div>
            )} 

         
    </div>
    
  )

}


export default Dashboard