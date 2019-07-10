/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import GifPlayer from '../lib/components/GifPlayer.react.js';


class App extends Component {
    render() {
        return (
            <div>
                <GifPlayer
                    gif={'/assets/giphy.gif'}
                    still={'/assets/giphy.png'}
                />
            </div>
        )
    }
}

export default App;