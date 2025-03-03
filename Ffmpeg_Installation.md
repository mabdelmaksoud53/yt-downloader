# FFmpeg Installation Guide

## Step 1: Download FFmpeg

1. Go to the official FFmpeg site: [FFmpeg Download](https://ffmpeg.org/download.html)
2. Click **Windows builds** under "Get Packages & Binaries".
3. Choose a version (e.g., **gpl version**) and download the ZIP file.

## Step 2: Extract FFmpeg

1. Extract the downloaded `.zip` file to `C:\ffmpeg` (or any preferred location).
2. Inside `C:\ffmpeg`, locate the `bin` folder.
3. The path should be: `C:\ffmpeg\bin\ffmpeg.exe`.

## Step 3: Add FFmpeg to System Path

1. Press **Win + R**, type `sysdm.cpl`, and press **Enter**.
2. Go to **Advanced** → Click **Environment Variables**.
3. Under **System Variables**, find **Path**, then click **Edit**.
4. Click **New** and paste the path:

   ```bash
   C:\ffmpeg\bin
   ```

5. Click **OK** → **OK** → **OK** to close all windows.

## Step 4: Verify Installation

1. Open **Command Prompt**: Press **Win + R**, type `cmd`, and press **Enter**.
2. Type the following command and press **Enter**:

   ```bash
   ffmpeg -version
   ```

3. If installed correctly, you will see version details displayed in the terminal.

FFmpeg is now installed and ready to use!
