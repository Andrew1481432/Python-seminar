def delete_empty_rows(table):
    newTable = []
    for i, row in enumerate(table):
        result = []
        for j, column in enumerate(row):
            if column is not None:
                result.append(column)
        if len(result) > 0:
            newTable.append(result)
    return newTable


def change_value(table):
    for i, row in enumerate(table):
        value = float(row[0])
        rounded_value = "{:.3f}".format(value)
        row[0] = "{:0<3}".format(rounded_value)
        row[1] = row[1].replace('-', '.')
        if row[2] == "Не выполнено":
            row[2] = "нет"
        elif row[2] == "Выполнено":
            row[2] = "да"
    return table


def delete_duplicate_columns(table):
    for row in table:
        del row[2]
    return table


def remove_duplicate_rows(table):
    seen = {}
    result = []
    for i, row in enumerate(table):
        row_key = tuple(row)
        if row_key not in seen:
            seen[row_key] = i
            result.append(row)
    return result


def split_column(table):
    new_table = [row[0].split('|') + row[1:] for row in table]
    return new_table


def main(table):
    return change_value(
        split_column(
            remove_duplicate_rows(
                delete_duplicate_columns(
                    delete_empty_rows(table)
                )
            )
        )
    )


# print(main([
#     [
#         "0.5|20-04-00", None, "Не выполнено", "Не выполнено"
#     ],
#     [
#         "0.1|09-06-03", None, "Не выполнено", "Не выполнено"
#     ],
#     [
#         "0.1|09-06-03", None, "Не выполнено", "Не выполнено"
#     ],
#     [
#         "0.1|09-06-03", None, "Не выполнено", "Не выполнено"
#     ],
#     [
#         "0.3|13-03-99", None, "Не выполнено", "Не выполнено"
#     ]
# ]))


print(main([['0.5|20-04-00', None, 'Не выполнено', 'Не выполнено'], ['0.1|09-06-03', None, 'Не выполнено', 'Не выполнено'], [None, None, None, None], ['0.1|09-06-03', None, 'Не выполнено', 'Не выполнено'], ['0.1|09-06-03', None, 'Не выполнено', 'Не выполнено'], ['0.3|13-03-99', None, 'Не выполнено', 'Не выполнено']]))
