E=ellinit([0,0,0,0,-1]); print("y^2=x^3-1: rank ",ellrank(E)[1..2]," tors ",elltors(E));
E=ellinit([0,0,0,0,1]); print("y^2=x^3+1: rank ",ellrank(E)[1..2]," tors ",elltors(E));
E=ellinit([0,0,0,0,16]); print("y^2=x^3+16: rank ",ellrank(E)[1..2]," tors ",elltors(E));
E=ellinit([0,0,0,0,-4]); print("y^2=x^3-4: rank ",ellrank(E)[1..2]," tors ",elltors(E));
quit;
