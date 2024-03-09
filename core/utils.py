def calculate_cmhc_premium(loan_amount, property_value):
    # Calculate loan-to-value (LTV) ratio
    loan_to_value_ratio = (loan_amount / property_value) * 100

    # Determine the premium rates based on the loan-to-value ratio
    if loan_to_value_ratio <= 65:
        premium_rate = 0.60
        portability_rate = 0.60
    elif 65 < loan_to_value_ratio <= 75:
        premium_rate = 1.70
        portability_rate = 5.90
    elif 75 < loan_to_value_ratio <= 80:
        premium_rate = 2.40
        portability_rate = 6.05
    elif 80 < loan_to_value_ratio <= 85:
        premium_rate = 2.80
        portability_rate = 6.20
    elif 85 < loan_to_value_ratio <= 90:
        premium_rate = 3.10
        portability_rate = 6.25
    elif 90 < loan_to_value_ratio <= 95:
        premium_rate = 4.00
        portability_rate = 6.30
    else:
        raise ValueError("Loan-to-value ratio exceeds 95% or is invalid.")

    # # Calculate premiums
    # premium_on_total_loan = loan_amount * (premium_rate / 100)
    # premium_on_increase_to_loan_amount = loan_amount * (portability_rate / 100)

    return premium_rate/100, portability_rate/100