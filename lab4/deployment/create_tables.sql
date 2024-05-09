-- create tables
CREATE TABLE job_title (
    job_title_id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE department (
    department_id SERIAL PRIMARY KEY,
    city VARCHAR(256),
    street VARCHAR(256),
    house VARCHAR(256),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE employee (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(256) NOT NULL,
    last_name VARCHAR(256),
    middle_name VARCHAR(256) NOT NULL,
    birth_date TIMESTAMP,
    sex CHAR(1),
    phone VARCHAR(11) NOT NULL,
    email VARCHAR(128) NOT NULL,
    hire_date TIMESTAMP,
    note TEXT,
    image_path VARCHAR(1024),
    job_title_id INTEGER NOT NULL REFERENCES job_title (job_title_id),
    department_id INTEGER REFERENCES department (department_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP
);


-- Add ON UPDATE trigger
CREATE OR REPLACE FUNCTION update_timestamp() RETURNS TRIGGER
LANGUAGE plpgsql
AS
$$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$;

CREATE TRIGGER title_updated_at
  BEFORE UPDATE
  ON job_title
  FOR EACH ROW
  EXECUTE PROCEDURE update_timestamp();

CREATE TRIGGER employee_updated_at
  BEFORE UPDATE
  ON employee
  FOR EACH ROW
  EXECUTE PROCEDURE update_timestamp();

CREATE TRIGGER department_updated_at
  BEFORE UPDATE
  ON department
  FOR EACH ROW
  EXECUTE PROCEDURE update_timestamp();

