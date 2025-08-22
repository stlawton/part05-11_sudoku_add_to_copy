def copy_and_add(sudolu: list, row_no: int, column_no: int, number: int):
  new_sudoku = []
  for item in sudoku:
    new_sudoku.append(item)
  new_sudoku[row_no][column_no] = number
  return new_sudoku
