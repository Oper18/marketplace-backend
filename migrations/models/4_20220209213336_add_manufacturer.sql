-- upgrade --
CREATE TABLE IF NOT EXISTS "manufacturer" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(256) NOT NULL,
    "name_en" VARCHAR(256),
    "name_de" VARCHAR(256),
    "name_fr" VARCHAR(256),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);;
ALTER TABLE "product" ADD "manufacturer_id" INT;
ALTER TABLE "product" ADD CONSTRAINT "fk_product_manufact_63272260" FOREIGN KEY ("manufacturer_id") REFERENCES "manufacturer" ("id") ON DELETE CASCADE;
-- downgrade --
ALTER TABLE "product" DROP CONSTRAINT "fk_product_manufact_63272260";
ALTER TABLE "product" DROP COLUMN "manufacturer_id";
DROP TABLE IF EXISTS "manufacturer";
