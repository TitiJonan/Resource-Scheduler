import time
import random
from queue import PriorityQueue
import threading

# Define Customer Class
class Customer:
    def __init__(self, id, priority, service_time):
        self.id = id
        self.priority = priority
        self.service_time = service_time
        self.arrival_time = time.time()
        self.start_time = None
        self.end_time = None

    def __lt__(self, other):
        return self.service_time < other.service_time  # Used for Shortest Job Next Scheduling

# Define Agent Class
class Agent:
    def __init__(self, id):
        self.id = id
        self.available = True
        self.tasks_handled = 0
        self.total_work_time = 0

    def assign_task(self, customer):
        self.available = False
        self.tasks_handled += 1
        customer.start_time = time.time()
        print(f"Agent {self.id} is serving Customer {customer.id} (Priority: {customer.priority}, Service Time: {customer.service_time}s)")
        time.sleep(customer.service_time)  # Simulating service time
        customer.end_time = time.time()
        self.total_work_time += customer.service_time
        self.available = True
        print(f"Agent {self.id} is now available")

# Initialize Customers & Agents
customers = [Customer(i, random.choice([1, 2, 3]), random.randint(1, 5)) for i in range(10)]
agents = [Agent(i) for i in range(3)]

# Scheduling Algorithms
class Scheduler:
    def __init__(self, agents):
        self.agents = agents
        self.completed_customers = []
        self.monitoring_thread = None

    def round_robin(self, customers):
        print("\nStarting Round Robin Scheduling...")
        for i, customer in enumerate(customers):
            agent = self.agents[i % len(self.agents)]
            agent.assign_task(customer)
            self.completed_customers.append(customer)

    def priority_scheduling(self, customers):
        print("\nStarting Priority Scheduling...")
        queue = PriorityQueue()
        for customer in customers:
            queue.put((customer.priority, customer))  # Priority queue based on priority
        while not queue.empty():
            _, customer = queue.get()
            available_agent = next((a for a in self.agents if a.available), None)
            if available_agent:
                available_agent.assign_task(customer)
                self.completed_customers.append(customer)

    def shortest_job_next(self, customers):
        print("\nStarting Shortest Job Next Scheduling...")
        queue = sorted(customers, key=lambda c: c.service_time)  # Sort by shortest service time
        for customer in queue:
            available_agent = next((a for a in self.agents if a.available), None)
            if available_agent:
                available_agent.assign_task(customer)
                self.completed_customers.append(customer)

    def real_time_monitoring(self, interval=5):
        if self.monitoring_thread and self.monitoring_thread.is_alive():
            return  # Prevent multiple threads from being created
        
        def monitor():
            print("\nStarting Real-Time Monitoring...")
            while True:
                time.sleep(interval)
                print("\nAgent Status Update:")
                for agent in self.agents:
                    status = "Available" if agent.available else "Busy"
                    print(f"Agent {agent.id}: {status}, Tasks Handled: {agent.tasks_handled}")
        
        self.monitoring_thread = threading.Thread(target=monitor, daemon=True)
        self.monitoring_thread.start()

    def calculate_performance_metrics(self):
        if not self.completed_customers:
            print("No completed tasks to evaluate performance.")
            return

        total_wait_time = sum((c.start_time - c.arrival_time) for c in self.completed_customers)
        avg_wait_time = total_wait_time / len(self.completed_customers)

        total_agent_utilization = sum(agent.total_work_time for agent in self.agents)
        total_runtime = time.time() - min(c.arrival_time for c in self.completed_customers)
        avg_utilization_rate = (total_agent_utilization / (len(self.agents) * total_runtime)) * 100

        print("\nPerformance Metrics:")
        print(f"Average Customer Wait Time: {avg_wait_time:.2f} seconds")
        print(f"Agent Utilization Rate: {avg_utilization_rate:.2f}%")
        print("Fairness in Task Distribution:")
        for agent in self.agents:
            print(f"Agent {agent.id}: {agent.tasks_handled} tasks handled")

# Run Simulation
scheduler = Scheduler(agents)
scheduler.priority_scheduling(customers)

# Start real-time monitoring
scheduler.real_time_monitoring()

# Wait for all customers to be served before calculating performance
time.sleep(10)
scheduler.calculate_performance_metrics()