# 検索ウィジェット関連キーバインディング

## 検索キーワード

find focussed focused visible

## 検索した結果の context keys

findInputFocussed
findWidgetVisible
notebookFindWidgetFocused
terminalFindVisible
terminalFindFocused
webviewFindWidgetVisible

## 関連

Awesome Emacs Keymap 関連
Keyboard Macro Beta 関連
システム関連

## システム関連詳細

1. findInputFocussed

{
"key": "enter",
"command": "editor.action.nextMatchFindAction",
"when": "editorFocus && findInputFocussed"
}
{
"key": "shift+enter",
"command": "editor.action.previousMatchFindAction",
"when": "editorFocus && findInputFocussed"
}

2. findWidgetVisible

{
"key": "shift+escape",
"command": "closeFindWidget",
"when": "editorFocus && findWidgetVisible && !isComposing"
}
{
"key": "escape",
"command": "closeFindWidget",
"when": "editorFocus && findWidgetVisible && !isComposing"
}
{
"key": "alt+cmd+enter",
"command": "editor.action.replaceAll",
"when": "editorFocus && findWidgetVisible"
}
{
"key": "cmd+enter",
"command": "editor.action.replaceAll",
"when": "editorFocus && findWidgetVisible && replaceInputFocussed"
}
{
"key": "shift+cmd+1",
"command": "editor.action.replaceOne",
"when": "editorFocus && findWidgetVisible"
}
{
"key": "enter",
"command": "editor.action.replaceOne",
"when": "editorFocus && findWidgetVisible && replaceInputFocussed"
}
{
"key": "alt+enter",
"command": "editor.action.selectAllMatches",
"when": "editorFocus && findWidgetVisible"
}
{
"key": "alt+cmd+enter",
"command": "search.action.replaceAll",
"when": "replaceActive && searchViewletVisible && !findWidgetVisible"
}

3. notebookFindWidgetFocused

{
"key": "escape",
"command": "notebook.hideFind",
"when": "notebookEditorFocused && notebookFindWidgetFocused"
}

4. terminalFindVisible

{
"key": "shift+escape",
"command": "workbench.action.terminal.hideFind",
"when": "terminalFindVisible && terminalFocus && terminalHasBeenCreated || terminalFindVisible && terminalFocus && terminalProcessSupported"
}
{
"key": "escape",
"command": "workbench.action.terminal.hideFind",
"when": "terminalFindVisible && terminalFocus && terminalHasBeenCreated || terminalFindVisible && terminalFocus && terminalProcessSupported"
}
{
"key": "escape",
"command": "workbench.action.terminal.clearSelection",
"when": "terminalFocusInAny && terminalHasBeenCreated && terminalTextSelected && !terminalFindVisible || terminalFocusInAny && terminalProcessSupported && terminalTextSelected && !terminalFindVisible"
}

5. terminalFindFocused

{
"key": "cmd+f",
"command": "workbench.action.terminal.focusFind",
"when": "terminalFindFocused && terminalHasBeenCreated || terminalFindFocused && terminalProcessSupported || terminalFocus && terminalHasBeenCreated || terminalFocus && terminalProcessSupported"
}
{
"key": "f3",
"command": "workbench.action.terminal.findNext",
"when": "terminalFindFocused && terminalHasBeenCreated || terminalFindFocused && terminalProcessSupported || terminalFocus && terminalHasBeenCreated || terminalFocus && terminalProcessSupported"
}
{
"key": "cmd+g",
"command": "workbench.action.terminal.findNext",
"when": "terminalFindFocused && terminalHasBeenCreated || terminalFindFocused && terminalProcessSupported || terminalFocus && terminalHasBeenCreated || terminalFocus && terminalProcessSupported"
}
{
"key": "alt+cmd+r",
"command": "workbench.action.terminal.toggleFindRegex",
"when": "terminalFindFocused && terminalHasBeenCreated || terminalFindFocused && terminalProcessSupported || terminalFocus && terminalHasBeenCreated || terminalFocus && terminalProcessSupported"
}
{
"key": "shift+f3",
"command": "workbench.action.terminal.findPrevious",
"when": "terminalFindFocused && terminalHasBeenCreated || terminalFindFocused && terminalProcessSupported || terminalFocus && terminalHasBeenCreated || terminalFocus && terminalProcessSupported"
}
{
"key": "shift+cmd+g",
"command": "workbench.action.terminal.findPrevious",
"when": "terminalFindFocused && terminalHasBeenCreated || terminalFindFocused && terminalProcessSupported || terminalFocus && terminalHasBeenCreated || terminalFocus && terminalProcessSupported"
}
{
"key": "alt+cmd+c",
"command": "workbench.action.terminal.toggleFindCaseSensitive",
"when": "terminalFindFocused && terminalHasBeenCreated || terminalFindFocused && terminalProcessSupported || terminalFocus && terminalHasBeenCreated || terminalFocus && terminalProcessSupported"
}
{
"key": "alt+cmd+w",
"command": "workbench.action.terminal.toggleFindWholeWord",
"when": "terminalFindFocused && terminalHasBeenCreated || terminalFindFocused && terminalProcessSupported || terminalFocus && terminalHasBeenCreated || terminalFocus && terminalProcessSupported"
}

6. webviewFindWidgetVisible
