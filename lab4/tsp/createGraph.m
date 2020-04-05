function [ graph ]  = createGraph(n, distrib)
graph.n = n;
% all points sampled from [low,low][high,high] square
low = -100;
high = 100;

function [ ]  = populateNorm(xMu, yMu, from, to, sigma)
    from = round(from);
    to = round(to);
    for insI = from:to
        graph.node(insI).x = normrnd(xMu,sigma);
        graph.node(insI).y = normrnd(yMu,sigma);
    end
end

switch distrib
    case 2 %normal distibution with 4 groups of parameters
        populateNorm(-50, -50, 1, n/4, 10)
        populateNorm(-50, 50, n/4+1, n/2, 20)
        populateNorm(50, -50, n/2+1, 3*n/4, 8)
        populateNorm(50, 50, 3*n/4+1, n, 23)
    case 3 %9 separated groups of points
        xMus = [0.0, 0., 0., 80., -80., 80., 80., -80., -80.];
        yMus = [0.0, 80., -80., 0., 0., 80., -80., 80., -80 ];
        for i = 1:9
            from = (i*(n-1) + (10-n))/9;
            to = ((i+1)*(n-1) + (10-n))/9;
            populateNorm(xMus(i), yMus(i), from, to, 8)
        end
    otherwise %uniform distribution
        for i = 1 : graph.n
            graph.node(i).x = low+rand*(high-low);
            graph.node(i).y = low+rand*(high-low);
        end
    
end
%% calculate length of edge between any 2 vertices
graph.edges = zeros(  graph.n , graph.n );
for i = 1 : graph.n
    for j = 1: graph.n
        x1 = graph.node(i).x ;
        x2 = graph.node(j).x;
        y1 = graph.node(i).y;
        y2 = graph.node(j).y;

        graph.edges(i,j) = sqrt(  (x1 - x2) ^2 + (y1 - y2)^2  );

    end
end
end

