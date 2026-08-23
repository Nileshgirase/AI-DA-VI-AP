import pandas as pd

def remove_duplicates(df: pd.DataFrame):
    cleaned_df = df.drop_duplicates()

    return cleaned_df

def fill_missing_numeric(
        df: pd.DataFrame,
        method: str = "median"
):
    cleaned_df = df.copy()

    numeric_columns=(
        cleaned_df.select_dtypes(include="number").columns
    )

    for column in numeric_columns:

        if method == "mean":
            value = cleaned_df[column].mean()
        else:
            value = cleaned_df[column].median()

        cleaned_df[column] = (cleaned_df[column].fillna(value))

        return cleaned_df

def fill_missing_categorical(
        df: pd.DataFrame
):
    cleaned_df= df.copy()

    categorical_columns = (
        cleaned_df.select_dtypes(include=["object","category"])
        .columns
    )

    for column in categorical_columns:

        if cleaned_df[column].isnull().any():

            mode = (
                cleaned_df[column]
                .mode()
            )

            if not mode.empty:

                cleaned_df[column] = (
                    cleaned_df[column]
                    .fillna(mode.iloc[0])
                )
    return cleaned_df

def get_cleaning_recommendations(
        df: pd.DataFrame
):
    recommendations = []

    duplicate_count = int(
        df.duplicated().sum()
    )

    if duplicate_count > 0:

        recommendations.append({
            "type":"duplicates",
            "count": duplicate_count,
            "recommendations":"Remove duplcate rows"
        })

    missing = (
        df.isnull().sum()
    )

    for column, count in missing.items():

        if count >0:
            recommendations.append({
                "type": "missing_values",
                "column": column,
                "count": int(count),
                "recommendation":
                    "Handle missing values"
            })
    return recommendations