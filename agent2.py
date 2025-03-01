import asyncio
from uagents import Agent, Context, Model

class Message(Model):
    text: str

agent2 = Agent(name="agent2", port=8003)

@agent2.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    print(f"[Agent2] 📩 Received message from {sender}: {msg.text}")
    ctx.logger.info(f"Received message from {sender}: {msg.text}")

if __name__ == "__main__":
    print(f"[Agent2] 🚀 Running on address: {agent2.address}")
    agent2.run()
