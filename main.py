import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all(), status=discord.Status.online)


#Mute members


muted_role = "Muted"
muted_category = "Main" 

@bot.command()
async def mute(ctx, member:discord.member):
    if any(role.name in admin_roles for role in ctx.author.roles):
        role = discord.utils.get(ctx.guild.roles, name=muted_role)
        if not role:
            await ctx.send(f"Role {role} not found")
            return
        
        await member.add_roles(role)
        await ctx.send(f"{member} was muted")
    else:
        await ctx.send("You dont have permissions to mute members")

#Unmute members
        
@bot.command()
async def unmute(ctx, member:discord.member):
    if any(role.name in admin_roles for role in ctx.author.roles):
        role = discord.utils.get(ctx.guild.roles, name=muted_role)
        if not role:
            await ctx.send(f"Role {role} not found")
            return
        
        await member.add_roles(role)
        await ctx.send(f"{member.mention} was unmuted")
    else:
        await ctx.send("You dont have permissions to unmute members")

#Unban members
        
@bot.command()
async def unban(ctx, *, member):
    if any(role.name in admin_roles for role in ctx.author.roles):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'The member {user.mention} has been unbanned.')
                return
        await ctx.send(f'Could not find member {member}.')
    else:
        await ctx.send("You don't have permission to unban members.")


bot.run("YOUR TOKEN  HERE")
