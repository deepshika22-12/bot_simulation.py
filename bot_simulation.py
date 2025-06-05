import random  # To simulate random distance values
import time    # To add delay between steps

# Simulates getting distance from a sensor (returns a value between 10 and 100 cm)
def get_distance():
    return random.randint(10, 100)

# Simulates bot moving forward
def move_forward():
    print("Bot is moving forward...")

# Simulates bot stopping when an obstacle is too close
def stop():
    print("Bot stopped due to obstacle.")

# Main function to simulate the bot’s behavior
def simulate_bot():
    for step in range(1, 11):  # Repeat for 10 steps
        distance = get_distance()  # Get simulated distance
        print(f"Step {step}: Distance to obstacle = {distance} cm")

        if distance < 20:  # If too close, stop the bot
            stop()
            break
        else:
            move_forward()
            time.sleep(1)  # Wait 1 second before next step

# Run the simulation
simulate_bot()
