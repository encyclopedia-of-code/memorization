# memorization
A tool to help you memorize text in Notepad++.  Uses the cognitive disfluency effect, by gradually corrupting text as you learn it.

Various researchers have discovered that learning is actually enhanced in some cases where the reader is forced to concentrate harder, such as if the text is blurry to read, or in an unfamiliar font.

Using a small Python script, this tool adds functionality to Notepad++.  By pressing a keyboard shortcut, you can "corrupt" a selected region of text (or if none, the current line).  "Corrupting" changes one random character to something else; hold the key down to corrupt a lot.

If there's a passage of text you want to learn, try corrupting a small piece of it, so that you have to squint and think about it to read it.  Once you're used to it, corrupt it a little more, until you're finally seeing gibberish and mentally substituting real words where you remember they belong.  You've memorized one part!  Good.  Now move on to another.  Don't go too fast or you'll forget the substitutions.  Work on each line a little at a time.

## InfoSec Applications

If you use this tool, you eventually end up with a gibberish passage of text that means something to you but not anyone else.  You can keep corrupting text beyond recognition as long as your memory can keep up with the substitutions.  Knowing how to de-code text that no one else can decode has obvious applications in information security, such as maintaining a list of passwords or pass-phrases.

Do your corrupting inside of a file that no one else can see, where you can go backwards in the undo-history if necessary in case you need a reminder (you forgot a subsitution).  Then, freely copy the finished text outside to another file, where it will appear to gibberish without the context of the undo-history.

### Preserve Your Original Data!

Obviously you shouldn't corrupt your only source of any text!  If it's important enough to you to memorize, you don't want to risk data loss.  Instead, keep the original text secure in one (private) document, corrupt it in another (private) document, and then copy the final text to a third document whenever you want your secret reminders to appear publicly in a form that is meaningless to everyone but you.

# Usage

After following the below instructions to install, simply press *Alt+z* (or your chosen keyboard shortcut) to corrupt a selected region of text (or if none, the current line).  "Corrupting" changes one random character to something else; hold the key down to corrupt a lot.

# Installation

I assume you're already a Notepad++ user; I maintain all sorts of detailed notes (recipes, to-do lists) using Notepad++.

All you have to with your Notepad++ install is open the "Plugins" menu and select the popular plugin called "Python Script".  Install it, then drop the attached script from this repo into your "scripts" folder.  Lastly, associate a new key binding with that script.  
