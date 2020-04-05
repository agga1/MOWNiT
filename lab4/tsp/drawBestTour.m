function [ ] = drawBestTour(tour , graph)
tour = [tour , tour(1)];

hold on
for i = 1 : length(tour) - 1
    
    n1 = tour(i);
    n2 =  tour(i+1); 
    xs = [graph.node(n1).x, graph.node(n2).x];
    ys = [graph.node(n1).y, graph.node(n2).y];

    plot (xs, ys, '-b');
end
% draw nodes
xs = [graph.node(:).x];
ys = [graph.node(:).y];
plot(xs, ys, 'ok', 'MarkerSize' , 3 , 'MarkerFaceColor', [0, 0, 0]);

title('Salesman Tour')
box('on');
