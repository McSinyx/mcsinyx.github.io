Infinite Sequences: A Case Study in Functional Python
=====================================================

In this article, we will only consider sequences defined by a function
whose domain is a subset of the set of all integers.  Such sequences will be
*visualized*, i.e. we will try to evaluate the first few (thousand) elements,
using functional programming paradigm, where functions are more similar
to the ones in math (in contrast to imperative style with side effects
confusing to inexperenced coders).  The idea is taken from `subsection 3.5.2
of SICP`_ and adapted to Python, which, compare to Scheme, is significantly
more popular: Python is pre-installed on almost every modern Unix-like system,
namely macOS, GNU/Linux and the \*BSDs; and even at MIT, the new 6.01 in Python
has recently replaced the legendary 6.001 (SICP).

One notable advantage of using Python is its huge **standard** library.
For example the *identity sequence* (sequence defined by the identity function)
can be imported directly from ``itertools``:

.. code-block:: python

   >>> from itertools import count
   >>> positive_integers = count(start=1)
   >>> next(positive_integers)
   1
   >>> next(positive_integers)
   2
   >>> for _ in range(4): next(positive_integers)
   ... 
   3
   4
   5
   6

To open a Python emulator, simply lauch your terminal and run ``python``.
If that is somehow still too struggling, navigate to `the interactive shell`_
on Python.org

*Let's get it started* with somethings everyone hates: recursively defined
sequences, e.g. the famous Fibonacci (:math:`F_n = F_{n-1} + F_{n-2}`,
:math:`F_1 = 1` and :math:`F_0 = 0`).  Since `Python does not support`_
`tail recursion`_, it's generally **not** a good idea to define anything
recursively (which is, ironically, the only trivial *functional* solution
in this case) but since we will only evaluate the first few terms
(use the **Tab** key to indent the line when needed):

.. code-block:: python

   >>> def fibonacci(n, a=0, b=1):
   ...     # To avoid making the code look complicated,
   ...     # n < 0 is not handled here.
   ...     return a if n == 0 else fibonacci(n - 1, b, a + b)
   ... 
   >>> fibo_seq = (fibonacci(n) for n in count(start=0))
   >>> for _ in range(7): next(fibo_seq)
   ... 
   0
   1
   1
   2
   3
   5
   8

.. note::

   The ``fibo_seq`` above is just to demonstrate how ``itertools.count``
   can be use to create an infinite sequence defined by a function.
   For better performance, this should be used instead:

   .. code-block:: python

      def fibonacci_sequence(a=0, b=1):
          yield a
          yield from fibonacci_sequence(b, a + b)

It is noticable that the elements having been iterated through (using ``next``)
will disappear forever in the void (oh no!), but that is the cost we are
willing to pay to save some memory, especially when we need to evaluate a
member of (arbitrarily) large index to estimate the sequence's limit.
One case in point is estimating a definite integral using `left Riemann sum`_.

.. code-block:: python

   def integral(f, a, b):
       def left_riemann_sum(n):
           dx = (b-a) / n
           def x(i): return a + i*dx
           return sum(f(x(i)) for i in range(n)) * dx
       return left_riemann_sum

The function ``integral(f, a, b)`` as defined above returns a function taking
:math:`n` as an argument.  As :math:`n\to\infty`, its result approaches
:math:`\int_a^b f(x)\mathrm d x`.  For example, we are going to estimate
:math:`\pi` as the area of a semicircle whose radius is :math:`\sqrt 2`:

.. code-block:: python

   >>> from math import sqrt
   >>> def semicircle(x): return sqrt(abs(2 - x*x))
   ... 
   >>> pi = integral(semicircle, -sqrt(2), sqrt(2))
   >>> pi_seq = (pi(n) for n in count(start=2))
   >>> for _ in range(3): next(pi_seq)
   ... 
   2.000000029802323
   2.514157464087051
   2.7320508224700384

Whilst the first few aren't quite close, at index around 1000,
the result is somewhat acceptable::

   3.1414873191059525
   3.1414874770617427
   3.1414876346231577

Since we are comfortable with sequence of sums, let's move on to sums of
a sequence, which are called series.  For estimation, again, we are going to
make use of infinite sequences of partial sums, which are implemented as
``itertools.accumulate`` by thoughtful Python developers.  Geometric_ and
p-series_ can be defined as follow:

.. code-block:: python

   from itertools import accumulate as partial_sums

   def geometric_series(r, a=1):
       return partial_sums(a*r**n for n in count(0))

   def p_series(p):
       return partial_sums(1 / n**p for n in count(1))

We can then use these to determine whether a series is convergent or divergent.
For instance, one can easily verify that the :math:`p`-series with :math:`p = 2`
converges to :math:`\pi^2 / 6 \approx 1.6449340668482264` via

.. code-block:: python

   >>> s = p_series(p=2)
   >>> for _ in range(11): next(s)
   ... 
   1.0
   1.25
   1.3611111111111112
   1.4236111111111112
   1.4636111111111112
   1.4913888888888889
   1.511797052154195
   1.527422052154195
   1.5397677311665408
   1.5497677311665408
   1.558032193976458

We can observe that it takes quite a lot of steps to get the precision we would
generally expect (:math:`s_{11}` is only precise to the first decimal place;
second decimal places: :math:`s_{101}`; third: :math:`s_{2304}`).
Luckily, many techniques for series acceleration are available.
`Shanks transformation`_ for instance, can be implemented as follow:

.. code-block:: python

   from itertools import islice, tee

   def shanks(seq):
       return map(lambda x, y, z: (x*z - y*y) / (x + z - y*2),
                  *(islice(t, i, None) for i, t in enumerate(tee(seq, 3))))



In the code above, ``lambda x, y, z: (x*z - y*y) / (x + z - y*2)`` denotes
the anonymous function :math:`(x, y, z) \mapsto \frac{xz - y^2}{x + z - 2y}`
and ``map`` is a higher order function applying that function to
respective elements of subsequences starting from index 1, 2 and 3 of `seq`.
On Python 2, one should import ``imap`` from ``itertools`` to get the same
lazy_ behavior of ``map`` on Python 3.

.. code-block:: python

   >>> s = shanks(p_series(2))
   >>> for _ in range(10): next(s)
   ... 
   1.4500000000000002
   1.503968253968257
   1.53472222222223
   1.5545202020202133
   1.5683119658120213
   1.57846371882088
   1.5862455815659202
   1.5923993101138652
   1.5973867787856946
   1.6015104548459742

The result was quite satisfying, yet we can do one step futher
by continuously applying the transformation to the sequence:

.. code-block:: python

   >>> def compose(transform, seq):
   ... 	yield next(seq)
   ... 	yield from compose(transform, transform(seq))
   ... 
   >>> s = compose(shanks, p_series(2))
   >>> for _ in range(10): next(s)
   ... 
   1.0
   1.503968253968257
   1.5999812811165188
   1.6284732442271674
   1.6384666832276524
   1.642311342667821
   1.6425249569252578
   1.640277484549416
   1.6415443295058203
   1.642038043478661

Shanks transformation works on every sequence (not just sequences of
partial sums).  Back to previous example of using left Riemann sum
to compute definite integral:

.. code-block:: python

   >>> pi_seq = compose(shanks, map(pi, count(2)))
   >>> for _ in range(10): next(pi_seq)
   ... 
   2.000000029802323
   2.978391111182236
   3.105916845397819
   3.1323116570377185
   3.1389379264270736
   3.140788413965646
   3.140921512857936
   3.1400282163913436
   3.1400874774021816
   3.1407097229603256
   >>> next(islice(pi_seq, 300, None))
   3.1415061302492413

Now having series defined, let's see if we can learn anything
about power series. Sequence of partial sums of power series
∑*c*<sub>*n*</sub>(*x*-*a*)<sup>*n*</sup> can be defined as

.. code-block:: python

   from operator import mul

   def power_series(c, start=0, a=0):
       return lambda x: partial_sums(map(mul, c, (x**n for n in count(start))))

We can use this to compute functions that can be written as
`Taylor series`_:

.. code-block:: python

   from math import factorial
   def exp(x):
       return power_series(1/factorial(n) for n in count(0))(x)

   def cos(x):
       c = ((1 - n%2) * (1 - n%4) / factorial(n) for n in count(0))
       return power_series(c)(x)

   def sin(x):
       c = (n%2 * (2 - n%4) / factorial(n) for n in count(1))
       return power_series(c, start=1)(x)

Amazing!  Let's test 'em!

.. code-block:: python

   >>> e = compose(shanks, exp(1)) # this should converges to 2.718281828459045
   >>> for _ in range(4): next(e)
   ... 
   1.0
   2.749999999999996
   2.718276515152136
   2.718281825486623

Impressive, huh? For sine and cosine, series acceleration is not even necessary:

.. code-block:: python

   >>> from math import pi as PI
   >>> s = sin(PI/6)
   >>> for _ in range(5): next(s)
   ... 
   0.5235987755982988
   0.5235987755982988
   0.49967417939436376
   0.49967417939436376
   0.5000021325887924
   >>> next(islice(cos(PI/3), 8, None))
   0.500000433432915

.. _subsection 3.5.2 of SICP:
   https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-24.html#%_sec_3.5.2
.. _the interactive shell: https://www.python.org/shell/
.. _Python does not support:
   http://neopythonic.blogspot.com/2009/04/final-words-on-tail-calls.html
.. _tail recursion:
   https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#call_footnote_Temp_48
.. _left Riemann sum: https://en.wikipedia.org/wiki/Riemann_sum#Left_Riemann_sum
.. _Geometric: https://en.wikipedia.org/wiki/Geometric_series
.. _p-series:
   https://math.oregonstate.edu/home/programs/undergrad/CalculusQuestStudyGuides/SandS/SeriesTests/p-series.html
.. _Shanks transformation: https://en.wikipedia.org/wiki/Shanks_transformation
.. _lazy: https://en.wikipedia.org/wiki/Lazy_evaluation
.. _Taylor series: https://en.wikipedia.org/wiki/Taylor_series
