-- upgrade --
ALTER TABLE "product" ADD "volume" VARCHAR(128);
-- downgrade --
ALTER TABLE "product" DROP COLUMN "volume";
