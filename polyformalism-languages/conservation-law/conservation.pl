% PROLOG: What declarative logic reveals about conservation
% Forces you to think about: Relations, not functions. delta(N, D) is not
%   "compute D from N" — it's "N and D stand in this RELATION."
% Broken assumption: That computation flows input→output. Given η and C,
%   you can query γ. The conservation law is BIDIRECTIONALLY QUERYABLE.
% Novel insight: γ + η = C is a Prolog clause. Directionality is an assumption,
%   not a law. You can ask "for what n is δ(n) > 0.1?" and let Prolog search.

:- use_module(library(lists)).

delta(N, D) :-
    N > 0,
    D is (1 / sqrt(N)) * (1 - 3 / (2 * N)).

ccr(N, C) :-
    delta(N, D),
    C is D * 100.

conservation_table :-
    writeln('    n       δ(n)     CCR%'),
    writeln('----------------------------'),
    forall(between(1, 100, N),
           ( delta(N, D),
             ccr(N, C),
             format('~5d  ~10f  ~7f%~n', [N, D, C]) )).

% Query: ?- conservation_table.
% Query: ?- delta(N, D), D > 0.1.  (find all n where δ > 0.1)

