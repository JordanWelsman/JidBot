# Button Classes

# Module Imports
import discord
import schedule

# Expose Classes
__all__ = ["TestButtonView"]

# View Classes
class TestButtonView(discord.ui.View):
    """
    # TestButtonView
    A view with a button
    """
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Click Me!", style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You clicked the button!", ephemeral=True)

class RouteButtonView(discord.ui.View):
    """
    # RouteButtonView
    A view with a button menu
    """
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Button A", style=discord.ButtonStyle.primary)
    async def button_a(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="You pressed **Button A**. Choose an option:", view=SubViewA())

    @discord.ui.button(label="Button B", style=discord.ButtonStyle.primary)
    async def button_b(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="You pressed **Button B**. Choose an option:", view=SubViewB())

class SubViewA(discord.ui.View):
    """
    # SubViewA
    A sub-view for Button A
    """
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Option 1", style=discord.ButtonStyle.primary)
    async def option_1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="You chose **Option 1**.", view=None)

    @discord.ui.button(label="Option 2", style=discord.ButtonStyle.primary)
    async def option_2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="You chose **Option 2**.", view=None)

class SubViewB(discord.ui.View):
    """
    # SubViewB
    A sub-view for Button B
    """
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Option 3", style=discord.ButtonStyle.primary)
    async def option_3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="You chose **Option 3**.", view=None)

    @discord.ui.button(label="Option 4", style=discord.ButtonStyle.primary)
    async def option_4(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="You chose **Option 4**.", view=None)
        
