Write-Host "1. Running Pytest Suite..." -ForegroundColor Cyan
python -m pytest test_backend.py

Write-Host "2. Launching FastAPI Backend..." -ForegroundColor Cyan
$backendProcess = Start-Process -FilePath "uvicorn" -ArgumentList "main:app --port 8000" -PassThru -NoNewWindow

Start-Sleep -Seconds 3

Write-Host "3. Running Playwright E2E Tests..." -ForegroundColor Cyan
Set-Location frontend
npx playwright test

Write-Host "4. Cleaning up processes..." -ForegroundColor Cyan
Stop-Process -Id $backendProcess.Id
Set-Location ..

Write-Host "Pipeline execution complete!" -ForegroundColor Green