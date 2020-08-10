program z_4;
var e,g:integer; 
M : array [1..10,1..13] of real;
begin
 for e:= 1 to 10 do
 begin 
    for g:= 1 to 13 do M[e,g]:=random ;
 end;

 for e:= 1 to 10 do
 begin 
    for g:= 1 to 13 do write(M[e,g]:5);
    Writeln;
 end;
end.