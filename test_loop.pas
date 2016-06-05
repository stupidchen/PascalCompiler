program test_loop;

var i,j,a:integer;

begin
   a := 0;
   while  a < 5  do
   begin
      writeln(a);
      a := a + 1;
   end;

   for a := 5  to 10 do
   begin
      writeln(a);
   end;

   for i := 1 to 3 do
   begin
      writeln(i);
      for j := 1 to i do
         writeln(j);
   end;
end.