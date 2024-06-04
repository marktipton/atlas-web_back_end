-- Lists all bands with Glam rock as their main style
-- ranks these bands by longevity.

CREATE OR REPLACE VIEW glam_rock_by_longevity AS
SELECT
  band_name,
  split - formed AS lifespan
FROM
  metal_bands
WHERE
  LOWER(style) LIKE '%glam rock%'
ORDER BY
  lifespan DESC;

SELECT * FROM glam_rock_by_longevity;