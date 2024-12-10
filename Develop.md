# non-incremental-mode 開発

参考にするコンフィグ
これらは typescript から設定しているので、コンフィグとは考えられなくて、
キーバインディングから見えるローカル変数の扱いではないかと疑っている。

acceptingArgument
acceptingRectCommand
inMarkMode
inRectMarkMode
inRegisterInsertMode
inRegisterSaveMode
minibufferReading
prefixArgument
prefixArgumentExists

まだ使えるキーバインド

ctrl+cmd+a
ctrl+cmd+w
ctrl+cmd+e
ctrl+cmd+v

{
"key": "cmd+f",
"command": "actions.find",
"when": "editorFocus || editorIsOpen"
}
