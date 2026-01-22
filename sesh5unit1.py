import numpy as np

def write_sin_table(filename='sin_table.txt', num_points=1000):
    """
    Writes a table of sin(x) vs x to a file.
    
    Parameters:
    filename (str): Name of the output file
    num_points (int): Number of points between 0 and 2
    """
    # Create an array of x values from 0 to 2
    x_values = np.linspace(0, 2, num_points)
    
    # Open file for writing
    with open(filename, 'w') as f:
        # Write header
        f.write("x\t\tsin(x)\n")
        
        # Write each x and sin(x) value
        for x in x_values:
            f.write(f"{x:.6f}\t{np.sin(x):.6f}\n")

def main():
    # Write the sin table to a file
    write_sin_table()
    print("Table of sin(x) vs x has been written to 'sin_table.txt'.")

# Run the program
if __name__ == "__main__":
    main()
