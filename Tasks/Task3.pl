
#Task3


% Parent relationships
parent(john, mary).
parent(john, peter).

parent(susan, mary).
parent(susan, peter).

parent(mary, anne).
parent(mary, mark).

parent(david, anne).
parent(david, mark).

parent(peter, lisa).
parent(peter, james).

parent(linda, lisa).
parent(linda, james).



#GENDER


% Male members
male(john).
male(peter).
male(david).
male(mark).
male(james).

% Female members
female(susan).
female(mary).
female(anne).
female(linda).
female(lisa).


  #RULES


% Father
father(X, Y) :-
    parent(X, Y),
    male(X).

% Mother
mother(X, Y) :-
    parent(X, Y),
    female(X).

% Child
child(X, Y) :-
    parent(Y, X).

% Son
son(X, Y) :-
    child(X, Y),
    male(X).

% Daughter
daughter(X, Y) :-
    child(X, Y),
    female(X).

% Siblings
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% Brother
brother(X, Y) :-
    sibling(X, Y),
    male(X).

% Sister
sister(X, Y) :-
    sibling(X, Y),
    female(X).

% Grandparent
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Grandfather
grandfather(X, Y) :-
    grandparent(X, Y),
    male(X).

% Grandmother
grandmother(X, Y) :-
    grandparent(X, Y),
    female(X).

% Grandchild
grandchild(X, Y) :-
    grandparent(Y, X).

% Uncle
uncle(X, Y) :-
    sibling(X, Z),
    parent(Z, Y),
    male(X).

% Aunt
aunt(X, Y) :-
    sibling(X, Z),
    parent(Z, Y),
    female(X).

% Cousins
cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B),
    X \= Y.


  # SAMPLE QUERIES
   #Run these in SWI-Prolog


% ?- father(john, mary).
% true.

% ?- mother(susan, peter).
% true.

% ?- sibling(mary, peter).
% true.

% ?- brother(peter, mary).
% true.

% ?- sister(mary, peter).
% true.

% ?- grandparent(john, anne).
% true.

% ?- grandfather(john, mark).
% true.

% ?- grandmother(susan, lisa).
% true.

% ?- uncle(peter, anne).
% false.

% ?- aunt(mary, lisa).
% true.

% ?- cousin(anne, lisa).
% true.

% ?- child(mark, mary).
% true.

% ?- son(james, peter).
% true.

% ?- daughter(anne, david).
% true.