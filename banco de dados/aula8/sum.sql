CREATE OR REPLACE PROCEDURE somar_dois_valores(
    IN a INT,
    IN b INT,
    OUT resultado INT
)
LANGUAGE plpgsql AS $$
BEGIN
    resultado := a + b;  -- Atribuição correta
END;
$$;
