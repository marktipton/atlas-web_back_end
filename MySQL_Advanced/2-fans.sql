-- ranks country origins of bands by number of fans

CREATE OR REPLACE VIEW fan_rank_by_country AS
SELECT
  origin,
  SUM(fans) AS nb_fans
FROM
  metal_bands
GROUP BY
  origin
ORDER BY
  nb_fans DESC;

SELECT * FROM fan_rank_by_country