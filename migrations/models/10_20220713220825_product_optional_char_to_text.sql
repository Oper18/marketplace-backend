-- upgrade --
ALTER TABLE "product" ALTER COLUMN "sketches_de" TYPE TEXT USING "sketches_de"::TEXT;
ALTER TABLE "product" ALTER COLUMN "sketches" TYPE TEXT USING "sketches"::TEXT;
ALTER TABLE "product" ALTER COLUMN "sketches_en" TYPE TEXT USING "sketches_en"::TEXT;
ALTER TABLE "product" ALTER COLUMN "sketches_fr" TYPE TEXT USING "sketches_fr"::TEXT;
-- downgrade --
ALTER TABLE "product" ALTER COLUMN "sketches_de" TYPE VARCHAR(2048) USING "sketches_de"::VARCHAR(2048);
ALTER TABLE "product" ALTER COLUMN "sketches" TYPE VARCHAR(2048) USING "sketches"::VARCHAR(2048);
ALTER TABLE "product" ALTER COLUMN "sketches_en" TYPE VARCHAR(2048) USING "sketches_en"::VARCHAR(2048);
ALTER TABLE "product" ALTER COLUMN "sketches_fr" TYPE VARCHAR(2048) USING "sketches_fr"::VARCHAR(2048);
