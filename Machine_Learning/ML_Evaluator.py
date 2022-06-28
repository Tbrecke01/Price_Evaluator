# dependencies
import pandas as pd
import joblib


def evaluate_price(product_id, date, price, condition, merchant):
    # read in user input from website -- TEST/HYPOTHETICAL INPUT FOR NOW
    user_input = pd.DataFrame({'id': product_id,
                            'quarter': pd.DateTimeIndex(pd.to_datetime(date)).quarter,
                            'month': pd.DateTimeIndex(pd.to_datetime(date)).quarter,
                            'prices_amountmin': price,
                            'prices_condition': condition,
                            'prices_merchant': merchant
                            }, index=[0])

    # Load encoders, scaler, and machine learning model:
    id_encoder = joblib.load('ID_Encoder.sav')
    cond_encoder = joblib.load('Condition_Encoder.sav')
    merch_encoder = joblib.load('Merchant_Encoder.sav')
    X_scaler = joblib.load('Data_Scaler.sav')
    ml_model = joblib.load('ML_Model.sav')

    # encode user input with id_encoder and merch_encoder
    user_input_encoded = user_input.copy()
    user_input_encoded['id'] = id_encoder.transform(user_input['id'])
    user_input_encoded['prices_condition'] = cond_encoder.transform(user_input['prices_condition'])
    user_input_encoded['prices_merchant'] = merch_encoder.transform(user_input['prices_merchant'])

    # Use X_scaler to transform encoded user input
    user_input_encoded_scaled = X_scaler.transform(user_input_encoded)

    # Return ml model prediction (True indicates price is likely discounted / False indicates price is likely not discounted)
    return ml_model.predict(user_input_encoded_scaled)[0]

