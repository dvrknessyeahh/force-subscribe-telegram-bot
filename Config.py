import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = ""
    DATABASE_URL = ""
    APP_ID = ""
    API_HASH = ""
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Paksa Subscribe**\n__Paksa anggota grup untuk bergabung dengan channel tertentu sebelum mengirim pesan di grup.\nSaya akan membisukan suara anggota jika mereka tidak bergabung dengan channel Anda dan memberi tahu mereka untuk bergabung dengan saluran dan membunyikannya sendiri dengan menekan tombol.__",
        
        "**Setup**\n__Pertama-tama tambahkan saya di grup sebagai admin dengan izin larangan pengguna dan di channel sebagai admin.\nNote: Hanya pembuat grup yang dapat mengatur saya dan saya akan meninggalkan obrolan jika saya bukan admin dalam obrolan.__",
        
        "**Commmands**\n__/ForceSubscribe - Untuk mendapatkan pengaturan saat ini.\n/ForceSubscribe no/off/disable - Untuk mematikan ForceSubscribe.\n/ForceSubscribe {channel username} - Untuk mengaktifkan dan mengatur channel.\n/ForceSubscribe clear - Untuk membunyikan semua anggota yang dibisukan oleh saya.\n\nNote: /FSub adalah alias dari /ForceSubscribe__",
        
        "*👇join👇**"
      ]

      START_MSG = "**Hey [{}](tg://user?id={})**\n__Saya dapat memaksa anggota untuk bergabung dengan channel tertentu sebelum menulis pesan di grup.\nPelajari lebih lanjut di /help__"
