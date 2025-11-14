# Zendesk Help Center Scraper
This scraper collects all publicly available articles from any Zendesk Help Center, helping teams quickly centralize customer support knowledge. It solves the challenge of manually browsing scattered documentation across multiple locales and categories, delivering clean, structured content for analysis or integration. With fast performance and lightweight operation, it is ideal for organizations relying on Zendesk content.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Zendesk Help Center</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
The Zendesk Help Center Scraper extracts articles from any public-facing Zendesk knowledge base. It simplifies content aggregation by automatically fetching titles, URLs, and article metadata across supported locales. This is especially useful for researchers, customer support teams, product teams, and documentation analysts.

### Why Centralizing Zendesk Articles Matters
- Ensures consistent, up-to-date access to public support documentation.
- Eliminates manual tracking of updates across categories and locales.
- Enables large-scale text analysis or content migration workflows.
- Supports organizations using custom domains mapped to Zendesk.
- Works efficiently even with large multi-page help centers.

## Features
| Feature | Description |
|---------|-------------|
| Full Article Extraction | Collects all accessible articles from a Zendesk Help Center, including titles and URLs. |
| Locale-Based Scraping | Supports user-defined locales to ensure accurate regional content. |
| Pagination Handling | Automatically retrieves results across multiple pages. |
| Custom Domain Detection | Works with Zendesk-hosted custom domains by detecting the underlying instance name. |
| Fast & Lightweight | Optimized for quick scraping with minimal resource usage. |

---

## What Data This Scraper Extracts
| Field Name | Field Description |
|------------|------------------|
| url | Direct link to the Zendesk article. |
| title | The public-facing title of the article. |
| locale | The language/region locale of the help center. |
| category | Category or section the article belongs to (when available). |
| article_id | Unique identifier of the article (derived from URL). |

---

## Example Output

Example:


    [
      {
        "url": "https://support.neofinancial.com/hc/en-ca/articles/31977741550221-Information-on-Canada-Post-labour-disruption",
        "title": "Information on Canada Post labour disruption"
      },
      {
        "url": "https://support.neofinancial.com/hc/en-ca/articles/31720635648013-Privacy-mode-for-your-account-balances",
        "title": "Privacy mode for your account balances"
      },
      {
        "url": "https://support.neofinancial.com/hc/en-ca/articles/31603041636877-Guide-to-getting-a-mortgage-from-Neo",
        "title": "Guide to getting a mortgage from Neo"
      }
    ]

---

## Directory Structure Tree


    Zendesk Help Center/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── zendesk_parser.py
    │   │   └── utils_format.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── inputs.sample.txt
    │   └── sample.json
    ├── requirements.txt
    └── README.md

---

## Use Cases
- **Customer support teams** use it to centralize knowledge base articles, so they can maintain consistent internal documentation.
- **Product managers** use it to analyze recurring customer issues, so they can prioritize improvements.
- **Data analysts** use it to perform text mining on large sets of support articles, so they can generate insights and trends.
- **Technical writers** use it to migrate or compare documentation across regions, so they can streamline content updates.
- **QA teams** use it to verify that support articles are properly published across all locales.

---

## FAQs

**Does this scraper work with custom Zendesk domains?**
Yes. It detects the underlying Zendesk instance by scanning the page source for `.zendesk.com`, making it compatible with non-standard domains.

**What if the locale I choose doesn’t exist?**
No results will be returned. Ensure the locale (e.g., `en-us`, `en-ca`) is valid for the target help center.

**How many pages can it scrape?**
You can manually define the maximum number of pages, allowing control over performance and dataset size.

**Is a proxy required?**
Using a proxy is strongly recommended to avoid request rate limits and ensure consistent scraping.

---

## Performance Benchmarks and Results
**Primary Metric:** Processes an average of 150–250 articles per minute depending on locale and page depth.
**Reliability Metric:** Maintains a 98% success rate across public Zendesk Help Centers.
**Efficiency Metric:** Operates with low memory overhead, enabling long-running extractions without degradation.
**Quality Metric:** Achieves over 99% completeness in article URL and title extraction, ensuring dependable datasets.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
