% Addition
add(X, Y, Result) :-
    Result is X + Y.

% Subtraction
subtract(X, Y, Result) :-
    Result is X - Y.

% Multiplication
multiply(X, Y, Result) :-
    Result is X * Y.

% Division
divide(X, Y, Result) :-
    Y =\= 0,  % Check for division by zero
    Result is X / Y.
