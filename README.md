# memorization
This tool helps you memorize any text using what's known as the "cognitive disfluency effect" -- by gradually "corrupting" your text while you're trying to learn it.  It works within your Notepad++ text editor.

Various researchers have discovered that learning is actually enhanced in some cases where the reader is forced to concentrate harder, such as when text is blurred or in an unfamiliar font.

Using a small Python script, this tool adds that sort of functionality to Notepad++.  By pressing a keyboard shortcut, you can "corrupt" a selected region of text (or if none, corrupt the current line).  "Corrupting" changes one random character to something else; hold the key down to corrupt a lot.

## How to Memorize:
If there's a passage of text you want to learn, try corrupting a small piece of it, so that you have to squint and think about it to read it.  Once you're used to it, corrupt it a little more, until you're finally seeing gibberish and mentally substituting real words where you remember they belong.  You've memorized one part!  Good.  Now move on to another.

Better yet, don't corrupt any one line too fast or you'll forget the substitutions.  Instead, spread out your corruption efforts in small bits, and move through the whole document in multiple passes.  Spread your passes out up to one per day if necessary.  Corrupt each line in different amounts, each one just enough to make you have to concentrate.

## InfoSec Applications

If you use this tool, you eventually end up with a gibberish passage of text that means something to you but not anyone else.  It's secure because you can keep corrupting text beyond the point of recoverability or recognizability -- as long as your brain can keep up with the substitutions.  Knowing how to de-code text that no one else can decode has obvious applications in information security, such as maintaining a list of passwords or pass-phrases.

When you do your corrupting, do it inside of a file that no one else can see, where you can backtrack in the undo-history if necessary in case you ever need a reminder (you forgot a subsitution).  Then, freely copy the finished text outside to another file, where it will appear as gibberish once seperated from the context of how it got to be that way.

#### Preserve Your Original Data!

Obviously you shouldn't corrupt your only source of any text!  If it's important enough to you to memorize, you don't want to risk data loss.  Instead, keep the original text secure in one (private) document, corrupt it in another (private) document, and then copy the final text to a third document whenever you want your secret reminders to appear publicly in a form that is meaningless to everyone but you.

# Usage

After following the below instructions to install, simply press *Alt+z* (or your chosen keyboard shortcut) to corrupt a selected region of text (or if none, corrupt the current line).  "Corrupting" changes one random character to something else; hold the key down to corrupt a lot.

# Installation

I assume you're already a Notepad++ user; I maintain all sorts of detailed notes (recipes, to-do lists) using Notepad++.

All you have to with your Notepad++ install is open the "Plugins" menu and select the popular plugin called "Python Script".  Install it, then drop the attached script from this repo into your "scripts" folder.  Lastly, associate a new key binding with that script.  I prefer binding *Alt+z* because it's available and the keys are near each other.

#### Binding your Key Shortcut

Follow the advice below, found [here](https://community.notepad-plus-plus.org/topic/14703/run-python-script-pythonscript-plugin-with-a-shortcut/3):

<blockquote>
  
<sub>Go to **Plugins** (menu) -> **Python Script** -> **Configuration**. The **Python Script Shortcut Configuration** window will appear.</sub>

<sub>In the **Scripts** area at the top of the **Python Script Shortcut Configuration** window, locate and select the script you want to bind to a shortcut (and/or toolbar button).</sub>

<sub>Between the **Scripts** box and the **Menu items** (or **Toolbar icons**) caption there is an **Add** button. To get your script added as a menu item (necessary to bind a keycombo to it via the “Shortcut Mapper”), press the **Add** button (the one above the **Menu items** caption). Very similar but hopefully obvious what to do for a toolbar button.</sub>

<sub>Once you click **OK** to dismiss the **Python Script Shortcut Configuration** window, you should be able to go into **Plugins** (menu) -> **Python Script** (just point to that and let the menu cascade open) and then see your script at this level of the menu (between the **Scripts->** and **Configuration** entries). Seeing your script appear here is key to being able to tie it to a shortcut keycombo.</sub>

<sub>Restart Notepad++. This allows the “Shortcut Mapper” to see that you’ve changed the **Plugins** (menu) -> **Python Script** menu contents.</sub>

<sub>Now go to **Settings** (menu) -> **Shortcut Mapper…** and select the **Plugin commands** tab. Scrolling down somewhat you should see your script in the **Name** column (along with “Pythonscript” in the **Plugin** column). Go ahead and select your script and assign a keycombo to it just like you would for any other command.</sub>
</blockquote>

### To Modify
  To edit this script's behavior or to make your own script to control all of Notepad++'s functionality, [read the documentation for the Python Script tool.](http://npppythonscript.sourceforge.net/)  The below source code should give you a head start in understanding how to control Notepad++.

## Full Source Code

```
import random

wasEmpty = editor.getSelectionEmpty()
cursorPos = editor.getCurrentPos()

if wasEmpty:
  editor.home()
  editor.lineEndExtend()
else:
  anchor = editor.getAnchor()
  
selection = editor.getSelText()
selection = list( selection )
selection[ random.randint( 0, len( selection )-1 ) ] = chr( random.randint( 0x20, 0x7E ) )
selection = "".join( selection )

editor.replaceSel( selection )

if wasEmpty:
  editor.setEmptySelection( cursorPos )
else:
  editor.setCurrentPos( cursorPos )
  editor.setAnchor( anchor )
```
Thanks to CrazySalamander from the SA forums for telling me about the cognitive disfluency effect!

###Further Reading
Make it Stick by Peter C. Brown:

<blockquote>
<sub>
  “Several studies have shown that although making text more difficult to read by leaving out letters or using an unusual typography may slow reading, readers remember more.
See M. A. McDaniel, G. O. Einstein, P. K. Dunay, & R. Cobb, Encoding difficulty and memory: Toward a unifying theory, Journal of Memory and Language 25 (1986), 645–656, 
and C. Diemand-Yauman, D. Oppenheimer, & E. B. Vaughn, Fortune favors the bold (and the italicized): Effects of disfluency on educational outcomes, Cognition 118 (2010), 111–115.
 The study in which the outline either matched or mismatched the chapter is S. M. Mannes & W. Kintsch, Knowledge organization and text organization, Cognition and Instruction 4 (1987), 91–115.”
  </sub>
  </blockquote>
