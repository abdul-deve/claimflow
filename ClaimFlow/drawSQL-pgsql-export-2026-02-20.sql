CREATE TABLE "User"(
    "id" BIGINT NOT NULL,
    "name" CHAR(255) NOT NULL,
    "email" CHAR(255) NOT NULL,
    "password" CHAR(255) NOT NULL,
    "username" CHAR(255) NOT NULL,
    "created_at" DATE NOT NULL,
    "updated_at" DATE NOT NULL
);
ALTER TABLE
    "User" ADD PRIMARY KEY("id");
CREATE TABLE "Roles"(
    "id" BIGINT NOT NULL,
    "role" CHAR(255) NOT NULL,
    "created_at" DATE NOT NULL,
    "updated_at" DATE NOT NULL
);
ALTER TABLE
    "Roles" ADD PRIMARY KEY("id");
COMMENT
ON COLUMN
    "Roles"."role" IS 'it will be choices filed';
CREATE TABLE "Organization"(
    "id" BIGINT NOT NULL,
    "owner" BIGINT NOT NULL,
    "name" CHAR(255) NOT NULL,
    "address" VARCHAR(255) NOT NULL,
    "created_at" DATE NOT NULL,
    "updated_at" DATE NOT NULL
);
ALTER TABLE
    "Organization" ADD PRIMARY KEY("id");
CREATE TABLE "Parctice"(
    "id" BIGINT NOT NULL,
    "organization" BIGINT NOT NULL,
    "manager" BIGINT NOT NULL,
    "name" CHAR(255) NOT NULL,
    "city" CHAR(255) NOT NULL,
    "created-at" DATE NOT NULL,
    "updated_at" DATE NOT NULL
);
ALTER TABLE
    "Parctice" ADD PRIMARY KEY("id");
CREATE TABLE "PracticePatient"(
    "id" BIGINT NOT NULL,
    "practice" BIGINT NOT NULL,
    "patient" BIGINT NOT NULL,
    "organization" BIGINT NOT NULL,
    "created_at" DATE NOT NULL,
    "updated_at" DATE NOT NULL
);
ALTER TABLE
    "PracticePatient" ADD PRIMARY KEY("id");
CREATE TABLE "Claim"(
    "id" BIGINT NOT NULL,
    "patient" BIGINT NOT NULL,
    "organization" BIGINT NOT NULL,
    "created_at" DATE NOT NULL,
    "updated_at" DATE NOT NULL
);
ALTER TABLE
    "Claim" ADD PRIMARY KEY("id");
CREATE TABLE "Procedure"(
    "id" BIGINT NOT NULL,
    "claim" BIGINT NOT NULL,
    "service" BIGINT NOT NULL,
    "organization" BIGINT NOT NULL,
    "price_at_time" DECIMAL(8, 2) NOT NULL,
    "created_at" DATE NOT NULL,
    "updated_at" DATE NOT NULL
);
ALTER TABLE
    "Procedure" ADD PRIMARY KEY("id");
CREATE TABLE "Service"(
    "id" BIGINT NOT NULL,
    "name" BIGINT NOT NULL
);
ALTER TABLE
    "Service" ADD PRIMARY KEY("id");
CREATE TABLE "Patient"(
    "id" BIGINT NOT NULL,
    "user" BIGINT NOT NULL,
    "created_at" DATE NOT NULL,
    "updated_at" DATE NOT NULL
);
ALTER TABLE
    "Patient" ADD PRIMARY KEY("id");
CREATE TABLE "Bill"(
    "id" BIGINT NOT NULL,
    "claim" BIGINT NOT NULL,
    "organization" BIGINT NOT NULL,
    "amount" DECIMAL(8, 2) NOT NULL,
    "method" CHAR(255) NOT NULL,
    "created_at" DATE NOT NULL,
    "updated_at" DATE NOT NULL
);
ALTER TABLE
    "Bill" ADD PRIMARY KEY("id");
CREATE TABLE "Payment"(
    "id" BIGINT NOT NULL,
    "bill" BIGINT NOT NULL,
    "paid_amount" BIGINT NOT NULL,
    "change" BIGINT NOT NULL,
    "organization" BIGINT NOT NULL,
    "created_at" DATE NOT NULL,
    "updated_at" DATE NOT NULL
);
ALTER TABLE
    "Payment" ADD PRIMARY KEY("id");
CREATE TABLE "UserRole"(
    "id" BIGINT NOT NULL,
    "user" BIGINT NOT NULL,
    "role" BIGINT NOT NULL,
    "created_at" BIGINT NOT NULL,
    "updated_ap" BIGINT NOT NULL
);
ALTER TABLE
    "UserRole" ADD PRIMARY KEY("id");
CREATE TABLE "OrganizationService"(
    "id" BIGINT NOT NULL,
    "service" BIGINT NOT NULL,
    "price" DECIMAL(8, 2) NOT NULL,
    "organization" BIGINT NOT NULL,
    "created_at" DATE NOT NULL,
    "updated_at" DATE NOT NULL
);
ALTER TABLE
    "OrganizationService" ADD PRIMARY KEY("id");
CREATE TABLE "PracticeService"(
    "id" BIGINT NOT NULL,
    "org_service" BIGINT NOT NULL,
    "price" DECIMAL(8, 2) NOT NULL,
    "practice" BIGINT NOT NULL,
    "created_at" DATE NOT NULL,
    "created_at" DATE NOT NULL
);
ALTER TABLE
    "PracticeService" ADD PRIMARY KEY("id");
ALTER TABLE
    "UserRole" ADD CONSTRAINT "userrole_role_foreign" FOREIGN KEY("role") REFERENCES "Roles"("id");
ALTER TABLE
    "Bill" ADD CONSTRAINT "bill_organization_foreign" FOREIGN KEY("organization") REFERENCES "PracticePatient"("id");
ALTER TABLE
    "PracticeService" ADD CONSTRAINT "practiceservice_practice_foreign" FOREIGN KEY("practice") REFERENCES "Parctice"("id");
ALTER TABLE
    "Claim" ADD CONSTRAINT "claim_patient_foreign" FOREIGN KEY("patient") REFERENCES "PracticePatient"("id");
ALTER TABLE
    "Organization" ADD CONSTRAINT "organization_owner_foreign" FOREIGN KEY("owner") REFERENCES "User"("id");
ALTER TABLE
    "Parctice" ADD CONSTRAINT "parctice_manager_foreign" FOREIGN KEY("manager") REFERENCES "User"("id");
ALTER TABLE
    "Parctice" ADD CONSTRAINT "parctice_organization_foreign" FOREIGN KEY("organization") REFERENCES "Organization"("id");
ALTER TABLE
    "Claim" ADD CONSTRAINT "claim_organization_foreign" FOREIGN KEY("organization") REFERENCES "Organization"("id");
ALTER TABLE
    "Payment" ADD CONSTRAINT "payment_organization_foreign" FOREIGN KEY("organization") REFERENCES "Organization"("id");
ALTER TABLE
    "Bill" ADD CONSTRAINT "bill_claim_foreign" FOREIGN KEY("claim") REFERENCES "Claim"("id");
ALTER TABLE
    "Service" ADD CONSTRAINT "service_id_foreign" FOREIGN KEY("id") REFERENCES "OrganizationService"("service");
ALTER TABLE
    "Procedure" ADD CONSTRAINT "procedure_service_foreign" FOREIGN KEY("service") REFERENCES "PracticeService"("id");
ALTER TABLE
    "Bill" ADD CONSTRAINT "bill_id_foreign" FOREIGN KEY("id") REFERENCES "Payment"("id");
ALTER TABLE
    "PracticePatient" ADD CONSTRAINT "practicepatient_organization_foreign" FOREIGN KEY("organization") REFERENCES "Organization"("id");
ALTER TABLE
    "Patient" ADD CONSTRAINT "patient_user_foreign" FOREIGN KEY("user") REFERENCES "User"("id");
ALTER TABLE
    "PracticePatient" ADD CONSTRAINT "practicepatient_patient_foreign" FOREIGN KEY("patient") REFERENCES "Patient"("id");
ALTER TABLE
    "Procedure" ADD CONSTRAINT "procedure_claim_foreign" FOREIGN KEY("claim") REFERENCES "Claim"("id");
ALTER TABLE
    "OrganizationService" ADD CONSTRAINT "organizationservice_organization_foreign" FOREIGN KEY("organization") REFERENCES "Organization"("id");
ALTER TABLE
    "Procedure" ADD CONSTRAINT "procedure_organization_foreign" FOREIGN KEY("organization") REFERENCES "Organization"("id");
ALTER TABLE
    "OrganizationService" ADD CONSTRAINT "organizationservice_id_foreign" FOREIGN KEY("id") REFERENCES "PracticeService"("org_service");
ALTER TABLE
    "UserRole" ADD CONSTRAINT "userrole_user_foreign" FOREIGN KEY("user") REFERENCES "User"("id");
ALTER TABLE
    "Bill" ADD CONSTRAINT "bill_organization_foreign" FOREIGN KEY("organization") REFERENCES "Organization"("id");