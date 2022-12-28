% course fact contains --> Name of course, Course department, Area of interest of course, Absolute/Relative grading, pre_reqs.

% Here we define which facts are dynamic
:- dynamic department/1, interest/1, grading/1, pre_reqs/1.


% Machine Learning Courses(CSE courses)
course('Machine Learning','CSE','Machine Learning','relative',['MTH100','CSE101']).
course('Natural Language Processing','CSE','Machine Learning','absolute',['MTH201','CSE101']).
course('Artificial Intelligence','CSE','Machine Learning','relative',['CSE102','CSE121']).

% Networking Courses(CSE courses)
course('Computer Networks','CSE','Networking','relative',['CSE101','CSE222','CSE232']).
course('Network Security','CSE','Networking','absolute',['CSE232','CSE231']).
course('Computer Security','CSE','Networking','relative',['CSE232']).

% Databases Courses(CSE courses)
course('Information Retrieval','CSE','Databases','relative',['CSE102','CSE201','CSE202']).
course('DBMS','CSE','Databases','relative',['CSE102']).
course('Information Integration and Applications','CSE','Databases','absolute',['CSE202']).

% Algorithms Courses(CSE courses)
course('Algorithm Design and Analysis','CSE','Algorithms','relative',['CSE102']).
course('Introduction to Programming','CSE','Algorithms','relative',[]).
course('Modern Algorithm Design','CSE','Algorithms','absolute',['CSE222']).
course('Approximation Algorithms','CSE','Algorithms','relative',['CSE222']).

% Biology Courses(Non-CSE courses)
course('Computational Gastronomy','Non-CSE','Biology','relative',[]).
course('Computing for Medicine','Non-CSE','Biology','relative',[]).
course('Machine Learning for Biomedical Applications','Non-CSE','Biology','relative',[]).

% Design Courses(Non-CSE courses)
course('Introduction to Animation and Graphics','Non-CSE','Design','absolute',[]).
course('3D Animation Film Making','Non-CSE','Design','relative',[]).
course('Affective Computing','Non-CSE','Design','relative',['CSE101','CSE102','CSE201']).

% Social Science Courses(Non-CSE courses)
course('Neuroscience of Decision Making','Non-CSE','Social Science','absolute',[]).
course('Urban Space and Political Power','Non-CSE','Social Science','relative',[]).
course('Environmental Sciences','Non-CSE','Social Sciences','relative',[]).

% Electronics Courses(Non-CSE courses)
course('Digital Signal Processing','Non-CSE','Electronics','absolute',['ECE250']).
course('Reinforcement Learning','Non-CSE','Electronics','relative',['MTH201']).
course('Digital Image Processing','Non-CSE','Electronics','relative',['MTH100','MTH201']).


pre_req_satisfy([],L) :-
	is_list(L).
pre_req_satisfy(L,[]) :-
	(not(is_list(L)) -> false;
		L==[]).
pre_req_satisfy(L1,L2) :-
	% L1 is the pre-requisites of the given course
	% L2 is all the courses done by the student previously.
	% This function tells us if the student can take the given course on basis of the 
	% pre-requisites(L1) of given course and the courses the student has done yet (L2).

	[H|T] = L1,
	member(H,L2),
	pre_req_satisfy(T,L2).

display_recommended_courses(A):-
	% This function is used to print all the courses that are best suitable for the student based on his preferences taken.
	% The ranking of the courses are done based on --> department > interest > grading > pre_req_satisfy.

	forall((course(Name,Dept,Area,Grading,Pre_reqs), department(Dept), interest(Area), grading(Grading), pre_req_satisfy(Pre_reqs,A)), (write(Name),nl)).


main :-
	% consult("facts.pl") loads the facts inside the file "facts.pl" in our current prolog database.
	consult("facts.pl"),
	write('This is an Elective course recommendation system'),nl,

	write('What is your name?'),nl,
	read(StudName),nl,
	write('Hi '),write(StudName),nl,

	% Here we read the list of courses done previously by the student into the variable A4.
	courses_done(A4),nl,

	% Here, we run the recommendation function display_recommended_courses/1. This function
	% simply prints all the courses that the student can take which are matching with the preferences
	% the student has selected before.
	write("Below are the recommended courses for you according to your given preferences :-"),nl,nl,
	display_recommended_courses(A4).