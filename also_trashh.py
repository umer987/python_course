const express = require('express') //importing server

const app = express() //making server calass instance
app.get("/",(req,res)=>{    
    res.send("HELLO WORLD")
})
app.get('/about',(req,res)=>{
    res.send("HELLO FROM ABOUT")
})
app.listen(6000)
    print(f"Squares: {collections['squares']}")
    print(f"Word Count: {collections['word_count']}")
    
    # Generator
    print("\nGenerator Demo (first 5 even numbers):")
    gen = generate_numbers(5)
    for num in gen:
        print(f"  {num}")
    
    # Prime generator
    print("\nPrime numbers up to 20:")
    primes = list(prime_generator(20))
    print(f"  {primes}")
    
    # Decorator
    print("\nDecorator Demo:")
    slow_function()
    
    # Exception handling
    print("\nException Handling:")
    print(f"10 / 3 = {divide_safely(10, 3)}")
    print(f"10 / 0 = {divide_safely(10, 0)}")
    
    # File operations
    print("\nFile Operations:")
    file_operations()
    with open("sample.txt", 'r') as f:
        print("File content:")
        print(f.read())
    
    # List operations
    print("\nList Operations:")
    my_list = [1, 2, 3, 4, 5]
    print(f"Original list: {my_list}")
    my_list.append(6)
    print(f"After append: {my_list}")
    my_list.remove(3)
    print(f"After remove: {my_list}")
    
    # Map, filter, reduce
    numbers = [1, 2, 3, 4, 5, 6]
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
