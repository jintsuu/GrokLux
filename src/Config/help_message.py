HELPMESSAGE: str = """
All commands are case-sensitive.

+help (menu) -  Displays this help menu in DMs. Structured: +command (aliases) | (arguments)  -  Explanation
+wrhelp (winratehelp) | ()  -  Displays the winrate help menu in DMs.

+gwenadd (add, gwenadd) | () -  Makes the bot automatically reply to any message containing the word 'Gwen' in any way. Replies on a server-wide basis.
+gwenremove (remove, rem, removesub) | ()  -  Removes you from the autoreplies.
+list () | ()  -  Gives a list of all accepted champions in DMs. Keep in mind that some champions have weird names officially...
+elolist () | ()  -  Gives a list of all accepted elos in DMs.
+rolelist (roles) | ()
+patch (version, checkver) | ()  -  Gives the current league patch that GwenBot uses. Any champ added after this patch will not work with GwenBot.

Fun commands:
+evasion (jax)
+gwen (g, immune)
+listenhere (lh)
+aatrox
+emo
+sylas (george)

GwenBot is open source, you can find all code on <https://github.com/Zexsch/GwenBotV3>
"""


WRHELPMESSAGE: str = """
+wr (winrate) | (champion)  -  Gives the winrate of the given champion.
Optional parameters:
elo, role, opposing champ
Example command usage: +wr vayne top d2+ aatrox - Gives the winrate of Vayne in top lane in D2+ elo against Aatrox.
Message @Zexsch#1884 if u.gg is not down and the commands do not work.
"""