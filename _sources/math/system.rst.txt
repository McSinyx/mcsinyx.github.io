System Cascade Connection
=========================

Given two discrete-time systems :math:`A` and :math:`B` connected in cascade
to form a new system :math:`C = x \mapsto B(A(x))`.

Linearity
---------

If :math:`A` and :math:`B` are linear, i.e. for all signals :math:`x_i` and scalars :math:`a_i`,

.. math::

   A\left(n \mapsto \sum_i a_i x_i[n]\right) &= n \mapsto \sum_i a_i A(x_i)[n]\\
   B\left(n \mapsto \sum_i a_i x_i[n]\right) &= n \mapsto \sum_i a_i B(x_i)[n]

then :math:`C` is also linear

.. math::

   C\left(n \mapsto \sum_i a_i x_i[n]\right)
   &= B\left(A\left(n \mapsto \sum_i a_i x_i[n]\right)\right)\\
   &= B\left(n \mapsto \sum_i a_i A(x_i)[n]\right)\\
   &= n \mapsto \sum_i a_i B(A(x_i))[n]\\
   &= n \mapsto \sum_i a_i C(x_i)[n]

Time Invariance
---------------

If :math:`A` and :math:`B` are time invariant,
i.e. for all signals :math:`x` and integers :math:`k`,

.. math::

   A(n \mapsto x[n - k]) &= n \mapsto A(x)[n - k]\\
   B(n \mapsto x[n - k]) &= n \mapsto B(x)[n - k]\\

then :math:`C` is also time invariant

.. math::

   C(n \mapsto x[n - k])
   &= B(A(n \mapsto x[n - k]))\\
   &= B(n \mapsto A(x)[n - k])\\
   &= n \mapsto B(A(x))[n - k]\\
   &= n \mapsto C(x)[n - k]

LTI Ordering
------------

If :math:`A` and :math:`B` are linear and time-invariant, there exists
signals :math:`g` and :math:`h` such that for all signals :math:`x`,
:math:`A = x \mapsto x * g` and :math:`B = x \mapsto x * h`, thus 

.. math::

   B(A(x)) = B(x * g) = x * g * h = x * h * g = A(x * h) = A(B(x))

or interchanging :math:`A` and :math:`B` order does not change :math:`C`.

Causality
---------

If :math:`A` and :math:`B` are causal,
i.e. for all signals :math:`x`, :math:`y` and any choise of integer :math:`k`,

.. math::

   \forall n < k, x[n] = y[n]\quad
   \Longrightarrow &\;\begin{cases}
     \forall n < k, A(x)[n] = A(y)[n]\\
     \forall n < k, B(x)[n] = B(y)[n]
   \end{cases}\\
   \Longrightarrow &\;\forall n < k, B(A(x))[n] = B(A(y))[n]\\
   \Longleftrightarrow &\;\forall n < k, C(x)[n] = C(y)[n]

then :math:`C` is also causal.

BIBO Stability
--------------

If :math:`A` and :math:`B` are stable, i.e. there exists a signal :math:`x`
and scalars :math:`a` and :math:`b` that for all integers :math:`n`,

.. math::

   |x[n]| < a &\Longrightarrow |A(x)[n]| < b\\
   |x[n]| < a &\Longrightarrow |B(x)[n]| < b

then :math:`C` is also stable, i.e. there exists a signal :math:`x`
and scalars :math:`a`, :math:`b` and :math:`c` that for all integers :math:`n`,

.. math::

   |x[n]| < a\quad
   \Longrightarrow &\;|A(x)[n]| < b\\
   \Longrightarrow &\;|B(A(x))[n]| < c\\
   \Longleftrightarrow &\;|C(x)[n]| < c
