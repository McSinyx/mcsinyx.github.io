:orphan:

Google Summer of Code 2020
==========================

In the summer of 2020, I worked with the contributors of ``pip``, trying
to improve the networking performance of the package manager.  Admittedly,
at the end of the internship_ period, :ref:`the benchmark said otherwise
<benchmark>`; though I really hope the clean-up and minor fixes
I happened to be doing to the codebase over the summer, in addition
to the implementation of parallel utils and lazy wheel, might actually
help the project.

Personally, I learned a lot: not just about Python packaging and
networking stuff, but also on how to work with others.  I am really
grateful to :github:`pradyunsg` (my mentor), :github:`chrahunt`,
:github:`uranusjr`, :github:`pfmoore`, :github:`brainwane`, :github:`sbidoul`,
:github:`xavfernandez`, :github:`webknjaz`, :github:`jaraco`,
:github:`deveshks`, :github:`gutsytechster`, :github:`dholth`,
:github:`dstufft`, :github:`cosmicexplorer` and :github:`ofek`.
While this feels like a long shout-out list, it really isn't.
These people are the maintainers, the contributors of ``pip`` and/or
other Python packaging projects, and more importantly, they have been more than
helpful, encouraging and patient to me throughout my every activities,
showing me the way when I was lost, fixing me when I was wrong, putting up with
my carelessness and showing me support across different social media.

To best serve the community, below I have tried my best to document
what I have done, how I've done it and why I've done it for over
the last three months.  At the time of writing, some work is still in progress,
so these also serve as a reference point for myself and others to reason
about decisions in relevant topics.

The Main Story
--------------

The storyline can be divided into the following four main acts.

Act One: Parallelization Utilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this first act, I ensured the portibility of parallelization
measures for later use in the final act.  Multithreading and multiprocessing
``map`` were properly fellback on platforms without full support.

* :pip:`8320`: Add utilities for parallelization (close :pip:`8169`)
* :pip:`8538`: Make ``utils.parallel`` tests tear down properly
* :pip:`8504`: Parallelize ``pip list --outdated`` and ``--uptodate``
  (using :pip:`8320`)

Act Two: Lazy Wheels
^^^^^^^^^^^^^^^^^^^^

As proposed by :github:`cosmicexplorer` in :pip:`7819`, it is possible to only
download a portion of a wheel to obtain metadata during dependency resolution.
Not only that this would reduce the total amount of data to be transmitted over
the network in case the resolver needs to perform heavy backtracking, but also
it would create a synchronization point at the end of the resolution progress
where parallel downloading can be applied to the needed wheels (some wheels
solely serve their metadata during dependency backtracking and are not needed
by the users).

* :pip:`8467`: Add utitlity to lazily acquire wheel metadata over HTTP
* :pip:`8584`: Revise lazy wheel and its tests
* :pip:`8681`: Make range requests closer to chunk size (help :pip:`8670`)
* :pip:`8716` and :pip:`8730`: Disable caching for range requests

Act Three: Late Downloading
^^^^^^^^^^^^^^^^^^^^^^^^^^^

During this act, the main works were refactoring to integrate the *lazy wheel*
into ``pip``'s codebase and clean up the way for download parallelization.

* :pip:`8411`: Refactor ``operations.prepare.prepare_linked_requirement``
* :pip:`8629`: Abstract away ``AbstractDistribution``
  in higher-level resolver code
* :pip:`8442`, :pip:`8532` and :pip:`8588` (later reworked by :github:`chrahunt`
  in :pip:`8685`): Use lazy wheel to obtain dependency information
  for the new resolver
* :pip:`8743`: Test hash checking for ``fast-deps``
* :pip:`8804`: Check download directory before making range requests

Act Four: Batch Downloading in Parallel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The final act is mostly about the UI of the parallel download.
My work involved around how the progress should be displayed
and how other relevant information should be reported to the users.

* :pip:`8710`: Revise method fetching metadata using lazy wheels
* :pip:`8722`: Dedent late download logs (fix :pip:`8721`)
* :pip:`8737`: Add a hook for batch downloading
* :pip:`8771`: Parallelize wheel download

The Side Quests
---------------

In order to keep the wheel turning (no pun intended) and avoid wasting time
waiting for the pull requests above to be reviewed, I decided to create
even more PRs (as I am typing this, many of the patches listed below
are nowhere near being merged).

* :pip:`7878`: Fail early when install path is not writable
* :pip:`7928`: Fix rst syntax in Getting Started guide
* :pip:`7988`: Fix tabulate col size in case of empty cell
* :pip:`8137`: Add subcommand alias mechanism
* :pip:`8143`: Make mypy happy with beta release automation
* :pip:`8248`: Fix typo and simplify ireq call
* :pip:`8332`: Add license requirement to ``_vendor/README.rst``
* :pip:`8423`: Nitpick logging calls
* :pip:`8435`: Use str.format style in logging calls
* :pip:`8456`: Lint ``src/pip/_vendor/README.rst``
* :pip:`8568`: Declare constants in configuration.py as such
* :pip:`8571`: Clean up ``Configuration.unset_value`` and nit ``__init__``
* :pip:`8578`: Allow verbose/quiet level to be specified
  via config files and environment variables
* :pip:`8599`: Replace tabs by spaces for consistency
* :pip:`8614`: Use ``monkeypatch.setenv`` to mock environment variables
* :pip:`8674`: Fix ``tests/functional/test_install_check.py``,
  when run with new resolver
* :pip:`8692`: Make assertion failure give better message
* :pip:`8709`: List downloaded distributions before exiting (fix :pip:`8696`)
* :pip:`8759`: Allow py2 deprecation warning from setuptools
* :pip:`8766`: Use the new resolver for test requirements
* :pip:`8790`: Mark tests using remote svn and hg as xfail
* :pip:`8795`: Reformat a few spots in user guide

The Plot Summary
----------------

Every Monday throughout the Summer of Code, I summarized what I had done
in the week before in the form of either a short blog or an (even shorter)
check-in.  These write-ups often contain handfuls of popular culture references
and was originally hosted on `Python GSoC`_.

.. toctree::
   :titlesonly:

   checkin20200601
   blog20200609
   checkin20200615
   blog20200622
   checkin20200629
   blog20200706
   checkin20200713
   blog20200720
   checkin20200727
   blog20200803
   checkin20200810
   blog20200817
   checkin20200824
   blog20200831

.. _internship:
   https://summerofcode.withgoogle.com/archive/2020/projects/6238594655584256
.. _Python GSoC: https://blogs.python-gsoc.org/en/mcsinyxs-blog/
