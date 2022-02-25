-- upgrade --
ALTER TABLE "productserialnumber" ALTER COLUMN "serial_number" TYPE VARCHAR(256) USING "serial_number"::VARCHAR(256);
-- downgrade --
ALTER TABLE "productserialnumber" ALTER COLUMN "serial_number" TYPE INT USING "serial_number"::INT;
