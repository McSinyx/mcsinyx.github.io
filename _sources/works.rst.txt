Free Software Works
===================

Applications
------------

comp
^^^^

`Curses Omni Media Player`__ is a mpv__ front-end using curses.

.. image::
   https://git.disroot.org/McSinyx/comp/raw/branch/bachelor/doc/screenshot.png

It has basic media player functions and can to extract playlists
from multiple sources such as media sites supported by youtube-dl__,
local and direct URL to video/audio and its own JSON playlist format.

__ https://pypi.org/project/comp
__ https://mpv.io
__ https://ytdl-org.github.io/youtube-dl

pip
^^^

pip__ is a package manager for Python.  `Summer 2020 <gsoc2020>`_,
I worked as an intern trying improve its new resolver's networking performance.
The final result was not satisfying so at the time of writing I am still
continuing the optimization works, as well as hanging around the project's
issue tracker doing what I can do, mostly because I've grown to like its
contributors and surprisingly hacky codebase (-;

__ https://pip.pypa.io

Libraries
---------

Palace
^^^^^^

`Pythonic Audio Library and Codecs Environment`__ provides
common higher-level API for audio rendering using OpenAL:

* 3D positional rendering, with HRTF__ support for stereo systems
* Environmental effects: reverb, atmospheric air absorption,
  sound occlusion and obstruction
* Out-of-the-box codec support: FLAC, MP3, Ogg Vorbis, Opus, WAV, AIFF, etc.

Palace wraps around the C++ interface alure__ using Cython__ for a safe and
convenient interface with type hinting, data descriptors and context managers,
following :pep:`8#naming-conventions` (``PascalCase.snake_case``).

__ https://mcsinyx.github.io/palace
__ https://en.wikipedia.org/wiki/Head-related_transfer_function
__ https://github.com/kcat/alure
__ https://cython.org

Lazip
^^^^^

Lazip__ is a Python library providing a read-only file-like object
lazily mapped to a ZIP file over HTTP via range requests.

__ https://lazip.rtfd.io

Video Games
-----------

Brutal Maze
^^^^^^^^^^^

`Brutal Maze`__ is a thrilling shoot ‘em up game with minimalist art style.

.. image:: https://brutalmaze.rtfd.io/_images/screenshot.png
   :target: https://brutalmaze.rtfd.io/recplayer.html

__ https://brutalmaze.rtfd.io

The game features a trigon trapped in an infinite maze.  As our hero tries
to escape, the maze's border turns into aggressive squares trying to stop per.
Your job is to help the trigon fight against those evil squares and find
a way out (if there is any).  Be aware that the more get killed,
the more will show up and our hero will get weaker when wounded.

Axuy
^^^^

Axuy__ is a mininalist peer-to-peer first-person shooter.

.. image:: https://user-images.githubusercontent.com/13689192/85820832-57455280-b7a1-11ea-84c5-b049abfc2098.png

It is a WIP game for me to experiment with various concepts
in P2P networking as well as 3D game development.

__ https://www.youtube.com/playlist?list=PLAA9fHINq3sayfxEyZSF2D_rMgDZGyL3N

Slacker
^^^^^^^

Slacker__ is a clone/parody of the popular arcade game Stacker__.

__ https://pypi.org/project/slacker-game
__ https://en.wikipedia.org/wiki/Stacker_(arcade_game)

Plugins
-------

Vicious
^^^^^^^

Vicious__ is a modular widget library for window managers, but mostly catering
to users of the `awesome window manager`__.  It was derived from the old
*wicked* widget library, and has some of the old *wicked* widget types,
a few of them rewritten, and a good number of new ones.

Vicious widget types are a framework for creating your own widgets.
Vicious contains modules that gather data about your system,
and a few *awesome* helper functions that make it easier to register timers,
suspend widgets and so on.  Vicious doesn't depend on any third party Lua__
library, but may depend on additional system utilities.

__ https://vicious.rtfd.io
__ https://awesomewm.org
__ https://www.lua.org

Alful
^^^^^

Alful__ is a six-line extension making Firefox Quantum open all windows
in fullscreen to hide the toolbars in windowed mode
(``full-screen-api.ignore-widgets = true``).  All credits go to tazeat,
who wrote the original version and suggested the change
`to achieve the current behavior`__.

__ https://addons.mozilla.org/en-US/firefox/addon/alful
__ https://github.com/tazeat/AutoFullscreen/issues/4#issuecomment-509723353

vim-octave
^^^^^^^^^^

I am maintaining `Octave syntax and indentation support for Vim`__.

__ https://github.com/McSinyx/vim-octave

Localizations
-------------

Simplified Vietnamese Keymaps
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I am the author of the `simplified Telex and VNI keymaps`__
for Vim__ and ibus-table__.

__ https://github.com/McSinyx/ibus-table-vietnamese#phương-thức-gõ
__ https://github.com/vim/vim/commit/a02a551
__ https://github.com/moebiuscurve/ibus-table-others/commit/b6fafd0

Vietnamese Translation of Flare
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I have translated the `Free/Libre Action Roleplaying Engine`__ (yep,
just the engine) to Vietnamese.  The translation of the `Empyrean Campaign`__
is work in progress---admittedly it does not get enough priority lately.

__ https://flarerpg.org
__ https://flarerpg.org/index.php/mods/flare-empyrean

Themes
------

Add-Waiter
^^^^^^^^^^

Add-Waiter is a `GTK+ 2`__ and xfwm4__ clone of the dark variant
of the default GTK+ 3 theme Adwaita__.  It was created using
screenshots of the original theme on GTK+ 3.16.

.. image:: https://cdn.pling.com/img//hive/content-pre2/170664-2.png

The theme was released under GPLv2+, although after the redesign
of openDesktop.org, such information is no longer available on the website.

__ https://www.opendesktop.org/p/1078597
__ https://www.opendesktop.org/p/1016170
__ https://blogs.gnome.org/mclasen/2014/06/13/a-new-default-theme-for-gtk/

MathieWD
^^^^^^^^

MathieWD__ is a flat and clean xfwm4 theme that uses colors from
the active GTK+ theme.  It is inspired by elementary mathematical symbols.

.. image:: https://cdn.pling.com/img//hive/content-pre2/168712-2.png

The theme was released under GPLv2+, although after the redesign of
openDesktop.org, such information is no longer available on the website.

__ https://www.opendesktop.org/p/1016294

Miscellaneous
^^^^^^^^^^^^^

Other themes and configurations are cooperated into my personal dotfiles__.

__ https://git.disroot.org/McSinyx/dotfiles
