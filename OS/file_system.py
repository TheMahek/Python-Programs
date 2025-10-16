class FileSystem:
    def __init__(self, total_blocks=20, block_size=1):
        self.total_blocks = total_blocks
        self.blocks = block_size
        self.free_blocks = [True] * total_blocks  # True = free, False = occupied
        self.directory = {}  # (filename: {"size": size, "blocks": [block indices]})

    def allocate_blockd(self, num_blocks):
        """Allocate free blocks for a file. """
        allocated = []
        for i in range(self.total_blocks):
            if self.free_blocks[i]:
                allocated.append(i)
                if len(allocated) == num_blocks:
                    for blk in allocated:
                        self.free_blocks[blk] = False
                    return allocated
        return None

    def create(self, filename, size):
        """Create a file with given size(in blocks)."""
        if filename in self.directory:
            print(f"Error: File '{filename}' already exists.")
            return

        num_blocks = (size + self.blocks) // self.blocks
        allocated = self.allocate_blockd(num_blocks)

        if allocated is None:
            print("Error: Not enough space to allocate file.")
        else:
            self.directory[filename] = {"size": size, "blocks": allocated}

    def read(self, filename):
        """Read file info."""
        if filename not in self.directory:
            print(f"Error: File '{filename}' not found.")
            return
        file_info = self.directory[filename]
        print(f"Reading file '{filename}':")
        print(f" -> Size: {file_info['size']} units")
        print(f" -> Books: {file_info['blocks']}")

    def delete(self, filename):
        """Delete a file and free its blocks."""
        if filename not in self.directory:
            print(f"File '{filename}' not found.")
            return
        for blk in self.directory[filename]['blocks']:
            self.free_blocks[blk] = True
        del self.directory[filename]
        print(f"File '{filename}' deleted successfully.")

    def show_directory(self):
        """Show all files and their block allocations."""
        if not self.directory:
            print("Directory is empty.")
            return
        print("Directory contents.")
        for fname, info in self.directory.items():
            print(f" -> {fname}:size={info['size']}, blocks={info['blocks']}")

    def show_free_blocks(self):
        """Show free/Used block status."""
        print("Block allocation status.")
        print("".join(["F" if free else "U" for free in self.free_blocks]))
