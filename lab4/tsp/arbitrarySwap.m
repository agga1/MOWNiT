function [NewTour] = arbitrarySwap(tour)
    toSwap=randsample(length(tour),2);
    i=toSwap(1);
    j=toSwap(2);
    
    NewTour = tour;
    NewTour(i) = tour(j);
    NewTour(j) = tour(i); 
end

