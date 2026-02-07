def parse_product(item, page_num):
    brand = item.query_selector("span.product-brand")
    name = item.query_selector("span.product-name")
    price = item.query_selector("div.price-section")
    rating = item.query_selector("div.average-rating")
    link = item.get_attribute("href")

    return {
        "Brand": brand.inner_text() if brand else None,
        "Name": name.inner_text() if name else None,
        "Price": price.inner_text() if price else None,
        "Rating": rating.inner_text() if rating else None,
        "Link": f"https://www.trendyol.com{link}" if link else None,
        "Page": page_num
    }