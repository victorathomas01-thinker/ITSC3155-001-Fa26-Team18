USE sandwich_maker_api;

-- 1. Update orders
ALTER TABLE orders
    MODIFY COLUMN order_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ADD COLUMN customer_id INT NULL,
    ADD COLUMN promotion_id INT NULL,
    ADD COLUMN tracking_number VARCHAR(60) NULL,
    ADD COLUMN order_status VARCHAR(30) NOT NULL DEFAULT 'pending',
    ADD COLUMN fulfillment_method VARCHAR(20) NULL,
    ADD COLUMN delivery_address VARCHAR(300) NULL,
    ADD COLUMN total_price DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    ADD UNIQUE KEY uq_orders_tracking_number (tracking_number),
    ADD KEY ix_orders_customer_id (customer_id),
    ADD CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id) REFERENCES customers(id),
    ADD CONSTRAINT fk_orders_promotion
        FOREIGN KEY (promotion_id) REFERENCES promotions(id),
    ADD CONSTRAINT ck_order_total CHECK (total_price >= 0);

-- 2. Update order_details
ALTER TABLE order_details
    MODIFY COLUMN order_id INT NOT NULL,
    MODIFY COLUMN sandwich_id INT NOT NULL,
    ADD COLUMN unit_price DECIMAL(10,2) NULL,
    ADD CONSTRAINT ck_detail_amount CHECK (amount > 0);

-- 3. Update recipes
ALTER TABLE recipes
    MODIFY COLUMN sandwich_id INT NOT NULL,
    MODIFY COLUMN resource_id INT NOT NULL,
    MODIFY COLUMN amount DECIMAL(10,2) NOT NULL,
    ADD CONSTRAINT uq_recipe_ingredient
        UNIQUE (sandwich_id, resource_id),
    ADD CONSTRAINT ck_recipe_amount CHECK (amount > 0);

-- 4. Update resources
ALTER TABLE resources
    MODIFY COLUMN amount DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    ADD COLUMN unit VARCHAR(30) NOT NULL DEFAULT 'units',
    ADD CONSTRAINT ck_resource_amount CHECK (amount >= 0);

-- 5. Update sandwiches
ALTER TABLE sandwiches
    MODIFY COLUMN sandwich_name VARCHAR(100) NOT NULL,
    MODIFY COLUMN price DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    ADD COLUMN calories INT NULL,
    ADD COLUMN food_category VARCHAR(80) NULL,
    ADD COLUMN description VARCHAR(500) NULL,
    ADD CONSTRAINT ck_sandwich_price CHECK (price >= 0),
    ADD CONSTRAINT ck_sandwich_calories
        CHECK (calories IS NULL OR calories >= 0);
