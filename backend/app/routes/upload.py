#Dataset Upload API 
import os 

#uuid :- Universally  unique identifier, used to generate unique file names for uploaded files
import uuid 

import pandas as pd

from io import BytesIO

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException #type: ignore[reportMissingImports]

from sqlalchemy.orm import Session #type: ignore[reportMissingImports]

from app.database import SessionLocal

from app.models.dataset import Dataset

from app.dependencies.auth import get_current_user

from app.services.dataset_analyzer import(
    analyze_dataset
)

router = APIRouter(
    #'/datasets' add at the beginning of every endpoint in this router
    prefix="/datasets",
    tags=["Datasets"] # tags is  used to  organize your api in Swagger UI
)

def get_db(): #Gives endpoint access to database.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload")
#create new endpoint for uploading datasets 
async def upload_dataset( 
    file: UploadFile =File(...), #Expects a file uploaded by user. 
    #File(...) means that the file parameter is required and must be provided in the request.
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    allowed_extensions ={".csv", ".xlsx"}

    extension = os.path.splitext(
        file.filename
    )[1].lower() #Get the file extension and convert it to lowercase

    if extension not in allowed_extensions:

        raise HTTPException(
            status_code=400,
            detail="Only CSV and Excel files are allowed"
        )

    os.makedirs(
        "uploads",
        exist_ok=True
    ) #Create uploads directory if it doesn't exist

    unique_filename = (
        f"{uuid.uuid4()}{extension}"
    ) #Generate a unique filename using uuid4 and the original file extension

    file_path = os.path.join(
        #os.path.join is used to join the directory path and the 
        # unique filename to create the full file path where the uploaded file will be saved.
        "uploads",#name of the folder
        unique_filename 
    )

    contents = await file.read() #reads data from file and store it
    # await is used to Wait for this file-reading operation to finish before using its result,without blocking the server unnecessarily."

    #without with we need to do both open and close the file 
    with open(
        file_path, "wb" #wb:- write binary
    ) as buffer:  #buffer is variable to tore open file
        
        buffer.write(contents)
        #Write the uploaded file data into the file we just opened.

    try: 
        if extension ==".csv":
            df = pd.read_csv(
                    BytesIO(contents)
            )
        else:
            df = pd.read_excel(
                    BytesIO(contents)
                )

    except Exception:
        os.remove(file_path)
        #This deletes the uploaded file from your computer/server

        raise HTTPException(
            status_code=400,
            details = " Invalid dataset file"
        )
        # Replace NaN values with None
    df = df.where(
        pd.notnull(df),
        None
    )

    # Convert DataFrame into list of dictionaries
    data = df.to_dict(
        orient="records"
    )

    dataset =Dataset(
        filename=file.filename,#gets and save original name of uploaded file
        file_path=file_path, #This stores the location where the file was saved
        file_type=extension.replace(".",""),
        user_id=current_user["user_id"]#This connects the dataset to the logged-in user
    )

    db.add(dataset)
    db.commit()
    db.refresh(dataset)

    return{
        "message": "Dataset uploaded successfully",
        "dataset_id":dataset.id,
        "filename":dataset.filename,
        "file_type":dataset.file_type,
        "columns": list(df.columns)
    }


@router.get("/{dataset_id}/preview")
def preview_dataset(
    dataset_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
    # it allows you to  communicate with database
):
    dataset = db.query(Dataset).filter(
        #Go to dataset table with two condition
        Dataset.id == dataset_id,
        Dataset.user_id == current_user["user_id"]
    ).first()#give first matching record

    if not dataset:
        raise HTTPException(
            status_code=401,
            detail="Dataset not found"
        )

    #check thefiletype
    if dataset.file_type == "csv":

        #read and convert csv file into pandas Dataframe 
        df = pd.read_csv(
            dataset.file_path 
        )

    else:
        #read and convert csv file into pandas Dataframe 
        df = pd.read_excel(
            dataset.file_path
        )

    preview = df.head(10)
    #head() returns firsst rows of dataframe

    return {
        "column": list(df.columns),#list() is used to convert index object into python list
        
        #Preview.to.dict() converts dataframe into a dictionary
        "rows": preview.to_dict(

            #orient="records" tells Pandas how to convert a DataFrame into a dictionary.
            orient="records"
        )
    }

@router.get("/datasets/{dataset_id}/analysis")
def get_dataset_analysis(
    dataset_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    dataset = (
        db.query(Dataset).filter(
            Dataset.id == dataset_id,
            Dataset.user_id ==
            current_user["user_id"]
        ).first()
    )

    if not dataset:

        raise HTTPException(
            status_code=404,
            detail="Dataset not found"
        )

    if dataset.file_type == "csv":

        df = pd.read_csv(
            dataset.file_path
        )

    else:

        df = pd.read_excel(
            dataset.file_path
        )

    analysis = analyze_dataset(df)

    return analysis