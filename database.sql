CREATE DATABASE customer_support;

CREATE TABLE customers (
  customer_id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  phone VARCHAR(15)
);

INSERT INTO customers (name, email, phone)
VALUES
('John Doe', 'john@example.com', '123-456-7890'),
('Jane Smith', 'jane@example.com', '987-654-3210');
INSERT INTO knowledge_base (category, question, solution) VALUES
('Billing', 'How to check my bill?', 'Log in to your account and navigate to the Billing section.'),
('Technical Support', 'My internet is not working.', 'Please restart your router.'),
('General Inquiry', 'What are your business hours?', 'We are open from 9 AM to 6 PM, Monday to Friday.');