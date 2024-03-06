import numpy as np

def create_sequences(data, sequence_length):
    """
    Create sequences from the provided data.

    :param data: A 2D numpy array where each row is [classId, x_pos, y_pos, timestamp, health, gameid]
    :param sequence_length: The number of time steps to be included in each sequence
    :return: X, y where X is a 3D numpy array for the input sequences and y is a 2D numpy array for the output sequences
    """
    X, y = [], []

    for i in range(len(data) - sequence_length):
        seq = data[i:i + sequence_length]  # Extract sequence
        target = data[i + sequence_length]  # Extract target value

        X.append(seq)
        y.append(target)

    return np.array(X), np.array(y)

# Example usage
data = np.array([
    # [classId, x_pos, y_pos, timestamp, health, gameid]
    [1, 10, 20, 1, 100, 1],
    [1, 11, 22, 2, 95, 1],
    [1, 12, 24, 3, 90, 1],
    # ... (more data)
])

sequence_length = 2  # Example sequence length

X, y = create_sequences(data, sequence_length)
X.shape, y.shape  # Check the shapes of the created sequences and targets
