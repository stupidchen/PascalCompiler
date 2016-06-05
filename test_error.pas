program test_1;
type
    arr = array [0..50] of integer;
var i,j,a,b,k,x,y,sum,testfunc: integer;
    aa:arr;
function fib(x:integer):integer;
begin
  if ((x = 0) or (x = 1)) then
    fib:=1
  else
    fib:=fib(x - 2) + fib(x - 1);
end;


begin
 i:=10;
 a:=fib(10);
 writeln(a);

 for i := 1 to 10 do
       aa[ i ] := i + 100;

 for i := 1 to 10 do
       writeln(aa[ i ]);

 for i := 2 to 50 do
   begin
      for j := 2 to i do
	      if(j = i) then
         	writeln(j);
   end;
end.
