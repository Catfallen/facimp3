create or replace procedure inserir_actor(
    first_name text,
    last_name text
)
Language plpgsql AS $$
begin
    insert into actor(first_name,last_name)
    values (first_name,last_name);
end;
$$

CREATE OR REPLACE PROCEDURE inserir_actor(
    first_name TEXT,
    last_name TEXT
)
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO actor(first_name, last_name)
    VALUES (first_name, last_name);
END;
$$;