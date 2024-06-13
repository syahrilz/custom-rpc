from pypresence import AioPresence
import asyncio
import time

client_id = '1250761579033530420'  # Ganti dengan client ID aplikasi Anda

async def main():
    RPC = AioPresence(client_id, transport="websocket")  # Inisialisasi AioPresence dengan transport websocket
    await RPC.connect()  # Menghubungkan ke Discord

    # Mengatur aktivitas
    start_time = int(time.time())
    await RPC.update(
        details="Life is so cute and adorable.",
        state="It's so funny, I can't stop laughing.",
        start=start_time,
        large_image="images",  # Ganti dengan image key yang valid
        large_text="Haha.",
        small_image="images",  # Ganti dengan image key yang valid
        small_text="Sucks.",
        buttons=[
            {"label": "PixiHive 🍔", "url": "https://dsc.gg"},
            {"label": "zeemarimo 🍔", "url": "https://www.youtube.com"}
        ]
    )
    print("RPC connected and activity set!")

    try:
        while True:
            await asyncio.sleep(15)  # Discord RPC memperbarui setiap 15 detik
    except KeyboardInterrupt:
        print("Disconnected from Discord")
        await RPC.close()  # Menutup koneksi secara bersih

if __name__ == "__main__":
    asyncio.run(main())