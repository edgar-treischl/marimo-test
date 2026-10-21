
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "pandas",
#     "altair",
# ]
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    import altair as alt
    import marimo as mo
    import pandas as pd

    return alt, mo, pd


@app.cell
def _(mo, pd):
    data_path = mo.notebook_location() / "public" / "data" / "penguins.csv"
    df = pd.read_csv(data_path)
    df = df.dropna(
        subset=[
            "species",
            "island",
            "bill_length_mm",
            "flipper_length_mm",
            "body_mass_g",
            "sex",
        ]
    )
    return (df,)


@app.cell
def _(mo):
    mo.md("""
    # 🐧 Palmer Penguins Explorer

    Explore penguin measurements across **Adelie**, **Chinstrap**,
    and **Gentoo** species.

    Use the filter to compare species and discover how flipper length
    relates to body mass.
    """)
    return


@app.cell
def _(df, mo):
    species_options = ["All species"] + sorted(df["species"].unique().tolist())

    species = mo.ui.dropdown(
        options=species_options,
        value="All species",
        label="Filter by species",
    )

    species
    return (species,)


@app.cell
def _(df, species):
    filtered_df = (
        df
        if species.value == "All species"
        else df[df["species"] == species.value]
    )
    return (filtered_df,)


@app.cell
def _(filtered_df, mo):
    mo.hstack(
        [
            mo.stat(
                label="Penguins",
                value=f"{len(filtered_df):,}",
            ),
            mo.stat(
                label="Avg. body mass",
                value=f"{filtered_df['body_mass_g'].mean():,.0f} g",
            ),
            mo.stat(
                label="Avg. flipper length",
                value=f"{filtered_df['flipper_length_mm'].mean():.1f} mm",
            ),
        ],
        justify="space-around",
    )
    return


@app.cell
def _(alt, filtered_df):
    scatter = (
        alt.Chart(filtered_df)
        .mark_circle(size=85, opacity=0.8)
        .encode(
            x=alt.X(
                "flipper_length_mm:Q",
                title="Flipper length (mm)",
            ),
            y=alt.Y(
                "body_mass_g:Q",
                title="Body mass (g)",
            ),
            color=alt.Color(
                "species:N",
                title="Species",
                scale=alt.Scale(scheme="set2"),
            ),
            tooltip=[
                "species:N",
                "island:N",
                "sex:N",
                "flipper_length_mm:Q",
                "body_mass_g:Q",
            ],
        )
        .properties(
            title="Flipper length vs. body mass",
            height=350,
        )
        .interactive()
    )

    scatter
    return


@app.cell
def _(alt, filtered_df):
    summary = (
        filtered_df.groupby("species", as_index=False)
        .agg(
            average_mass=("body_mass_g", "mean"),
            penguin_count=("body_mass_g", "size"),
        )
    )

    bars = (
        alt.Chart(summary)
        .mark_bar(cornerRadiusEnd=5)
        .encode(
            x=alt.X(
                "species:N",
                title=None,
                sort="-y",
            ),
            y=alt.Y(
                "average_mass:Q",
                title="Average body mass (g)",
            ),
            color=alt.Color(
                "species:N",
                legend=None,
                scale=alt.Scale(scheme="set2"),
            ),
            tooltip=[
                alt.Tooltip("species:N", title="Species"),
                alt.Tooltip(
                    "average_mass:Q",
                    title="Average mass (g)",
                    format=".0f",
                ),
                alt.Tooltip(
                    "penguin_count:Q",
                    title="Penguins",
                ),
            ],
        )
        .properties(
            title="Average body mass by species",
            height=300,
        )
    )

    bars
    return


@app.cell
def _(mo):
    mo.md("""
    ---

    ### Explore the data

    The table below supports sorting, filtering, searching, and
    downloading the data for further analysis.
    """)
    return


@app.cell
def _(filtered_df):
    filtered_df
    return


if __name__ == "__main__":
    app.run()
