import * as React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import Grid from '@mui/material/Grid';
import axios from 'axios';


function loadScript(src, position, id) {
  if (!position) {
    return;
  }

  const script = document.createElement('script');
  script.setAttribute('async', '');
  script.setAttribute('id', id);
  script.src = src;
  position.appendChild(script);
}

const autocompleteService = { current: null };

export default function AsyncAutocomplete(props) {
  const [value, setValue] = React.useState(null);
  const [inputValue, setInputValue] = React.useState('');
  const [options, setOptions] = React.useState([]);
  const loaded = React.useRef(false);

  React.useEffect(() => {
    let active = true;

    if (inputValue === '') {
      setOptions(value ? [value] : []);
      return undefined;
    }

    axios.get("http://127.0.0.1:5000/api?textInput=" + inputValue)
      .then(response => {
        setOptions(response.data.searchResult)
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });

    props.setValue(value);

    return () => {
      active = false;
    };

  }, [value, inputValue, fetch]);

  const customStyle = {
    fontFamily: 'Monospace',
  };

  return (
    <Autocomplete
      id="async-autocomplete-1"
      style={customStyle}
      sx={{ width: 300 }}
      getOptionLabel={(option) =>
        typeof option === 'string' ? option : option.description
      }
      filterOptions={(x) => x}
      options={options}
      autoComplete
      includeInputInList
      filterSelectedOptions
      value={value}
      noOptionsText="No page found"
      onChange={(event, newValue) => {
        setOptions(newValue ? [newValue, ...options] : options);
        setValue(newValue);
      }}
      onInputChange={(event, newInputValue) => {
        setInputValue(newInputValue);
      }}
      renderInput={(params) => (
        <TextField {...params} label={props.title} fullWidth />
      )}
      renderOption={(props, option) => {
        const matches = option;

        return (
          <li {...props}>
            <Grid container alignItems="center">
              <Grid item sx={{ width: 'calc(100% - 44px)', wordWrap: 'break-word' }}>
              
                <div style={{ fontFamily: 'Monospace'}}>{option}</div>
              </Grid>
            </Grid>
          </li>
        );
      }}
    />
  );
}