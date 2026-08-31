# FinGuard — Banking Transaction & Fraud Intelligence Platform

## Project Overview
FinGuard is a banking transaction and fraud intelligence platform focused on analyzing banking data, understanding transaction behavior, and investigating potentially suspicious activity.

## Business Problem
Royal Bank of Canada (RBC) processes a large volume of financial transactions across its customers and accounts. With such high transaction activity, identifying unusual behavior and potentially fraudulent transactions can be challenging without a structured analytical system.

FinGuard aims to provide a centralized intelligence platform for analyzing transaction behavior, investigating suspicious activity, understanding fraud patterns, and generating actionable insights that can support fraud analysts, risk teams, and banking management in their decision-making.


## Business Objectives
FinGuard is designed to achieve the following objectives:

1. **Understand Transaction Activity** — Analyze transaction volume, amounts, types, channels, locations, timing, and other transaction characteristics to establish a clear view of banking activity.
2. **Analyze Customer and Account Behavior** — Examine customer and account activity to identify behavioral patterns, activity levels, and potentially unusual behavior.
3. **Investigate Suspicious Activity** — Analyze fraud patterns and suspicious transactions across transaction types, locations, merchants, channels, time periods, customers, and accounts.
4. **Measure Financial Impact** — Quantify transaction values, fraudulent transaction amounts, and other financial activity to understand potential financial exposure and operational impact.
5. **Generate Actionable Intelligence** — Transform analytical findings into meaningful insights and recommendations that can support fraud analysts, risk teams, and banking management in their decision-making.


## Stakeholders
FinGuard is designed to provide analytical intelligence to multiple banking stakeholders, with each stakeholder group using the platform for different decision-making needs.

### Fraud Analysts
Investigate suspicious transactions, customer behavior, and fraud patterns.

### Risk Team
Identify areas of transaction and financial risk and analyze potentially high-risk activity.

### Bank Management
Monitor overall transaction activity, fraud trends, financial impact, and key risk indicators.

### Compliance Team
Analyze unusual transaction patterns and support investigations requiring additional review.

### Data Science / Analytics Team
Explore banking data, develop analytical methods, and eventually build statistical and machine-learning capabilities.


## Data Requirements
FinGuard requires banking data that can support transaction analysis, customer and account behavior analysis, fraud investigation, and financial intelligence.
The initial data requirements include:

* **Customers** — Customer identity, demographic, status, and relationship information.
* **Accounts** — Account information, account type, status, balances, and customer relationships.
* **Transactions** — Transaction identifiers, dates, amounts, types, status, payment methods, channels, and fraud indicators.
* **Merchants** — Merchant identity, category, and location information.
* **Locations** — Geographic information associated with customers, merchants, and transactions.
* **Cards / Payment Information** — Information that allows transaction activity to be analyzed by card or payment method where applicable.

The final data model and available fields will be determined during the database and dataset design stages.


## Data Model
FinGuard uses a relational data model designed to organize banking information into distinct entities while minimizing unnecessary data duplication and maintaining clear relationships between records.

### Core Entities
#### Customer
Represents an individual banking customer and contains customer-level identification, demographic, geographic, and relationship information.

#### Account
Represents a banking account associated with a customer and contains account-level information such as account type, status, opening date, and balance.

#### Transaction
Represents a financial transaction associated with an account. Transaction-level information includes transaction date, amount, transaction type, payment method, channel, status, merchant association, and fraud indication.

#### Merchant
Represents a merchant associated with transactions and contains merchant identification, category, and geographic information.

### Core Relationships
### Entity Relationship Diagram

```text
┌─────────────────────────┐
│        CUSTOMER         │
├─────────────────────────┤
│ PK customer_id          │
│ first_name              │
│ last_name               │
│ date_of_birth           │
│ gender                  │
│ city                    │
│ province                │
│ country                 │
│ customer_since          │
│ customer_status         │
└────────────┬────────────┘
             │
             │ 1 : M
             ▼
┌─────────────────────────┐
│         ACCOUNT         │
├─────────────────────────┤
│ PK account_id           │
│ FK customer_id          │
│ account_type            │
│ account_open_date       │
│ account_status          │
│ current_balance         │
└────────────┬────────────┘
             │
             │ 1 : M
             ▼
┌─────────────────────────┐
│       TRANSACTION       │
├─────────────────────────┤
│ PK transaction_id       │
│ FK account_id           │
│ FK merchant_id          │
│ transaction_date        │
│ transaction_type        │
│ amount                  │
│ payment_method          │
│ channel                 │
│ status                  │
│ is_fraud                │
└────────────┬────────────┘
             │
             │ M : 1
             ▼
┌─────────────────────────┐
│        MERCHANT         │
├─────────────────────────┤
│ PK merchant_id          │
│ merchant_name           │
│ merchant_category       │
│ merchant_city           │
│ merchant_province       │
│ merchant_country        │
└─────────────────────────┘
```

### Relational Schema
The current relational schema consists of four core entities:

**Customer**
* `customer_id` — Primary Key
* `first_name`
* `last_name`
* `date_of_birth`
* `gender`
* `city`
* `province`
* `country`
* `customer_since`
* `customer_status`

**Account**
* `account_id` — Primary Key
* `customer_id` — Foreign Key → Customer
* `account_type`
* `account_open_date`
* `account_status`
* `current_balance`

**Merchant**
* `merchant_id` — Primary Key
* `merchant_name`
* `merchant_category`
* `merchant_city`
* `merchant_province`
* `merchant_country`

**Transaction**
* `transaction_id` — Primary Key
* `account_id` — Foreign Key → Account
* `merchant_id` — Foreign Key → Merchant
* `transaction_date`
* `transaction_type`
* `amount`
* `payment_method`
* `channel`
* `status`
* `is_fraud`

The schema is subject to refinement during implementation as the dataset structure and analytical requirements are finalized.

### PostgreSQL Architecture
FinGuard will use PostgreSQL as the relational database layer for V1.
The initial database structure will use a dedicated `finguard` database with the default public schema.
The core tables will include:
* customers
* accounts
* merchants
* transactions
The tables will be connected through primary and foreign key relationships to maintain referential integrity.

The planned dependency structure is:
```text
Customer
   ↓
Account
   ↓
Transaction
   ↑
Merchant
```
Data will be loaded in dependency order so that referenced records exist before dependent transaction records are inserted.
Database credentials will be managed outside the source code and will not be committed to the repository.



### Design Principles
* Each core entity maintains its own attributes.
* Primary keys uniquely identify records within each entity.
* Foreign keys establish relationships between related entities.
* Customer information is associated with accounts rather than being redundantly stored within transactions.
* Merchant information is maintained separately from transaction records.
* Location information remains context-specific until the final dataset determines whether further normalization is appropriate.
The final relational schema may evolve during implementation as the dataset and analytical requirements are finalized.


## Dataset Strategy
FinGuard will use a synthetic banking dataset designed to represent realistic customer, account, merchant, and transaction activity within a large financial institution.
The dataset will be designed to support transaction analysis, customer and account behavior analysis, fraud investigation, and financial intelligence while also providing realistic data-quality challenges for the analytical workflow.
The dataset structure and scale will be finalized during the data and database implementation stages.

> **Disclaimer:** FinGuard is an independent educational project using synthetic data. It is not affiliated with, sponsored by, or based on confidential data from Royal Bank of Canada (RBC).


## Version 1 Scope
The first version of FinGuard focuses on banking transaction analytics and fraud investigation using the project's current analytical technology stack.

### V1 Includes
* Synthetic banking data generation and preparation
* Relational database design using PostgreSQL
* Data ingestion and data-quality analysis
* SQL-based transaction, customer, account, fraud, and financial analysis
* Python and Pandas-based analytical workflows
* Exploratory data analysis
* Statistical exploration using descriptive analysis
* Fraud and suspicious-activity investigation
* Data visualization using Matplotlib, Seaborn, and Plotly
* Business insights and actionable recommendations

### V1 Excludes
Advanced capabilities such as machine-learning-based fraud prediction, advanced statistical modeling, APIs, deep learning, cloud deployment, and MLOps are outside the initial scope and will be introduced in future versions as the project evolves.


## Development Principles
FinGuard is being developed as a long-term professional project with a focus on practical problem solving, analytical reasoning, and maintainable implementation.

### Business-First Approach
Development begins with a defined business problem and business objectives. Data, analysis, and technical implementation are selected based on the questions the platform needs to answer.

### Purpose-Driven Technology
Technical concepts and design patterns are introduced when they provide a genuine purpose within the project. Functions, classes, modules, advanced SQL, and other technologies will be used when they improve the implementation rather than being added solely for demonstration.

### Progressive Development
FinGuard is designed as an extensible platform that can evolve as new analytical methods and technologies are introduced.

### Practical Complexity
The project prioritizes correctness, readability, maintainability, and explainability over unnecessary complexity.

### Actionable Analysis
Analytical work should go beyond presenting results. Findings should be interpreted in their business context and, where appropriate, translated into actionable recommendations.

## Version 1 Definition
FinGuard V1 is a banking transaction analytics and fraud intelligence platform that uses synthetic banking data, PostgreSQL, Python, Pandas, NumPy, and visualization tools to analyze customer, account, transaction, financial, and suspicious-activity patterns and transform those findings into actionable business intelligence.


## Project Status
**Version:** V1  
**Status:** In Development  
**Current Phase:** Data Preparation & Ingestion