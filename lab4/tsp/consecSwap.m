function [newTour] = consecSwap(tour)
    ind=randi(length(tour));
    ind2=mod(ind, length(tour))+1;

    newTour = tour;
    newTour(ind) = tour(ind2);
    newTour(ind2) = tour(ind); 
end
