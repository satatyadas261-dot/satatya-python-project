import numpy as np
def main():
    marks = np.array([78, 85, 92, 67, 74, 88, 81, 95, 70, 83])
    print("==== Internal Marks Analysis ====")
    print("Marks:", marks)
    print("Sorted Marks:", np.sort(marks))
    print("Total Marks:", np.sum(marks))
    print("Mean:", np.mean(marks))
    print("Median:", np.median(marks))
    print("Standard Deviation:", np.std(marks))
    print("Variance:", np.var(marks))
    print("Maximum:", np.max(marks))
    print("Minimum:", np.min(marks))
if __name__ == "__main__":
    main()
