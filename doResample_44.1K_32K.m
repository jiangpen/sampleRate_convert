clear all
close all
clc

dropF = 1;
fn = 'organfinale.wav';
data = wavread(fn);

fsin = 44100;
fsout = 32000;
N = 32;
upN = 8;
downN = 11;

x = data(:,1);%data(1:5*44100,1);

%generate filter coefficients.
B = fir1(N,(1/upN));
% B = B*upN;
xUps = zeros(length(x)*upN,1);
y = zeros(ceil(length(x)*upN/downN),1);

t = 0:1/fsin:(length(x)/fsin - 1/fsin);
s = 0.98 * sin(1000 * 2 * pi * t);
sUps = xUps;
ys = y;
clear t;

if(dropF ~= 1)
    k=1;
    for n=1:upN:length(xUps)
        xUps(n) = x(k);
        k=k+1;
    end
    xUps = filter(B,1,xUps);
    k=1;
    for n=1:downN:length(xUps)
        y(k) = xUps(n);
        k=k+1;
    end
    
else %drop every 89th sample
    last = length(xUps) - ceil(length(xUps)/(upN+1));
    k=1;
    for n=1:upN:last
        xUps(n) = x(k);
        sUps(n) = s(k);
        if(mod(k,88) == 0)
            k = k+2;
        else
            k=k+1;
        end
    end
    xUps = filter(B,1,xUps);
    sUps = filter(B,1,sUps);
    k=1;
    for n=1:downN:length(xUps)
        y(k) = xUps(n);
        ys(k) = sUps(n);
        k=k+1;
    end
    
end
% y = 0.9*y/max(y);
% soundsc(y(1:floor(end/2)),fsout)
% soundsc(data(1:floor(end/2)),fsin)
data = resample(data, 320, 441);
wavwrite(data, fsout, 'resample_poc_funct.wav');
wavwrite(y, fsout, 'resample_poc.wav');
soundsc(ys(1:floor(end/6)),fsout)


