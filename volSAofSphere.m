%id = 10922160
%name = andrews kofi blemano
%department = mten

function [volume, SA] = volSAofSphere(r)
r = input('Enter the radius:');
volume = (4 * pi * (r)^3)/3;
SA = 4*pi*(r)^2;
fprintf('the volume of the sphere is %.3f\n',volume)
fprintf('the surface area of the sphere is %.1f\n',SA)
end