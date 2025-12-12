import collections

def lmap(f, l): return list(map(f, l))

class PresentShape:
    """Represents a unique present shape and its properties."""
    def __init__(self, index, definition_lines):
        self.index = index
        self.offsets = []
        for r, row in enumerate(definition_lines):
            for c, char in enumerate(row):
                if char == '#':
                    self.offsets.append((r, c))
        
        self.density = len(self.offsets) 


MIN_BLOCK_SIZE = 3 



def calculate_definitely_fitting(filename="data.txt"):
    """
    Reads input and returns the count of regions that are guaranteed to fit 
    (the 'Definitely' category, based on non-overlapping 3x3 blocks).
    """

    try:
        with open(filename) as r:
            s = r.read().rstrip()
            lgroups = s.split('\n\n')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0

    
    presents_data = lgroups[:-1]
    
    present_objects = {}
    current_index = 0
    for block in presents_data:
        lines = block.strip().split('\n')
        if not lines: continue
        
        if lines[0].endswith(':'):
            index = int(lines[0].strip()[:-1])
            definition_lines = lines[1:]
        else:
            index = current_index 
            definition_lines = lines
        
        present_objects[index] = PresentShape(index, definition_lines)
        current_index += 1

    
    regions = lgroups[-1].split('\n')
    
    definitely_count = 0

    for region_line in regions:
        region_line = region_line.strip()
        if not region_line: continue

        
        try:
            xy, counts_str = region_line.split(": ")
            counts_list = lmap(int, counts_str.split(' '))
            x, y = lmap(int, xy.split('x'))
        except ValueError:
            continue

        
        
        total_presents = sum(counts_list)
        
        
        available_blocks = (x // MIN_BLOCK_SIZE) * (y // MIN_BLOCK_SIZE)
        
        
        if total_presents <= available_blocks:
            definitely_count += 1
        
    return definitely_count


def_result = calculate_definitely_fitting(filename='data.txt')

print(f"The number of regions that are guaranteed to fit is: {def_result}")