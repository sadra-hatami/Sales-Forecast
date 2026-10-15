    import pandas as pd
    import numpy as np
    from datetime import datetime, timedelta
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error
    import math
    
    def load_and_preprocess_data(filepath):
        try:
            # Attempt to read the file with UTF-8 encoding
            data = pd.read_csv(filepath, encoding='utf-8')
        except UnicodeDecodeError:
            # If UTF-8 fails, try reading with ISO-8859-1
            data = pd.read_csv(filepath, encoding='ISO-8859-1')
        except FileNotFoundError:
            print(f"Error: The file {filepath} was not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
        # Fill missing values and convert dates
        data.fillna(method='ffill', inplace=True)
        data['Date'] = pd.to_datetime(data['Date'])
        data['Year'] = data['Date'].dt.year
        data['Month'] = data['Date'].dt.month
        data['Day'] = data['Date'].dt.day
        
        # Convert categorical data to numerical using one-hot encoding
        data = pd.get_dummies(data, columns=['Advertising'])
        return data
    
    def prepare_features(data):
        if data is None:
            return None, None
        # Select features and target variable
        X = data[['Year', 'Month', 'Day', 'Price', 'Advertising_High', 'Advertising_Low', 'Advertising_Medium']]
        y = data['Sales']
        return X, y
    
    def train_model(X_train, y_train):
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        model = LinearRegression()
        model.fit(X_train_scaled, y_train)
        return model, scaler
    
    def evaluate_model(model, scaler, X_test, y_test):
        X_test_scaled = scaler.transform(X_test)
        y_pred = model.predict(X_test_scaled)
        mse = mean_squared_error(y_test, y_pred)
        rmse = math.sqrt(mse)
        print(f'Mean Squared Error: {mse}')
        print(f'Root Mean Squared Error: {rmse}')
    
    if __name__ == "__main__":
        filepath = 'C:/path/to/your/sales_data.csv'  # Update with the correct path to your CSV file
        data = load_and_preprocess_data(filepath)
        if data is not None:
            X, y = prepare_features(data)
            if X is not None and y is not None:
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                model, scaler = train_model(X_train, y_train)
                evaluate_model(model, scaler, X_test, y_test)
            else:
                print("Feature preparation failed.")
        else:
            print("Data loading failed, script will terminate.")
    

