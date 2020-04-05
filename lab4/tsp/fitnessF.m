function [ fitness ] = fitnessF ( tour , graph)
fitness = 0;
for i = 1 : length(tour) -1
    fitness = fitness + graph.edges( tour(i) , tour(i+1));
end
fitness = fitness +  graph.edges( tour(length(tour)) ,  tour(1) );
fitness = -fitness; % change minimum to maximum
end