from fastapi import APIRouter, Depends, UploadFile, File, HTTPException #type: ignore[reportMissingImports] 
import pandas as pd

router = APIRouter(
    prefix="/data",
    tags=["Data Upload"]
)