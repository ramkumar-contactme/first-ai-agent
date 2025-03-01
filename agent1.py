import asyncio
from uagents import Agent, Context, Model

class Message(Model):
    text: str

agent1 = Agent(name="agent1", port=8001)

# Save Agent1's address dynamically
with open("agent1_address.txt", "w") as f:
    f.write(agent1.address)

@agent1.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    print(f"[Agent1] 📩 Received message from {sender}: {msg.text}")
    ctx.logger.info(f"Received message from {sender}: {msg.text}")

if __name__ == "__main__":
    print(f"[Agent1] 🚀 Running on address: {agent1.address}")
    agent1.run()
