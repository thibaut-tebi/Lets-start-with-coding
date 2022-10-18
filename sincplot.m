%sinplot using MATLAB 

x = pi/100:pi/100:10*pi;
y = sin(x)./x;

plot(x,y,'--rs','LineWidth', 2,...
    'Markersize',10);

xlabel('\pi/100 \leg \pi/100 \leg 10\pi');
ylabel('y=sin(x)/x)');

gtext('y= sinx/x');
title(' A graph of x against y')

grid on

hold off
