-- upgrade --
ALTER TABLE "bid" RENAME COLUMN "contacts" TO "message";
ALTER TABLE "bid" ADD "email" VARCHAR(256);
ALTER TABLE "bid" ADD "name" VARCHAR(256);
-- downgrade --
ALTER TABLE "bid" RENAME COLUMN "message" TO "contacts";
ALTER TABLE "bid" DROP COLUMN "email";
ALTER TABLE "bid" DROP COLUMN "name";
