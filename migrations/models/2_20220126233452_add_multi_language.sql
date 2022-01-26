-- upgrade --
ALTER TABLE "new" ADD "text_de" TEXT;
ALTER TABLE "new" ADD "head_en" VARCHAR(256);
ALTER TABLE "new" ADD "head_fr" VARCHAR(256);
ALTER TABLE "new" ADD "text_en" TEXT;
ALTER TABLE "new" ADD "head_de" VARCHAR(256);
ALTER TABLE "new" ADD "text_fr" TEXT;
ALTER TABLE "product" ADD "name_fr" VARCHAR(256);
ALTER TABLE "product" ADD "name_en" VARCHAR(256);
ALTER TABLE "product" ADD "full_name_en" VARCHAR(512);
ALTER TABLE "product" ADD "sketches_en" VARCHAR(2048);
ALTER TABLE "product" ADD "description_en" TEXT;
ALTER TABLE "product" ADD "full_name_fr" VARCHAR(512);
ALTER TABLE "product" ADD "description_fr" TEXT;
ALTER TABLE "product" ADD "full_name_de" VARCHAR(512);
ALTER TABLE "product" ADD "sketches_de" VARCHAR(2048);
ALTER TABLE "product" ADD "description_de" TEXT;
ALTER TABLE "product" ADD "name_de" VARCHAR(256);
ALTER TABLE "product" ADD "sketches_fr" VARCHAR(2048);
-- downgrade --
ALTER TABLE "new" DROP COLUMN "text_de";
ALTER TABLE "new" DROP COLUMN "head_en";
ALTER TABLE "new" DROP COLUMN "head_fr";
ALTER TABLE "new" DROP COLUMN "text_en";
ALTER TABLE "new" DROP COLUMN "head_de";
ALTER TABLE "new" DROP COLUMN "text_fr";
ALTER TABLE "product" DROP COLUMN "name_fr";
ALTER TABLE "product" DROP COLUMN "name_en";
ALTER TABLE "product" DROP COLUMN "full_name_en";
ALTER TABLE "product" DROP COLUMN "sketches_en";
ALTER TABLE "product" DROP COLUMN "description_en";
ALTER TABLE "product" DROP COLUMN "full_name_fr";
ALTER TABLE "product" DROP COLUMN "description_fr";
ALTER TABLE "product" DROP COLUMN "full_name_de";
ALTER TABLE "product" DROP COLUMN "sketches_de";
ALTER TABLE "product" DROP COLUMN "description_de";
ALTER TABLE "product" DROP COLUMN "name_de";
ALTER TABLE "product" DROP COLUMN "sketches_fr";