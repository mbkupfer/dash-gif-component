# dash-gif-component


dash-gif-component provides a playable gif dash component that is built on top of [react-gif-player](https://github.com/benwiley4000/react-gif-player).

Plotly's dash documentation can be found [here](https://dash.plot.ly/).


## Background

While there may be many possible use cases for using a gif in a dash app, the one reason that originally inspired me to add them was to provide a visual aid to show end-users how to use various interactive features. 

My original approach was to simply put a gif in an html `<img>` tag, but I quickly found out that this didn't work well in practice since the constant looping was a bit overwhelming, especially when there were multiple gifs on the same page. 

The second approach was a bit more refined, and I wrote a plotly community blog post about it [here](https://community.plot.ly/t/show-and-tell-creating-playable-gifs-to-document-interactive-features/22240). This used custom javascript that was dispatched when the window location's hash was changed and it worked just fine...that was until I learned that this caused very strange behavior in Internet Explorer when using dash > 0.39. There were also many other annoying issues when making this compatible with IE which made this a pain to maintain.

That brings me to dash-gif-component -- the final chapter of this story. Finally, a simple to use python module that wont require you to write a single line of javascript or create any hacks. It works on the latest version of dash, and best of all, works in IE as is!

Hope you enjoy using this plugin. 

## Installation

You can install *dash-gif-component* with `pip`:

```
pip install dash-gif-component
```

## Documentation

`dash-gif-comonent` has only one component (`GifPlayer`) and it is really easy to setup. All you need to provide are two properties:

1. `gif`: A string path to your gif
2. `still`: A string path to an image that is used for the "pause" mode*
3. There is also an optional property called `autoplay` which when set to true, will cause the gifs to automatically play. I find this to defeat the purpose of the component, but decided to include this for completeness when replicating [react-gif-player](https://github.com/benwiley4000/react-gif-player).

*[Gifsicle](http://www.lcdf.org/gifsicle/) is a useful cli-tool that can extract the first, or any, frame of a gif, among other gif related tasks.

*Note: if using local files for gif and still, then they must be loaded from the folder that is configured to serve static files. By default, this is set to `assets`.*

### Usage example:

```python
import dash_gif_component as Gif
import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    Gif.GifPlayer(
        gif='assets/my-gif.gif',
        still='assets/my-still.png',
    )
])

```

*For a complete running example, please check out [demo/usage.py](https://github.com/mbkupfer/dash-gif-component/tree/master/demo/usage.py)*

### Custom Styling

While I do find the original style sheet to be excellent on its own, you may still want to make some tweaks here and there. There are only a handful of selectors and overwriting is straightforward. The stylesheet can be referenced in [src/lib/components/css/gifplayer.css](https://github.com/mbkupfer/dash-gif-component/tree/master/src/lib/components/css/gifplayer.css).



