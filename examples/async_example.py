import asyncio
import sys
from recnetlogin import RecNetLoginAsync  # Include the async client

# Insert your Rec Room account credentials
USERNAME: str = ""
PASSWORD: str = ""

async def main() -> None:
    rnl = RecNetLoginAsync(username=USERNAME, password=PASSWORD, prompt_2fa=True)
    
    token = await rnl.get_token(include_bearer=True)
    decoded_token = await rnl.get_decoded_token()
    
    print(f"{token=}\n{decoded_token=}")

if __name__ == "__main__":
    if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):  # fix "RuntimeError: Event Loop is closed" exception with asyncio on Windows
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())