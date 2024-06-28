CREATE OR REPLACE FUNCTION get_nb_page(table_name TEXT)
RETURNS TABLE (nb_pages INTEGER) AS $$
DECLARE
    total_count INTEGER;
BEGIN
    -- Construire la requête pour compter les lignes dans la table spécifiée
    EXECUTE format('SELECT count(*) FROM %I', table_name) INTO total_count;

    -- Calculer le nombre de pages nécessaires
    nb_pages := CEIL(total_count / 20.0);

    RETURN NEXT;
END;
$$ LANGUAGE plpgsql;
