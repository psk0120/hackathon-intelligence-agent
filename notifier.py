def notify(result, decision):

    if decision != "APPLY":
        return

    print("\n🔥 NEW TECH HACKATHON FOUND 🔥")
    print(f"Title: {result['title']}")
    print(f"Mode: {result['mode']}")
    print(f"Deadline: {result['deadline']}")
    print(f"Prize Pool: {result['prize_pool']}")
    print(f"Link: {result['url']}")
    print("-" * 40)