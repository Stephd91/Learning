# Concurrency

To learn more : 
- https://www.dabeaz.com/coroutines/Coroutines.pdf
- https://stackoverflow.com/questions/5201852/what-is-a-thread-really
- https://www.youtube.com/watch?v=GpqAQxH1Afc&ab_channel=ArjanCodes
- https://stackoverflow.com/questions/27435284/multiprocessing-vs-multithreading-vs-asyncio
- https://www.youtube.com/watch?v=K56nNuBEd0c&ab_channel=Socratica

**1) Concurrency vs Parallelism**

* **Concurrency** is 2 lines of customers ordering from a single cashier (lines take turns ordering).
* **Parallelism** is 2 lines of customers ordeting from 2 cachiers (each line gets its own cashier).
Parallelism.

**2) Multiprocessing vs Multithreading**

In **multiprocessing** you leverage multiple CPUs to distribute your calculations. Since each of the CPUs runs in parallel, you're effectively able to run multiple tasks simultaneously. You would want to use multiprocessing for CPU-bound tasks. An example would be trying to calculate a sum of all elements of a huge list. If your machine has 8 cores, you can "cut" the list into 8 smaller lists and calculate the sum of each of those lists separately on separate core and then just add up those numbers. You'll get a ~8x speedup by doing that.

In **(multi)threading** you don't need multiple CPUs. Imagine a program that sends lots of HTTP requests to the web. If you used a single-threaded program, it would stop the execution (block) at each request, wait for a response, and then continue once received a response. The problem here is that your CPU isn't really doing work while waiting for some external server to do the job; it could have actually done some useful work in the meantime! The fix is to use threads - you can create many of them, each responsible for requesting some content from the web. The nice thing about threads is that, even if they run on one CPU, the CPU from time to time "freezes" the execution of one thread and jumps to executing the other one (it's called context switching and it happens constantly at non-deterministic intervals). So if your task is I/O bound - use threading.

**asyncio** is essentially threading where not the CPU but you, as a programmer (or actually your application), decide where and when does the context switch happen. In Python you use an await keyword to suspend the execution of your coroutine (defined using async keyword).

Recap : 
- Is it IO-BOUND ? -----------> USE asyncio
- IS IT CPU-HEAVY ? ---------> USE multiprocessing
- ELSE ? ----------------------> USE threading

- CPU Bound => Multi Processing
- I/O Bound, Fast I/O, Limited Number of Connections => Multi Threading
- I/O Bound, Slow I/O, Many connections => Asyncio

coroutines = similar to generators but are data consumers (not data producers like generators)
