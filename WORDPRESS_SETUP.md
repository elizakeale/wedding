# E & L Wedding Site — WordPress Setup

## Option A: Standalone HTML (Simplest)
Upload the entire folder to your hosting. Point your domain to `index.html`. Done.
No WordPress needed for this phase — it's fully self-contained.

## Option B: Drop into WordPress as a template

### 1. Copy assets
Place `css/style.css` and `js/app.js` into your theme folder (e.g. `/wp-content/themes/your-theme/`).

### 2. Enqueue in functions.php
```php
function wedding_enqueue_scripts() {
    wp_enqueue_style(
        'wedding-style',
        get_template_directory_uri() . '/css/style.css',
        [],
        '1.0.0'
    );
    wp_enqueue_script(
        'wedding-app',
        get_template_directory_uri() . '/js/app.js',
        [],
        '1.0.0',
        true // load in footer
    );
}
add_action( 'wp_enqueue_scripts', 'wedding_enqueue_scripts' );
```

### 3. Create a page template
Create `page-save-the-date.php` in your theme:
```php
<?php /* Template Name: Save the Date */ ?>
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
  <meta charset="<?php bloginfo('charset'); ?>" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Save the Date — E & L Wedding</title>
  <meta name="robots" content="noindex, nofollow" />
  <?php wp_head(); ?>
</head>
<body>
  <!-- Paste the contents of <body> from index.html here -->
  <?php wp_footer(); ?>
</body>
</html>
```

### 4. Change the password
In `js/app.js`, line 10:
```js
const CORRECT_PASSWORD = 'your-new-password-here';
```

## Images
The images currently load from Figma's CDN (valid ~7 days).
Before go-live, download them and replace the `src` paths with your own hosted versions.

- Background / hero: `https://www.figma.com/api/mcp/asset/a42a1747-...png`
- Password page background: `https://www.figma.com/api/mcp/asset/90fadef0-...png`  
- Couple photo: `https://www.figma.com/api/mcp/asset/99068a57-...png`
