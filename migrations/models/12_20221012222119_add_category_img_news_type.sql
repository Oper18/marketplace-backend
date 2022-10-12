-- upgrade --
ALTER TABLE "category" ADD "img" VARCHAR(64);
ALTER TABLE "new" ADD "new_type" INT  UNIQUE;
-- downgrade --
ALTER TABLE "new" DROP COLUMN "new_type";
ALTER TABLE "category" DROP COLUMN "img";
