// net.minecraft.command

package net.minecraft.command;

import net.minecraft.server.MinecraftServer;
import net.minecraft.util.math.BlockPos;
import net.minecraft.util.text.TextComponentTranslation;
import net.minecraft.util.text.TextFormatting;

import javax.annotation.Nullable;
import java.util.Collections;
import java.util.List;

public class CommandServerPlugins extends CommandBase {
    public String getCommandName() { return "plugins"; }

    public int getRequiredPermissionLevel() { return 2; }

    public String getCommandUsage(ICommandSender sender)
    {
        return "/plugins";
    }

    public void execute(MinecraftServer server, ICommandSender sender, String[] args) throws CommandException
    {
        sender.addChatMessage(new TextComponentTranslation("Plugins " + getPluginList()));
    }

    public String getPluginList() {
        StringBuilder builder = new StringBuilder();

        if(builder.length() > 0) {
            builder.append(TextFormatting.WHITE);
            builder.append(", ");
        }

        builder.append(TextFormatting.GREEN);
        builder.append("Papyrus");
        return "(" + 1 + "): " + builder.toString();
    }

    public List<String> getTabCompletionOptions(MinecraftServer server, ICommandSender sender, String[] args, @Nullable BlockPos pos)
    {
        return Collections.emptyList();
    }
}
