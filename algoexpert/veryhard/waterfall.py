def waterfallStreams(array, source):
    # Write your code here.
    row_above = array[0][:]
    row_above[source] = -1

    for row in range(1, len(array)):
        current_row = array[row][:]
        for idx in range(len(row_above)):
            value_above = row_above[idx]

            has_water_above = value_above < 0
            has_block = current_row[idx] == 1
            if not has_water_above:
                continue
            if not has_block:
                current_row[idx] += value_above
                continue

            split_water = value_above / 2
            right_idx = idx
            while right_idx + 1 < len(row_above):
                right_idx += 1
                if row_above[right_idx] == 1:
                    break
                if current_row[right_idx] != 1:
                    current_row[right_idx] += split_water
                    break
            left_idx = idx
            while left_idx - 1 >= 0:
                left_idx -= 1
                if row_above[left_idx] == 1:
                    break
                if current_row[left_idx] != 1:
                    current_row[left_idx] += split_water
                    break
        row_above = current_row

    final_percentage = [num * -100 for num in row_above]
    return final_percentage

