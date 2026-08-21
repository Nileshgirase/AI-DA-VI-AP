import { useState } from "react";
import api from "../services/api";

function UploadDataset() {
    const [file, setFile] = useState(null);
    const [message, setMessage] = useState("");
    const [dataset, setDataset] = useState(null);
    const [preview, setPreview] = useState(null);
    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const getPreview = async (datasetId) => {
        try {
            const response = await api.get(
                `/datasets/${datasetId}/preview`
            );

            setPreview(response.data);

        } catch (error) {
            console.error(error);

            setMessage("Could not load dataset preview");
            }
    };
    const handleUpload = async () => {
        if (!file) {
            setMessage("Please select a file first");
            return;
        }

        const formData = new FormData();

        formData.append("file", file);

        try {
            const response = await api.post(
                "/datasets/upload",
                formData
            );
            setMessage(response.data.message);

            setDataset(response.data);

            await getPreview(
            response.data.dataset_id
            );
        }
        catch (error) {
            console.error(error);

            setMessage(
                error.response?.data?.detail || "Upload failed"
            ); 
        }
    };

    return (
        <div>
            <h1>Upload Dataset</h1>

            <input
                type="file"
                accept="'csv,.xlsx"
                onChange={handleFileChange}
            />
            <br/><br/>

            <button onClick={handleUpload}>
                Upload Dataset
            </button>

            <p>{message}</p>

            {dataset && (
                <div>
                    <h2>Dataset Information</h2>

                    <p>
                        <strong>Filename:</strong>{" "}
                        {dataset.filename}
                    </p>

                    <p><strong>Total Rows:</strong>{" "}
                        {dataset.rows}
                    </p>

                    <p>
                        <strong>Columns:</strong>
                    </p>

                    <ul>
                        {dataset.columns.map((column) => (
                            <li key={column}>
                                {column}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
            {preview && (
                <div>
                    <h2>Dataset Preview</h2>

                    <table border="1">
                        <thead>
                            <tr>
                                {preview.columns  && preview.columns.map((column) => (
                                    <th key={column}>
                                        {column}
                                    </th>
                                ))}
                            </tr>
                        </thead>
                        <tbody>
                            {preview.data && preview.data.map((row,index) => (
                                <tr key={index}>
                                    {preview.columns.map((column) => (
                                        <td key={column}>
                                            {row[column]}
                                        </td>
                                    ))}
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
}

export default UploadDataset