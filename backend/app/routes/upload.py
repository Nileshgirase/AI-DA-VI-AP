from fastapi import APIRouter, Depends, UploadFile, File, HTTPException #type: ignore[reportMissingImports] 
import pandas as pd
import os 

#uuid :- Universally  unique identifier, used to generate unique file names for uploaded files
import uuid 

router = APIRouter(
    prefix="/data",
    tags=["Data Upload"]
)