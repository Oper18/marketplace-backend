-- upgrade --
ALTER TABLE "category" ADD "head_en" VARCHAR(256);
ALTER TABLE "category" ADD "description_fr" VARCHAR(256);
ALTER TABLE "category" ADD "description" VARCHAR(256);
ALTER TABLE "category" ADD "description_en" VARCHAR(256);
ALTER TABLE "category" ADD "head_fr" VARCHAR(256);
ALTER TABLE "category" ADD "title" VARCHAR(256);
ALTER TABLE "category" ADD "title_fr" VARCHAR(256);
ALTER TABLE "category" ADD "title_de" VARCHAR(256);
ALTER TABLE "category" ADD "head" VARCHAR(256);
ALTER TABLE "category" ADD "head_de" VARCHAR(256);
ALTER TABLE "category" ADD "title_en" VARCHAR(256);
ALTER TABLE "category" ADD "description_de" VARCHAR(256);
-- downgrade --
ALTER TABLE "category" DROP COLUMN "head_en";
ALTER TABLE "category" DROP COLUMN "description_fr";
ALTER TABLE "category" DROP COLUMN "description";
ALTER TABLE "category" DROP COLUMN "description_en";
ALTER TABLE "category" DROP COLUMN "head_fr";
ALTER TABLE "category" DROP COLUMN "title";
ALTER TABLE "category" DROP COLUMN "title_fr";
ALTER TABLE "category" DROP COLUMN "title_de";
ALTER TABLE "category" DROP COLUMN "head";
ALTER TABLE "category" DROP COLUMN "head_de";
ALTER TABLE "category" DROP COLUMN "title_en";
ALTER TABLE "category" DROP COLUMN "description_de";
