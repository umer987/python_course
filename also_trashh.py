


    
    




    return n * factorial(n - 1)

def reverse_string(s):
    """Reverse a string using slicing"""
    return s[::-1]

def count_vowels(text):
    """Count vowels in a string"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

# ====== SECTION 3: DECORATORS ======
def timer(func):
    """Decorator to time function execution"""
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        print(f"{func.__name__} took {end - start} seconds")
        return result
    return wrapper

@timer
def slow_function():
    """Example function with timer decorator"""
    import time
    time.sleep(0.5)
    return "Done"

# ====== SECTION 4: DATA STRUCTURES ======
def demonstrate_collections():
    """Show various collection operations"""
    # List comprehensions
    squares = [x**2 for x in range(10)]
    evens = [x for x in range(20) if x % 2 == 0]
    
    # Dictionary comprehensions
    square_dict = {x: x**2 for x in range(5)}
    
    # Set operations
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    union = set1 | set2
    intersection = set1 & set2
    
    # Counter example
    text = "hello world hello python"
    word_count = Counter(text.split())
    
    # Default dict
    dd = defaultdict(list)
    dd['numbers'].append(1)
    dd['numbers'].append(2)
    
    return {
        'squares': squares,
        'evens': evens,
        'square_dict': square_dict,
        'union': union,
        'intersection': intersection,
        'word_count': word_count,
        'default_dict': dict(dd)
    }

# ====== SECTION 5: FILE OPERATIONS ======
def file_operations():
    """Demonstrate file operations"""
    filename = "sample.txt"
    
    # Write to file
    with open(filename, 'w') as f:
        f.write("Hello, Python!\n")
        f.write("This is line 2\n")
        f.write("This is line 3\n")
    
    # Read from file
    with open(filename, 'r') as f:
        content = f.read()
        lines = f.readlines()
    
    # Append to file
    with open(filename, 'a') as f:
        f.write("This is appended line\n")
    
    return content

# ====== SECTION 6: EXCEPTION HANDLING ======
def divide_safely(a, b):
    """Divide two numbers with error handling"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Invalid type!")
        return None
    finally:
        print("Division attempted")

# ====== SECTION 7: GENERATORS ======
def generate_numbers(limit):
    """Generator that yields numbers up to limit"""
    for i in range(limit):
        yield i * 2

def prime_generator(limit):
    """Generator for prime numbers"""
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

# ====== SECTION 8: MAIN EXECUTION ======
def main():
    """Main function to run the program"""
    print("=" * 50)
    print("100 LINES PYTHON PROGRAM")
    print("=" * 50)
    
    # Create objects
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Orange")
    
    print(f"\nDog: {dog.speak()}")
    print(f"Cat: {cat.speak()}")
    print(f"Dog fetch: {dog.fetch()}")
    print(f"Cat purr: {cat.purr()}")
    
    # Test functions
    print(f"\nFibonacci(10): {fibonacci(10)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Is 20 prime? {is_prime(20)}")
    print(f"Factorial(5): {factorial(5)}")
    print(f"Reverse 'Python': {reverse_string('Python')}")
    print(f"Vowels in 'Hello World': {count_vowels('Hello World')}")
    
    # Collections
    print("\nCollections Demo:")
    collections = demonstrate_collections()
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
