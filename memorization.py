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
