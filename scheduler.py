import time
import schedule
from main import main


def run_agent():
    print("\n🤖 Running autonomous hackathon scan...\n")
    main()


# ✅ Run agent every day at 09:00
schedule.every().day.at("09:00").do(run_agent)

print("🧠 Autonomous Agent Started (Phase 3)")
print("⏳ Waiting for scheduled runs...\n")


# ✅ Keep program alive forever
while True:
    schedule.run_pending()
    time.sleep(30)