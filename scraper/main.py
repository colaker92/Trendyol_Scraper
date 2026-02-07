import tkinter as tk
from tkinter import messagebox
from playwright.sync_api import sync_playwright
import pandas as pd
import threading

def scrape_category(base_url, max_pages=5, sheet_name="Kategori"):
    products = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        for page_num in range(1, max_pages + 1):
            url = f"{base_url}&pi={page_num}"
            page.goto(url, wait_until="networkidle")
            page.wait_for_load_state("domcontentloaded")

            product_elements = page.query_selector_all("a.product-card")

            # UI log güncellemesi
            log_message(f"{page_num}. sayfa çekildi, {len(product_elements)} ürün bulundu.")

            for product in product_elements:
                brand_el = product.query_selector("span.product-brand")
                title_el = product.query_selector("span.product-name")

                price_el = (
                    product.query_selector("div.sale-price")
                    or product.query_selector("div[data-testid='price-section']")
                    or product.query_selector("div.price-section")
                )

                old_price_el = product.query_selector("div.strikethrough-price")

                discount_price_el = (
                    product.query_selector("span[data-testid='price-value']")
                    or product.query_selector("span.price-value")
                )

                link_el = product.get_attribute("href")

                brand = brand_el.inner_text().strip() if brand_el else ""
                title = title_el.inner_text().strip() if title_el else ""
                price = price_el.inner_text().strip() if price_el else ""
                old_price = old_price_el.inner_text().strip() if old_price_el else ""
                discount_price = discount_price_el.inner_text().strip() if discount_price_el else ""
                link = "https://www.trendyol.com" + link_el if link_el else ""

                products.append({
                    "brand": brand,
                    "title": title,
                    "price": price,
                    "old_price": old_price,
                    "discount_price": discount_price,
                    "link": link
                })

        browser.close()
    return products


def start_scrape():
    base_url = entry_url.get()
    try:
        max_pages = int(entry_pages.get())
    except ValueError:
        messagebox.showerror("Hata", "Sayfa sayısı bir sayı olmalı!")
        return
    sheet_name = entry_sheet.get() or "Kategori"

    log_message("Scraping başladı...")

    products = scrape_category(base_url, max_pages, sheet_name)

    output_file = "products.xlsx"
    try:
        with pd.ExcelWriter(output_file, mode="a", if_sheet_exists="replace") as writer:
            df = pd.DataFrame(products)
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        messagebox.showinfo("Başarılı", f"{len(products)} ürün kaydedildi → {output_file} ({sheet_name} sheet)")
    except Exception:
        with pd.ExcelWriter(output_file) as writer:
            df = pd.DataFrame(products)
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        messagebox.showinfo("Başarılı", f"{len(products)} ürün kaydedildi → {output_file} ({sheet_name} sheet)")

    log_message("Scraping tamamlandı.")


def start_scrape_thread():
    t = threading.Thread(target=start_scrape)
    t.start()


def log_message(msg):
    log_text.insert(tk.END, msg + "\n")
    log_text.see(tk.END)


# Tkinter arayüz
root = tk.Tk()
root.title("Trendyol Scraper")

tk.Label(root, text="Trendyol Linki:").grid(row=0, column=0, padx=5, pady=5)
entry_url = tk.Entry(root, width=50)
entry_url.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Kaç Sayfa:").grid(row=1, column=0, padx=5, pady=5)
entry_pages = tk.Entry(root, width=10)
entry_pages.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Excel Sheet Adı:").grid(row=2, column=0, padx=5, pady=5)
entry_sheet = tk.Entry(root, width=20)
entry_sheet.grid(row=2, column=1, padx=5, pady=5)

btn_start = tk.Button(root, text="Scrape Başlat", command=start_scrape_thread)
btn_start.grid(row=3, column=0, columnspan=2, pady=10)

# Log alanı
log_text = tk.Text(root, height=10, width=60)
log_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()