function [] = drawState(optimState, graph, fitness_hist,it)
    outmsg = [ 'it ' , num2str(it) , ' length = ' , num2str(abs(optimState.cost))  ];
    disp(outmsg)

    subplot(1,2,1)
    title(['Iteration #' , num2str(it) ])
    % draw current best tour
    cla
    drawBestTour( optimState.tour, graph );

    subplot(1,2,2);
    plot(fitness_hist) 
    xlabel('iteration')
    ylabel('tour length (-)')
    drawnow
end