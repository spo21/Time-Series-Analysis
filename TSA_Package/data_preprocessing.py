from sklearn.preprocessing import MinMaxScaler

def analyse_data(data):

    data['MA_5'] = data['Close'].rolling(window=5).mean()
    data['STD_5'] = data['Close'].rolling(window=5).std()

    print("Analyse data end function")


def normalise_data(data):
    
    scaler = MinMaxScaler()
    data['Close_scaled'] = scaler.fit_transform(data[['Close']])


# Split data into train and test data
def data_split(data):
    train_size = int(len(data) * 0.8)
    train, test = data[:train_size], data[train_size:]
    return train, test

def interpolate(data):
    data['Close'] = data['Close'].interpolate()