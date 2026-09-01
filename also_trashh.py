




    

    squared = list(map(lambda x: x**2, numbers))
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    sum_all = reduce(lambda x, y: x + y, numbers)
    print(f"Squared: {squared}")
    print(f"Evens: {evens}")
    print(f"Sum: {sum_all}")
    
    print("\n" + "=" * 50)
    print("PROGRAM COMPLETED SUCCESSFULLY")
    print("=" * 50)

# ====== SECTION 9: SCRIPT ENTRY POINT ======
if __name__ == "__main__":
    main()
