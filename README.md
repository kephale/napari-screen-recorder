# napari-screen-recorder

[![License MIT](https://img.shields.io/pypi/l/napari-screen-recorder.svg?color=green)](https://github.com/kephale/napari-screen-recorder/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-screen-recorder.svg?color=green)](https://pypi.org/project/napari-screen-recorder)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-screen-recorder.svg?color=green)](https://python.org)
[![tests](https://github.com/kephale/napari-screen-recorder/workflows/tests/badge.svg)](https://github.com/kephale/napari-screen-recorder/actions)
[![codecov](https://codecov.io/gh/kephale/napari-screen-recorder/branch/main/graph/badge.svg)](https://codecov.io/gh/kephale/napari-screen-recorder)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-screen-recorder)](https://napari-hub.org/plugins/napari-screen-recorder)

A simple screen recorder for napari

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-screen-recorder` via [pip]:

    pip install napari-screen-recorder



To install latest development version :

    pip install git+https://github.com/kephale/napari-screen-recorder.git


## Usage

```
import napari
from napari_screen_recorder import add_recording_widget

# Your custom code to initialize and manipulate the viewer
viewer = napari.Viewer()

# Add the recording widget to the viewer
recording_widget = add_recording_widget(viewer)

# Programmatically start recording
recording_widget.recorder.set_file_path('output.mp4')
recording_widget.recorder.set_canvas_only(True)
recording_widget.recorder.start_recording(duration=10, continuous=False)

# Start the Napari event loop
napari.run()
```

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-screen-recorder" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/kephale/napari-screen-recorder/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
