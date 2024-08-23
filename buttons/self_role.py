import disnake
from disnake.ext import commands

class SelfRole(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="FIB", style=disnake.ButtonStyle.grey, custom_id="FIB")
    async def FIB_Button(self, button: disnake.ui.Button, inter: disnake.Interaction):
        fib_role = inter.guild.get_role(1275857044225916978)
        if fib_role in inter.author.roles:
            await inter.author.remove_roles(fib_role)
        else:
            await inter.author.add_roles(fib_role)
        await inter.response.defer()

    @disnake.ui.button(label="LSPD", style=disnake.ButtonStyle.blurple, custom_id="LSPD")
    async def LSPD_Button(self, button: disnake.ui.Button, inter: disnake.Interaction):
        lspd_role = inter.author.guild.get_role(1275211613980328030)
        if lspd_role in inter.author.roles:
            await inter.author.remove_roles(lspd_role)
        else:
            await inter.author.add_roles(lspd_role)
        await inter.response.defer()
    

class ButtonCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistents_views_added = False

    @commands.command()
    async def buttons(self, inter):
        view = SelfRole()
        fib_role = inter.guild.get_role(1275857044225916978)
        lspd_role = inter.guild.get_role(1275211613980328030)
        embed = disnake.Embed(color=0x000066FF)
        embed.set_author(name="Buttons:")
        embed.description = "Test"
        embed.set_image(url="https://cdn.worldvectorlogo.com/logos/department-of-justice-2.svg")
        await inter.send(embed=embed, view=view)

    @commands.Cog.listener()
    async def on_connect(self):
        if self.persistents_views_added:
            return
        self.bot.add_view(SelfRole(), message_id = 1275858508599787520)

def setup(bot):
    bot.add_cog(ButtonCog(bot))
