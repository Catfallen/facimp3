create or replace procedure somar_dois valores(in a int,in b int,out resultado)
$$
begin
    resultado: a+b;
end;
$$
Language plpgsql

--procedure
DO $$
declare
    resultado int
begin
    call somar_dois_valores(5,6,resultado);
    raise notice "Resultado: %", resultado;

end $$;