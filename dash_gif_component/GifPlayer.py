# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class GifPlayer(Component):
    """A GifPlayer component.
GifPlayer is a component the creates a playable
gif in a dash application. This provides a more 
pleasant experience since gifs will not be constantly
looping. This component requires a file path to a
gif as well as a still image to use when the gif is
paused.

Keyword arguments:
- gif (string; required): A string address to an animated GIF image.
- still (string; required): A string address to a still preview of the GIF (e.g. JPG, PNG, etc.)
- autoplay (boolean; default False): A boolean which can be set true if you want to immediately
bomard your user with a moving GIF.
- alt (string; optional): Optional alt text attribute passed to
img element."""
    @_explicitize_args
    def __init__(self, gif=Component.REQUIRED, still=Component.REQUIRED, autoplay=Component.UNDEFINED, alt=Component.UNDEFINED, **kwargs):
        self._prop_names = ['gif', 'still', 'autoplay', 'alt']
        self._type = 'GifPlayer'
        self._namespace = 'dash_gif_component'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['gif', 'still', 'autoplay', 'alt']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['gif', 'still']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(GifPlayer, self).__init__(**args)
