import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='&', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
async def dm(ctx, *, message: str):
    await ctx.send("📨 Envoi des messages en cours...")

    members = [m for m in ctx.guild.members if not m.bot]
    total = len(members)
    sent = 0
    failed = 0

    print(f"\n--- DÉBUT DE L'ENVOI ---\nTotal à DM : {total}\n")

    for idx, member in enumerate(members, start=1):
        try:
            await member.send(message)
            sent += 1
            print(f"[✅] Envoyé à {member} ({idx}/{total})")
            await asyncio.sleep(1)  # Pause standard pour éviter ratelimit
        except discord.errors.Forbidden:
            failed += 1
            print(f"[❌] Impossible d'envoyer à {member} (DM désactivés) ({failed} échecs)")
        except discord.errors.HTTPException as e:
            failed += 1
            print(f"[❌] Erreur HTTP pour {member} : {e} ({failed} échecs)")
            await asyncio.sleep(5)
        except Exception as e:
            failed += 1
            print(f"[❌] Erreur inconnue pour {member} : {e} ({failed} échecs)")

    print("\n--- FIN DE L'ENVOI ---")
    print(f"✅ Envoyés : {sent}")
    print(f"❌ Échecs : {failed}")

    await ctx.send(f"✅ Terminé : {sent} envoyés, ❌ {failed} échecs.")

@dm.error
async def dm_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("🚫 Tu n'as pas la permission d'utiliser cette commande.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("⚠️ Veuillez fournir un message à envoyer. Exemple: `&dm Salut !`")
    else:
        await ctx.send(f"⚠️ Erreur : {error}")

if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("⚠️ Erreur : le token Discord n'est pas défini dans le fichier .env")
    else:
        bot.run(token)
