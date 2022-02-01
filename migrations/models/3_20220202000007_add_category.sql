-- upgrade --
CREATE TABLE IF NOT EXISTS "category" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(256) NOT NULL,
    "name_en" VARCHAR(256),
    "name_de" VARCHAR(256),
    "name_fr" VARCHAR(256),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);;
ALTER TABLE "product" ADD "article_number" VARCHAR(128);
ALTER TABLE "product" ADD "category_id" INT;
ALTER TABLE "product" ADD CONSTRAINT "fk_product_category_b9cd9984" FOREIGN KEY ("category_id") REFERENCES "category" ("id") ON DELETE CASCADE;
-- downgrade --
ALTER TABLE "product" DROP CONSTRAINT "fk_product_category_b9cd9984";
ALTER TABLE "product" DROP COLUMN "article_number";
ALTER TABLE "product" DROP COLUMN "category_id";
DROP TABLE IF EXISTS "category";
