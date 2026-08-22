import { useEffect, useState } from "react"; 
//useEffect is used to automatically run the code when the component loads

import { useParams } from"react-router-dom";
//useParams() gets information from URL

import api from "../services/api";

function DatasetAnalysis(){

    const {datasetId} = useParams();

    const [analysis, setAnalysis] = useState(null);

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState("");

    const fetchAnalysis = async () =>{

        try{
            const response = await api.get(
                `/datasets/${datasetId}/analysis`
            );

            setAnalysis(response.data);
        } catch (error) {

            console.error(error);

            setError(
                error.response?.data?.detail || 
                "Failed to load dataset analysis"
            );
        }
        finally{
            setLoading(false);
        }
    };
    useEffect(() => {
        fetchAnalysis();
    }, [datasetId]);

    if (loading) {
        return <h2>Analyzing Dataset.....</h2>
    }

    if (error) {
        return <h2>{error}</h2>
    }

    return(
        <div>
            <h1 className="text-3xl font-bild text-blue-600">
                Dataset Analysis
            </h1>
            
            <div>
                <h3>Total Rows</h3>

                <p>
                    {analysis.total_rows}
                </p>
            </div>
            <div>
                <h3>Total Columns</h3>

                <p>
                    {analysis.total_columns}
                </p>
            </div>
            <div>
                <h3>Duplicate Rows</h3>
                <p>
                    {analysis.duplicate_rows}
                </p>
            </div>
            <div className="column-categories">
                <h2>
                    Column Categories
                </h2>

                <table border="1">

                    <thead>

                        <tr>
                            <th>Column</th>
                            <th>Category</th>
                        </tr>

                    </thead>

                    <tbody>

                        {Object.entries(
                            analysis.column_categories
                        ).map(([column,]) => (
                            <tr key={column}>

                                <td>
                                    {column}
                                </td>

                                <td>
                                    {category}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            <div className="missing-values">
                <h2>
                    Missing Values
                </h2>

                <table border="1">

                    <thead>

                        <tr>
                            <th>Column</th>
                            <th>Missing Values</th>
                        </tr>

                    </thead>
                    <tbody>
                        {Object.entries(
                            analysis.missing_values
                        ).map(([column, count]) => (

                            <tr key={column}>

                                <td>
                                    {column}
                                </td>

                                <td>
                                    {count}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
            <div className="numeric-statetics">
                <h2>
                    Numeric Statistics
                </h2>
                {Object.entries(
                    analysis.numeric_statistics 
                ).map(([column, stats]) => (
                    <div key={column}>
                        
                        <h3>{column}</h3>

                            <p>
                                Mean: {stats.mean}
                            </p>

                            <p>
                                Median:{stats.median}
                            </p>

                            <p>
                                Minimum:{stats.min}
                            </p>

                            <p>
                                Maximum:{stats.max}
                            </p>
                        
                    </div>
                ))}
            </div>
        </div>
    );
}

export default DatasetAnalysis;