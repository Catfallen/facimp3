create function somar_numeros(a integer, b integer)
returns integer
Language plpgsql
as $$
begin
    return a+b;
end;
$$