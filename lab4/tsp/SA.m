clear all
close all

%% Symulated Annealing for solving TSP

%% parameters
graph  = createGraph(20, 3); % choose graph
T=100;                         % start temperature
alph=0.9992;                   % cooling factor
iter = 7000;                  % nr of iterations to perform
consecutive = false;         % type of swap (consecutive / arbitrary)
drawSteps = 0;               % draw steps while execution: 0-don't, 1-some, 2-all
%% initializing variables
optimState.tour = randperm(graph.n);
optimState.cost = fitnessF ( optimState.tour , graph);
fitness_hist = zeros(1, iter);
clc
%% Symulated Annealing algorithm
for it = 1 : iter
    set(gcf, 'Position',  [100, 100, 1000, 400])
    fitness_hist(it) = optimState.cost;
    
    % get new state
    if consecutive
        optimStateNew.tour=consecSwap(optimState.tour);
    else
        optimStateNew.tour=arbitrarySwap(optimState.tour);
    end
    optimStateNew.cost = fitnessF( optimStateNew.tour , graph);
    
    % decide whether change state
    delta = optimStateNew.cost - optimState.cost;
    if delta > 0
        optimState.cost = optimStateNew.cost;
        optimState.tour = optimStateNew.tour;
    else
        if rand<=exp(delta/T)
            optimState.cost = optimStateNew.cost;
            optimState.tour = optimStateNew.tour;
        end
    end
    
    % calculate new temperature
    T=alph*T;
%     T=T-alph;
    
    % Display current results 
    if drawSteps==2 || (drawSteps==1 && mod(it, 100)==0)
        drawState(optimState, graph, fitness_hist,it) 
    end
end

%% display end results
drawState(optimState, graph, fitness_hist,it) 

