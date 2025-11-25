# GitHub Actions Secrets Configuration

This document lists all the secret variables you need to configure in your GitHub repository for the daily paper digest workflow to send emails.

## Required Secrets

Configure these in: **GitHub Repository → Settings → Secrets and variables → Actions → New repository secret**

### 1. `SMTP_HOST`
- **Description:** Your SMTP server hostname
- **Example:** `smtp.gmail.com` or `smtp.mail.yahoo.com` or `mail.intrawebb.com`
- **Required:** Yes

### 2. `SMTP_PORT`
- **Description:** SMTP server port number (usually 587 for TLS or 465 for SSL)
- **Example:** `587` or `465`
- **Required:** Yes
- **Default:** If not set, defaults to 587

### 3. `EMAIL_USER`
- **Description:** SMTP authentication username (usually your email address)
- **Example:** `dailypapersender@intrawebb.com` or `your-email@gmail.com`
- **Required:** Yes

### 4. `EMAIL_PASS`
- **Description:** SMTP authentication password or app-specific password
- **Example:** Your email password or app-specific password
- **Required:** Yes
- **Note:** For Gmail, you may need an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password

### 5. `EMAIL_RECIPIENTS`
- **Description:** Comma-separated list of email addresses to send the digest to
- **Example:** `daniel@intrawebb.com,recipient2@example.com`
- **Required:** No (will fall back to reading from `config/emails.txt` file)
- **Note:** If not set, the code will read recipients from the `config/emails.txt` file in the repository

## Optional Secrets

### `DIGEST_MODE` (Optional)
- **Description:** Set to "daily" or "weekly" to control digest frequency
- **Example:** `daily` or `weekly`
- **Required:** No
- **Default:** `daily`

### `SCHOLAR_PROXY_URL` (Optional)
- **Description:** Proxy URL for Google Scholar API requests
- **Required:** No
- **Only needed if:** You're using Google Scholar integration and need a proxy

## How to Set Up Secrets

1. Go to your GitHub repository: `https://github.com/ddrizzil/HyperImage`
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add each secret listed above:
   - **Name:** (e.g., `SMTP_HOST`)
   - **Secret:** (paste your value)
   - Click **Add secret**
5. Repeat for all required secrets

## Example SMTP Settings

### Gmail
```
SMTP_HOST: smtp.gmail.com
SMTP_PORT: 587
EMAIL_USER: your-email@gmail.com
EMAIL_PASS: [App Password - see note above]
EMAIL_RECIPIENTS: recipient@example.com
```

### Outlook/Office 365
```
SMTP_HOST: smtp-mail.outlook.com
SMTP_PORT: 587
EMAIL_USER: your-email@outlook.com
EMAIL_PASS: your-password
EMAIL_RECIPIENTS: recipient@example.com
```

### Yahoo
```
SMTP_HOST: smtp.mail.yahoo.com
SMTP_PORT: 587
EMAIL_USER: your-email@yahoo.com
EMAIL_PASS: your-password
EMAIL_RECIPIENTS: recipient@example.com
```

### Custom SMTP Server
```
SMTP_HOST: mail.yourdomain.com
SMTP_PORT: 587
EMAIL_USER: sender@yourdomain.com
EMAIL_PASS: your-password
EMAIL_RECIPIENTS: recipient@example.com
```

## Verification

After setting up secrets, you can:
1. Manually trigger the workflow from the **Actions** tab → **Daily Paper Digest** → **Run workflow**
2. Check the workflow logs to see if emails are being sent
3. Look for log messages like: `"Email sent to recipient@example.com"`

## Troubleshooting

- **"SMTP_HOST is not set"**: Make sure `SMTP_HOST` secret is configured
- **"SMTP credentials missing"**: Check that `EMAIL_USER` and `EMAIL_PASS` are set correctly
- **Authentication failed**: Verify your password/app password is correct
- **Connection timeout**: Check that `SMTP_HOST` and `SMTP_PORT` are correct for your email provider

