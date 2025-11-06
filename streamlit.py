import streamlit as st
import pandas as pd
from pathlib import Path

st.title("CSV Extension Changer")

uploaded = st.file_uploader("Upload your CSV", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)

    # 1) Let user pick the filename column (default to first column)
    default_col = df.columns[0] if len(df.columns) else None
    col_name = st.selectbox("Which column has the filenames?", df.columns, index=df.columns.get_loc(default_col))

    # 2) Pick target extension
    target_ext = st.selectbox("Change extension to:", [".ai", ".eps", ".svg", ".png", ".jpg", ".jpeg"])

    # 3) Preview before/after (top 5)
    if col_name:
        before = df[col_name].head().tolist()

        # safer suffix change using pathlib
        def set_ext(name: str) -> str:
            try:
                p = Path(str(name))
                # if name has no suffix, still add one
                return p.with_suffix(target_ext).name
            except Exception:
                return str(name)  # leave as-is on any weird value

        df[col_name] = df[col_name].astype(str).apply(set_ext)
        after = df[col_name].head().tolist()

        st.write("### Preview (first 5 rows)")
        st.table({"Before": before, "After": after})

        # 4) Download updated CSV
        csv_bytes = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download updated CSV", csv_bytes, "updated.csv", "text/csv")
