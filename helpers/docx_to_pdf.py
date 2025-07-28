import subprocess

def docx_to_pdf(input_file: str, output_file: str):
  result = subprocess.run([
      'soffice', 
      '--headless',
      '--invisible',     
      '--nologo',        
      '--nodefault', 
      '--convert-to', 
      'pdf', 
      input_file, 
      '--outdir', 
      output_file], 
      check=True, 
      capture_output=True,
      text=True,
    )
  
  return result