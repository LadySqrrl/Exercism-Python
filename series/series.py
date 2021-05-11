def slices(series, length):
    if len(series) < 1:
        raise ValueError("Series cannot be empty")

    if length < 1:
        raise ValueError("Length cannot be less than 1")

    if length > len(series):
        raise ValueError("Length cannot bee longer than the series")

    slice_list = []
    i = 0

    while i <= len(series)-length:
        end = i + length
        slice_list.append(series[i:end])
        i += 1

    return slice_list