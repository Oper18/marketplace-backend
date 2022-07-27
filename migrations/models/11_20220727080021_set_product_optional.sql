-- upgrade --
ALTER TABLE "productserialnumber" ALTER COLUMN "product_id" DROP NOT NULL;
-- downgrade --
ALTER TABLE "productserialnumber" ALTER COLUMN "product_id" INT NOT NULL;
