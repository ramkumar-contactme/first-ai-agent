import asyncio
from uagents import Agent, Context, Model

class Message(Model):
    text: str

communicator = Agent(name="communicator", port=8002)

async def send_message(ctx: Context):
    try:
        with open("agent1_address.txt", "r") as f:
            receiver_address = f.read().strip()
    except FileNotFoundError:
        print("[Communicator] ❌ Error: agent1_address.txt not found. Make sure Agent1 is running.")
        return

    message = Message(text="Hello Agent1, this is Communicator!")
    print(f"[Communicator] ✉️ Sending message to {receiver_address}: {message.text}")

    await ctx.send(receiver_address, message)
    ctx.logger.info(f"Sent message to {receiver_address}")

@communicator.on_event("startup")
async def startup(ctx: Context):
    await send_message(ctx)

if __name__ == "__main__":
    print(f"[Communicator] 🚀 Running on address: {communicator.address}")
    communicator.run()
