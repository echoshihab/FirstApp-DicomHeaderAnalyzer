from django.shortcuts import render
from .forms import UploadFileForm
import pydicom

#ds = pydicom.dcmread("dicomprocess/IM000001")
#context = {
#	"test": ds
#}

# Create your views here.
def dicomviewer(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():	
				try:
					ts = pydicom.dcmread(request.FILES['file'])
					ds = {

						'error' 	: 'DICOM Headers',
						'name'		: ts[0x10,0x10].value,
						'StudyDate'	: ts[0x08, 0x12].value,
						'SOPUID' 	: ts[0x08, 0X18].value,
						'Accession' : ts[0x08, 0x50].value,
						'PatientID' : ts[0x10, 0x20].value,
						'Institute' : ts[0x08, 0x80].value,
					   	'StudInsUID': ts[0x20, 0x0d].value,
					   	'SerInsUID'	: ts[0x20, 0x0e].value

					}
					return render(request,'dicomprocess/processed.html', ds)

				except pydicom.errors.InvalidDicomError:
					ds = {
						'error'     : 'Invalid File!',
						'name'		: 'Not a valid DICOM file',
						'StudyDate'	: 'Not a valid DICOM file',
						'SOPUID' 	: 'Not a valid DICOM file',
						'Accession' : 'Not a valid DICOM file',
						'PatientID' : 'Not a valid DICOM file',
						'Institute' : 'Not a valid DICOM file',
					   	'StudInsUID': 'Not a valid DICOM file',
					   	'SerInsUID'	: 'Not a valid DICOM file'

					}
					return render(request,'dicomprocess/processed.html', ds)
			
		else: 
			return render(request,'dicomprocess/dicomprocess.html', {'form': UploadFileForm})
	else:
		return render(request,'dicomprocess/dicomprocess.html', {'form': UploadFileForm})




