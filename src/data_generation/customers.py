import numpy as np
import pandas as pd

FIRST_NAMES = [
    "James",
    "John",
    "Michael",
    "David",
    "Robert",
    "William",
    "Daniel",
    "Sarah",
    "Emily",
    "Jessica",
    "Olivia",
    "Sophia",
    "Emma",
    "Mia",
    "Ava",
]
LAST_NAMES = [
    "Smith",
    "Brown",
    "Wilson",
    "Taylor",
    "Anderson",
    "Thomas",
    "Jackson",
    "White",
    "Harris",
    "Martin",
    "Thompson",
    "Garcia",
    "Clark",
    "Lewis",
    "Lee",
]
PROVINCES = [
    "Ontario",
    "Quebec",
    "British Columbia",
    "Alberta",
    "Manitoba",
    "Saskatchewan",
    "Nova Scotia",
    "New Brunswick",
    "Newfoundland and Labrador",
    "Prince Edward Island",
]
PROVINCE_PROBABILITIES = [
    0.40,
    0.20,
    0.15,
    0.12,
    0.04,
    0.03,
    0.02,
    0.02,
    0.01,
    0.01,
]
PROVINCE_CITIES = {
    "Ontario": [
        "Toronto",
        "Brampton",
        "Mississauga",
        "Ottawa",
        "Hamilton",
    ],
    "Quebec": [
        "Montreal",
        "Quebec City",
        "Laval",
    ],
    "British Columbia": [
        "Vancouver",
        "Surrey",
        "Victoria",
    ],
    "Alberta": [
        "Calgary",
        "Edmonton",
        "Red Deer",
    ],
    "Manitoba": [
        "Winnipeg",
    ],
    "Saskatchewan": [
        "Saskatoon",
        "Regina",
    ],
    "Nova Scotia": [
        "Halifax",
    ],
    "New Brunswick": [
        "Moncton",
        "Saint John",
    ],
    "Newfoundland and Labrador": [
        "St. John's",
    ],
    "Prince Edward Island": [
        "Charlottetown",
    ],
}


def generate_customers(n_customers, rng):
    #unique id of the customer(PK)
    customer_ids = np.arange(100001, 100001 + n_customers)

    #first name of the customer
    first_names = rng.choice(FIRST_NAMES, size=n_customers)

    #last name of the customer
    last_names = rng.choice(LAST_NAMES, size=n_customers)

    #gender of the customer
    genders= rng.choice(["Male", "Female"], size=n_customers, p=[0.5, 0.5])

    #name of the province of customer
    provinces= rng.choice(PROVINCES, size=n_customers, p=PROVINCE_PROBABILITIES)

    #name of the city of customer
    cities= [rng.choice(PROVINCE_CITIES[province])for province in provinces]

    #which country customer is from
    countries= np.full(n_customers,"Canada")

    #customer status
    customer_status= rng.choice(["Active", "Inactive", "Closed"], size=n_customers, p=[0.90, 0.07, 0.03])

    #date of birth
    start_date = np.datetime64("1944-01-01")
    end_date = np.datetime64("2006-12-31")
    birth_days = rng.integers(0,(end_date - start_date).astype("timedelta64[D]").astype(int) + 1, size=n_customers)
    date_of_birth = start_date + birth_days.astype("timedelta64[D]")

    # Generate customer onboarding dates
    today = pd.Timestamp("2026-08-31")
    birth_dates = pd.to_datetime(date_of_birth)
    eighteenth_birthdays = birth_dates + pd.DateOffset(years=18)
    customer_since = pd.to_datetime([rng.choice(pd.date_range(birthday, today))for birthday in eighteenth_birthdays])


    customers = pd.DataFrame({
    "customer_id": customer_ids,
    "first_name": first_names,
    "last_name": last_names,
    "date_of_birth": date_of_birth,
    "gender": genders,
    "city": cities,
    "province": provinces,
    "country": countries,
    "customer_since": customer_since,
    "customer_status": customer_status,
    })

    return customers
    
#customer validation
def validate_customers(customers):
    assert customers["customer_id"].is_unique
    assert customers["customer_id"].notna().all()
    assert customers["first_name"].notna().all()
    assert customers["last_name"].notna().all()
    assert customers["province"].notna().all()
    assert customers["city"].notna().all()
    assert customers["country"].eq("Canada").all()
    assert customers["customer_status"].isin(
        {"Active", "Inactive", "Closed"}
    ).all()

    assert customers["customer_since"].le(
        pd.Timestamp("2026-08-31")
    ).all()

    eighteenth_birthdays = (
        customers["date_of_birth"]
        + pd.DateOffset(years=18)
    )

    assert (
        customers["customer_since"]
        >= eighteenth_birthdays
    ).all()

    return True

#Testing
if __name__ == "__main__":
    rng = np.random.default_rng(42)
    customers = generate_customers(10000, rng)
    customers.to_csv("data/raw/customers.csv", index=False)
