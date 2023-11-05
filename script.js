// テキストエリアでタブキーを押してインデントする
function handleTabKey(event, textarea) {
    if (event.key === "Tab") {
        event.preventDefault(); // デフォルトの動作を無効化
        const start = textarea.selectionStart;
        const end = textarea.selectionEnd;
        const text = textarea.value;
        const indent = "    "; // インデント用のスペース（4つのスペース）

        // カーソル位置にインデントを挿入
        textarea.value = text.substring(0, start) + indent + text.substring(end);

        // カーソル位置を調整
        textarea.selectionStart = start + indent.length;
        textarea.selectionEnd = textarea.selectionStart;
    }
}