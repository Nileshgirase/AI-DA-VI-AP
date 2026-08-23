import pandas as pd

def detect_column_type(series:  pd.Series):

    if pd.api.types.is_numeric_dtype(series):
        return "numeric"

    if pd.api.types.is_datetime64_any_dtype(series):
        return "datetime"

    if series.dtype == "object":

        try:
            pd.to_datetime(
                series,
                errors="raise"
            )

            return "datetime"
        
        except Exception:

            return "categorical"

    return "categorical"

def analyze_dataset(df: pd.DataFrame):

    #Detect missing values
    missing_values = (
        df.isnull()
        .sum()
        .to_dict()
    )

    duplicate_rows= int(
        df.duplicated().sum()
    )

    column_types = {
        column: str(dtype)
        for column, dtype in df.dtypes.items()
    }

    column_categories ={}

    for column in df.columns:

        column_categories[column] = (
            detect_column_type(
                df[column]
            )
        )

    numeric_statistics = {}

    numeric_columns = []

    for column in df.select_dtypes(include="number").columns:

        column_name=column.lower()

        if(
            column_name == "id"
            or column_name.endswith("_id")
            or column_name.endswith("id")
        ):
            continue
        numeric_columns.append(column)

    for column in numeric_columns:

        numeric_statistics[column] = {
            "mean":float(df[column].mean()),
            "median": float(df[column].median()),
            "min": float(df[column].min()),
            "max": float(df[column].max()),
            "std": float(df[column].max())
        }
    analysis ={
        "total_rows":len(df),
        "total_columns": len(df.columns),
        "columns": list(df.columns),
        "missing_values": missing_values,
        "duplicate_rows": duplicate_rows,
        "column_types": column_types,
        "column_categories": column_categories,
        "numeric_statistics": numeric_statistics
    }

    return analysis