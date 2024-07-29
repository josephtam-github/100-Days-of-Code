# Day 11 to 15: Asynchronous Programming with Python (Asyncio)

## Intro
For Day 11 to 15 of my __#100DaysofCode__ I have been focusing on Asynchronous programming using Python's Asyncio

## What is Async I/O ?
Imagine programming as a journey from point __A__ to __D__. In traditional synchronous programming we travel in a straight line, stopping at each point before moving to the next, this means if there's a delay at any point everything pauses until we can move on. Now asynchronous programming changes the game, it allows us to start tasks at __B__ __C__ and __D__ even if the task at __A__ isn't finished yet. This is like sending out Scouts to explore multiple paths at once without waiting for the first Scout to return before sending out the next, this way our program can handle multiple tasks simultaneously, making it more efficient especially when dealing with operations that have waiting times like loading a web page and that's the essence of asynchronous programming - making our code more efficient by doing multiple things at once without the unnecessary waiting. Python has a built in module that enables us perform asynchronous programming called `asyncio`

### When should we use Asyncio
Asyncio is your choice for tasks that wait a lot like Network requests or file reading. It excels in handling many tasks concurrently without using much CPU power this makes your application more efficient and responsive when you're waiting on a lot of different tasks.

## Key Concepts in Asyncio
There are five key Concepts that I will be explaining on asyncio

### Event Loop
In Python's asyncio, the Event Loop is the core that manages and distributes tasks. Think of it as a central hub with tasks circling around it waiting for their turn to be executed. Each task takes its turn in the center where it's either executed immediately or paused if it's waiting for something like data from the internet. When a task awaits it steps aside (but still inside the central hub) making room for another task to run, ensuring the loop is always efficiently utilized once the awaited operation is complete the task will resume ensuring a smooth and responsive program flow, and that's how asyncio's event loop keeps your Python program running efficiently handling multiple tasks asynchronously.

```python
import asyncio

#coroutine function
async def main():
    print("Start of main coroutine")

#Run the main coroutine
asyncio.run(main())
```
Whenever we start writing asynchronous code in Python, we begin by importing the asyncio module

### Coroutines
Function defined with the `async` keyword like `async def function_name():` is known as a coroutine. Calling a coroutine and passing it to `asyncio.run()` will start your event loop and allow you to start running asynchronous code

```python
import asyncio

# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay) # Simulate an I/0 operation with a sleep
    print("Data fetched")
    return {"data": "Some data"} # Return some data


# Define another coroutine that calls the first coroutine
async def main():
    print("Start of main coroutine")
    task = fetch_data(2)
    # Await the fetch_data coroutine, pausing execution of main until fetch_data completes result await task
    print(f"Received result: {result}")
    print("End of main coroutine")

# Run the main coroutine
asyncio.run(main())
```

Simply calling this function you may assume that it's simply going to print out "start of main coroutine" but you'll see that that's actually not the case 

```python
>>> RuntimeWarning: coroutine 'main' was never awaited main()
```
It says coroutine main was never awaited now the reason we get that issue is because when we call the function here, what we're actually doing is we're generating a coroutine object this coroutine object needs to be awaited in order for us to actually get the result of its execution. That's why we use the `asyncio.run()` syntax because this will handle awaiting this coroutine and then allow us to write some more asynchronous code now the next thing that we need to look at is the await keyword.
Now the await keyword is what we can use to await a coroutine and to actually allow it to execute and for us to get the result the thing is though we can only use this await keyword inside of an asynchronous function or inside of a coroutine. So let's write another coroutine and see how we would await it 

```python
import asyncio

# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay) # Simulate an I/0 operation with a sleep
    print("Data fetched")
    return {"data": "Some data"} # Return some data


# Define another coroutine that calls the first coroutine
async def main():
    print("Start of main coroutine")
    task = fetch_data(2)
    # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
    result await task
    print(f"Received result: {result}")
    print("End of main coroutine")

# Run the main coroutine
asyncio.run(main())
```

slight variation to the last example we're we have two different coroutine objects and we're then awaiting them

```python
# Define a coroutine that simulates a time-consuming task
    async def fetch_data(delay, id):
    print("Fetching data... id:", id)
    await asyncio.sleep(delay) Simulate an 1/0 operation with a sleep
    print("Data fetched, id:", id)
    return {"data": "Some data", "id": id} # Return some data


# Define another coroutine that calls the first coroutine
    async def main():
    task1 fetch_data(2, 1)
    task2 fetch_data(2, 2)
    result await task1
    print(f"Received result: {result1}")
    result2
    task2 1
    print(f"Received result: {result2}")


# Run the main coroutine
asyncio.run(main())
```

Take a guess of what you think the output's going to be and how long you think it will take for this to execute.

```
>>> Fetching data... id: 1
>>> Data fetched, id: 1
>>> Received result: {'data': 'Some data', 'id': 1}
>>> Fetching data... id: 2
>>> Data fetched, id: 2
>>> Received result: {'data': 'Some data', 'id': 2}
```

See that we get `fetching data id: 1`, `data fetched id: 1` we then receive the result and then we go ahead and we fetch it for `id: 2` if set a perfcounter you can see that it takes 2 seconds we fetch the first result it takes another 2 seconds and we fetch the second result. Now this might seem counterintuitive because you may have guessed that when we created these two coroutine objects they were going to start running concurrently and that means that it would only take us a total of 2 seconds and we'd immediately get both of the results. But remember a coroutine doesn't start running until it's awaited so in this case we actually wait for the first coroutine to finish and only once this has finished do we even start executing the second coroutine. Meaning that we haven't really got any performance benefit here we've just 
created a way to kind of wait for a task to be finished that's all.

### Tasks
Now that we've understand the previous concept we can move over and talk about tasks and see how we can actually speed up an operation ation like the previous example and run both the tasks or coroutines at the same time. A task is a way to schedule a coroutine to run as soon as possible and to allow us to run multiple coroutines simultaneously. Now the issue we saw previously is that we needed to wait for one coroutine to finish before we could start executing the next, with a task we don't have that issue and as soon as a coroutine is sleeping or it's waiting on something that's not in control of our program we can move on and start executing another task. We're never going to be executing these tasks at the exact same time we're not using multiple CPU cores but if one task isn't doing something, if it's idle, if it's blocked, if it's waiting on something, we can switch over and start working on another task. The whole goal here is that our program is optimizing its efficiency so we're always attempting to do something and when we're waiting on something that's not in control of our program we switch over to another task and start working on that. o here's a quick example that shows you how we would optimize kind of the previous example that we looked at

```python
import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
    # Create tasks for running coroutines concurrently
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))
    task3 = asyncio.create_task(fetch_data(3, 1))
    result1 = await task1
    result2 = await task2
    result3 = await task3
    print(result1, result2, result3)


asyncio.run(main())
```
What we do here is we use the simple create task function. What we do is we say `task1` is equal to `asynio.create_task()` and then we pass in here a coroutine object. It's a coroutine object because this is a coroutine function we call the function and that returns to us a coroutine. We still need to `await` these tasks to finish so I just `await` them all in line and then collect all of their different results. If this was running synchronously, we'd have to wait for each of these tasks to run it would take us 2 seconds plus 3 seconds plus 1 second so a total of 6 seconds for this code to execute. However, you'll see now that this code will be executed in simply 3 seconds because as soon as one of the tasks is idle and we're waiting on this sleep we can go and execute or start another task. 

### Gather Function
The Gather function is a quick way to concurrently run multiple coroutines just like we did manually before so rather than creating a task for every single one of the coroutines using the `create_task()` function. We can simply use `gather()` and it will automatically run these concurrently for us and collect the results in a list. The way it works is that we pass multiple coroutines in here as arguments these are automatically going to be scheduled to run concurrently so we don't need to wait for them to finish before we start executing the next one, and then we will gather all of the results in a list in the order in which we provided the coroutines and it's going to wait for all of them to finish. We then use the `await` keyword which just simplifies this process for us, allowing us to have all of the results in one place so we can parse through them using this for Loop

```python
import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time) # Simulate a network request or 10 operation
    # Return some data as a result
    return {"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
    # Run coroutines concurrently and gather their return values
    results await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3))
    # Process the results
    for result in results:
    print(f"Received result: {result}")


# Run the main coroutine
asyncio.run(main())
```

Running this code and you see that it starts all three of our coroutines, it waits 3 seconds, and then we get all of our different results.

### Task Groups
One thing you should know about `gather` is that it's not that great at error handling and it's not going to automatically cancel other coroutines if one of them were to fail. Which means you could get some weird state in your application if you're not manually handling the different exceptions and errors that could occur. That is why we have `TaskGroup` which actually provides some built-in error handling which means it's typically preferred over `gather` because if any of the tasks inside of our task groups were to fail it will automatically cancel all of the other tasks which is typically preferable when we are dealing with some Advanced errors or some larger applications where we want to be a bit more robust.

```python
import asyncio

async def fetch_data(id, sleep_time): print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time) # Simulate a network request or I/O operation
    return {"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for 1, sleep_time in enumerate ([2, 1, 3], start=1): task tg.create_task(fetch_data(i, sleep_time)) tasks.append(task)
        # After the Task Group block, all tasks have completed
        results [task.result() for task in tasks]
        for result in results:
        print(f"Received result: {result}")

asyncio.run(main())
```
The `fetch_data()` function has not changed at all. All we've done here is we've started using `asyncio.TaskGroup()`. Notice I'm using `async with` this is known as an asynchronous context manager. You have seen context managers before but what this does is give us access to this `tg` variable so we create a task group as `tg` and now to create a task we can say `tg.create_task()`. The idea is, you simply create a task and as soon as it's created inside of the task group we now need to wait for that and all the other tasks to finish before we unblock from the block of code, then once they're all finished, we move on to the next lines of code. Similarly to any other task that we looked at before these are all going to run concurrently. 

### Synchronization Primatives
These are tools that allow us to synchronize the execution of various coroutines especially when we have larger more complicated programs. Let's look at three synchronization primatives:

#### Lock
The first synchronization tool is `lock`. Let's say that we have some shared resource maybe a database, table, or file. It might take a fair amount of time tomodify or do some operation on this shared resource and we want to make sure that no two coroutines are working on this at the same time. The reason for that is if two coroutines were modifying the same file for example- writing something to the database, we could get some kind of error where we get a mutated state or just weird results end up occurring because we have kind of different operations happening at different times and they're simultaneously occurring when we want really wait for one entire operation to finish before the next one completes. That might seem a little bit confusing but the idea is we have something and we want to lock it off and only be using it from one coroutine at a time. So what we can do is create a lock. When we create a lock we have the ability to acquire the lock and we do that with this code below:

```python
import asyncio

# A shared variable
shared_resource = 0

# An asyncio Lock
Lock asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock:
    # Critical section starts
    print(f"Resource before modification: {shared_resource}")
    shared_resource += 1 # Modify the shared resource
    await asyncio.sleep(1) # Simulate an I/O operation
    print(f"Resource after modification: {shared_resource}")
    # Critical section ends

async def main():
    await asyncio.gather(*(modify_shared_resource() for - in range(5)))


asyncio.run(main())
```

Understand how we use `async with lock` this again is an asynchronous context manager and what this will do is it will check if any other coroutine is currently using the lock. If it is, it's going to wait until that coroutine is finished. If it's not, it's going to go into this block of code. The idea is whatever we put inside of this context manager needs to finish executing before the lock will be released which means we can do some critical part of modification, we can have some kind of code occurring in here that we know will happen all at once before we move on to a different task or to a different coroutine. The reason that's important is because we have something like an `await` maybe we're waiting a network operation to save something else, that could trigger a different task to start running in this case we're saying "hey within this lock wait for all of this to finish before we release the lock" which means that even though another task could potentially be executing when the `asyncio.sleep()` occurs, it can't start executing. This is a critical part of code until all of this is finished and the lock is released. So all the lock is really doing is it's synchronizing our different coroutines so that they can't be using this block of code or executing this block of code while another coroutine is executing it that's all it's doing - locking off access to, in this case a critical resource that we only want to be accessed one at a time. You can see that we create five different instances of this coroutine, we then are accessing the lock and once we get down to `async def main():` we're going to release it 


#### Sephamore
A `semaphore` is something that works very similarly to a lock however, it allows multiple coroutines to have access to the same object at the same time but we can decide how many we want that to to have that access. So in this case we create a semaphore and we give give it a limit of two that means only two coroutines can access some resource at the exact same time and the reason we would do that is to make sure that we kind of throttle our program and we don't overload some kind of resource, so it's possible that we're going to send a bunch of different network requests we can do a few of them at the same time but we can't do maybe a thousand or ten thousand at the same time, so in that case we would create a semaphore. We'd say "okay our limit is maybe five at a time" and this way now we have the event loop automatically handled this throttle our code intentionally to only send maximum five requests at a time.

```python
import asyncio


async def access_resource(semaphore, resource_id):
    async with semaphore:
        # Simulate accessing a limited resource
        print(f"Accessing resource {resource_id}")
        await asyncio.sleep(1) # Simulate work with the resource
        print(f"Releasing resource {resource_id}")


async def main():
    semaphore = asyncio.Semaphore(2) # Allow 2 concurrent accesses
    await asyncio.gather( (access_resource(semaphore, i) for i in range(5)))


asyncio.run(main())

>>> Accessing resource 0
>>> Accessing resource 1
>>> Releasing resource 0
>>> Releasing resource 1
>>> Accessing resource 2
>>> Accessing resource 3
>>> Releasing resource 2
>>> Releasing resource 3
>>> Accessing resource 4
>>> Releasing resource 4
```

You can see that we can access the resource two at a time and modify it but we can't have any more than that

#### Event
The `event` (not the event loop previously discussed) is something that's a little bit more basic and allows us to do some simpler synchronization. In this case we can create an event and what we can do is we can await the event to be set and we can set the event. This acts as a simple Boolean flag and it allows us to block other areas of our code until we've set this flag to be true so it's really just like setting a variable to true or false in this case it's just doing it in the asynchronous way.

```python
import asyncio

async def waiter(event):
    print("waiting for the event to be set")
    await event.wait()
    print("event has been set, continuing execution")


async def setter(event):
    await asyncio.sleep(2) # Simulate doing some work
    event.set()
    print("event has been set!")


async def main():
    event asyncio.Event()
    await asyncio.gather(waiter(event), setter (event))
    
    
asyncio.run(main())
```

```
>>> waiting for the event to be set
>>> event has been set!
>>> event has been set, continuing execution
```

you can see we have some Setter function maybe it takes two seconds to be able to set some result we then set the result and as soon as that result has been set we can come up here we await that so we wait for this to finish


## Conclusion

Asynchronous programming with Python, particularly using the asyncio module, offers a powerful way to handle multiple tasks concurrently, making your applications more efficient and responsive. By understanding and utilizing key concepts such as the event loop, coroutines, tasks, gather function, task groups, and synchronization primitives like locks, semaphores, and events, you can optimize your code to perform better, especially in scenarios involving significant waiting times like network requests or file operations. Embracing these techniques not only enhances performance but also ensures that your programs can handle complex, real-world tasks with greater ease and reliability.

## Resources

- My knowledge on Async IO was gotten from my study of [Tech With Tim's YouTube tutorial](https://youtu.be/Qb9s3UiMSTA?si=i53xHGPiVMQsdNKs). Please like and subscribe to his channel

- Also read Python's Async IO docs [here](https://docs.python.org/3/library/asyncio.html)