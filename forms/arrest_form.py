import datetime

import disnake
from disnake.ext import commands
from disnake import TextInputStyle, ModalInteraction


class ArrestModal(disnake.ui.Modal):
    def __init__(self):
        #Компоненты формы
        components = [
            disnake.ui.TextInput(
                label="Жетон",
                placeholder="Жетон сотрудника",
                custom_id="badge",
                style=TextInputStyle.short,
                max_length=6,
                required=True
            ),
            disnake.ui.TextInput(
                label="ФИО задержанного",
                placeholder="ФИО",
                custom_id="name",
                style=TextInputStyle.short,
            ),
            disnake.ui.TextInput(
                label="Номер паспорта задержаного",
                placeholder="Номер",
                custom_id="pass_number",
                style=TextInputStyle.short
            ),
            disnake.ui.TextInput(
                label="Статьи",
                placeholder="Вменяемые статьи",
                custom_id="charges",
                style=TextInputStyle.short,
            ),
            disnake.ui.TextInput(
                label="Время заключения",
                placeholder="ЧЧ:ММ:СС",
                custom_id="time",
                style=TextInputStyle.short,
            ),
        ]
        super().__init__(
            title="Arrest report",
            custom_id="arrest_report",
            components=components,
        )

#Параметры отправки формы
    async def callback(self, inter: disnake.ModalInteraction):
        badge = inter.text_values["badge"]
        suspect_name = inter.text_values["name"]
        charges = inter.text_values["charges"]
        pass_number = inter.text_values["pass_number"]
        time = inter.text_values["time"]

        embed = disnake.Embed(title="Arrest report", description="Отчет об аресте", url="https://discord.gg/Suec6a6m", color=disnake.Colour.blue(), timestamp=datetime.datetime.now())

        embed.set_footer(
            text="U.S Department of justice",
            icon_url="https://cdn.worldvectorlogo.com/logos/department-of-justice-2.svg",
        )

        embed.add_field(name="Сотрудник", value=inter.user.mention, inline=True)
        embed.add_field(name="Департамент", value=inter.user.top_role, inline=True)
        embed.add_field(name="Жетон", value=badge, inline=True)

        embed.add_field(name="ФИО задержанного", value=suspect_name, inline=True)
        embed.add_field(name="Номер паспорта", value=pass_number, inline=True)
        embed.add_field(name="Статьи", value=charges, inline=True)
        embed.add_field(name="Время заключения", value=time, inline=False)

        await inter.response.send_message(embed=embed)



