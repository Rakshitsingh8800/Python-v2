def shutdown():
    print("\nInitiating shutdown sequence...")
    print("Saving all open files...")
    print("Closing running applications...")
    print("Logging out user...")
    print("System shutdown completed successfully.")

    exit()

print("System started successfully.")
print("System is currently running.")

choice = input("Do you want to shutdown the system? (yes/no): ")

if choice.lower() == "yes":
    shutdown()
else:
    print("Shutdown cancelled.System continues to run.")