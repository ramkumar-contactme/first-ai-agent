from uagents import Agent, Context, Model
import asyncio

class Message(Model):
    message: str

agent_name = "MasterAgent"
communicator = Agent(
    name=agent_name,
    port=8003,
    seed=f"{agent_name} secret phrase",
    endpoint=["http://127.0.0.1:8003/submit"],
)

# List of slave agents
slaveAgents = ["SlaveAgent1", "SlaveAgent2"]

async def send_message(ctx: Context, agent_service):
    try:
        with open(f"{agent_service}_address.txt", "r") as f:
            receiver_address = f.read().strip()
    except FileNotFoundError:
        print(f"[{agent_name}] ❌ Error: {agent_service}_address.txt not found. Make sure {slaveAgents[0]} and {slaveAgents[1]} are running.")
        return

    message = Message(message=f"Hello {agent_service}, this is {agent_name}!")
    print(f"[{agent_name}] ✉️ Sending message to [{agent_service}]: {receiver_address}: {message.message}")

    await ctx.send(receiver_address, message)
    ctx.logger.info(f"[{agent_name}] ✉️ Sent message to [{agent_service}]: {receiver_address}")

@communicator.on_event("startup")
async def startup(ctx: Context):
    for agent in slaveAgents:
        await send_message(ctx, agent)

if __name__ == "__main__":
    print(f"[{agent_name}] 🚀 Running on address: {communicator.address}")
    communicator.run()
