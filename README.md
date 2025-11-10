# Label Combiner - README

## What This Does
Automatically downloads shipping labels (or any PDFs) from a list of URLs and combines them into a single PDF file. Perfect for batch printing labels!

---

## Quick Start Instructions

### 1. Prepare Your Links
- Open your spreadsheet with the label URLs
- Select the entire column of URLs
- Copy them (Ctrl+C / Cmd+C)

### 2. Paste Into links.txt
- Open the `links.txt` file (it's in the same folder as the program)
- Paste all the URLs (Ctrl+V / Cmd+V)
- Save the file (Ctrl+S / Cmd+S)
- Each URL should be on its own line

### 3. Run the Program
**Windows:**
- Double-click `label_combiner.exe`

**Mac:**
- Double-click `label_combiner`
- If it says "unidentified developer", right-click → Open → Open anyway

### 4. Get Your PDF
- The program will show its progress in a black window
- When done, find `combined_orders.pdf` in the same folder
- Print it and you're done!

---

## Cool Features

✅ **Automatic Duplicate Removal** - If you accidentally copied the same URL twice, it'll skip duplicates

✅ **Smart File Naming** - If `combined_orders.pdf` already exists, it creates `combined_orders_1.pdf`, then `combined_orders_2.pdf`, etc. Your old files won't get overwritten!

✅ **Progress Tracking** - Shows you which PDF it's downloading (e.g., "Downloading PDF 5/23...")

✅ **Error Handling** - If one URL fails, it skips it and continues with the rest

✅ **Page Count** - Tells you exactly how many pages are in the final PDF

---

## What You'll See

When you run the program, you'll see something like this:

```
Total URLs in file: 47
After removing duplicates: 45 unique URLs

First 3 URLs:
  https://example.com/label1.pdf
  https://example.com/label2.pdf
  https://example.com/label3.pdf

Starting download and combination...

Downloading PDF 1/45: https://example.com/label1.pdf
  ✓ Added 1 pages
Downloading PDF 2/45: https://example.com/label2.pdf
  ✓ Added 1 pages
...

✓ Combined PDF saved as: combined_orders.pdf
Total pages: 45
```

---

## Troubleshooting

### "links.txt not found"
- Make sure `links.txt` is in the **same folder** as the program
- Check that it's named exactly `links.txt` (not `links.txt.txt`)

### "No such file or directory" error
- The program looks for `links.txt` in the same folder it's located in
- Don't move the program to a different folder without also moving `links.txt`

### Some URLs fail to download
- This is normal if a label URL has expired or the server is down
- The program will skip failed URLs and continue with the rest
- Check the output to see which ones failed

### Nothing happens when I double-click (Mac)
- Right-click the program → **Open** → click **Open** again
- This is a Mac security feature for apps not from the App Store
- You only need to do this once

### Nothing happens when I double-click (Windows)
- Windows Defender might block it
- Click "More info" → "Run anyway"
- You only need to do this once

---

## Tips & Tricks

💡 **Empty your links.txt between runs** - Copy over old URLs or clear the file for your next batch

💡 **Keep old PDFs** - The program never deletes old combined PDFs, so you can keep them as records

💡 **Test with a few URLs first** - If you have 100+ labels, try 5 URLs first to make sure everything works

💡 **Internet required** - The program downloads PDFs from the web, so you need an active internet connection

💡 **One URL per line** - Make sure each URL is on its own line in links.txt (spreadsheet paste does this automatically)

---

## File Structure

Your folder should look like this:
```
label_combiner/
├── label_combiner.exe (Windows) or label_combiner (Mac)
├── links.txt (your URLs go here)
├── combined_orders.pdf (created after first run)
├── combined_orders_1.pdf (created on second run)
└── README.txt (this file)
```

---

## Technical Details

**No installation required** - Everything needed is bundled in the executable

**Supported formats** - Any valid PDF URL that's publicly accessible

**Processing time** - About 0.5 seconds per PDF (so 50 PDFs = ~25 seconds)

**File size** - Final PDF size depends on the labels you're combining

**Platforms** - Windows .exe for Windows users, standalone executable for Mac users

---

## Questions?

The program is simple: it reads URLs from `links.txt`, downloads each PDF, and combines them into one file. That's it!

If something's not working, double-check:
1. ✅ links.txt is in the same folder as the program
2. ✅ links.txt has URLs (one per line)
3. ✅ You have an internet connection
4. ✅ The URLs are valid and accessible

Happy printing! 🖨️
