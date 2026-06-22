class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}
        
        # Iterate through each cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                
                # Skip empty cells
                if cell == ".":
                    continue
                
                # TODO: Get the box coordinates using integer division
                # box_key = (r // 3, c // 3)
                box_key = (r // 3, c // 3)
                
                # TODO: Initialize sets in the dictionaries if they don't exist
                # if r not in rows:
                #     rows[r] = set()
                # etc...
                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if box_key not in boxes:
                    boxes[box_key] = set()
                
                # TODO: Check if the cell value is already in the row/col/box
                # If it is, return False
                if cell in rows[r] or cell in cols[c] or cell in boxes[box_key]:
                    return False
                # TODO: Add the cell value to the row/col/box sets
        
                rows[r].add(cell)
                cols[c].add(cell)
                boxes[box_key].add(cell)


        return True