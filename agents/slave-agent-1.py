from uagents import Agent, Context, Model

class Message(Model):
    message: str

agent_name = "SlaveAgent1"
slave_agent1 = Agent(
    name=agent_name,
    port=8001,
    seed=f"{agent_name} secret phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)

@slave_agent1.on_message(model=Message)
async def handle_message(ctx: Context, sender: str, message: Message):  # Added `sender`
    print(f"[{agent_name}] 📩 Received message from {sender}: {message.message}")
    ctx.logger.info(f"[{agent_name}] Received message from {sender}: {message.message}")

# Save the agent's address to a file for communication
with open(f"{agent_name}_address.txt", "w") as f:
    f.write(slave_agent1.address)

if __name__ == "__main__":
    print(f"[{agent_name}] 🚀 Running on address: {slave_agent1.address}")
    slave_agent1.run()
