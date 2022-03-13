-- upgrade --
ALTER TABLE "product" ALTER COLUMN "img" DROP NOT NULL;
-- downgrade --
ALTER TABLE "product" ALTER COLUMN "img" SET NOT NULL;
