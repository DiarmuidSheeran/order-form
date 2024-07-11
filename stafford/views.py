import pandas as pd
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .forms import UploadFileForm
from .models import staffordProduct

# Create your views here.
def stafford(request):
    return render(request, 'stafford/stafford-order.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            file_path = fs.path(filename)

            try:
                data = pd.read_excel(file_path)
                for _, row in data.iterrows():
                    product = staffordProduct(
                        name=row['name'],
                        productCode=row['productCode'],
                        weight=row['weight'],
                        barcode=row['barcode'],
                        caseCount=row['caseCount']
                    )
                    product.save()
            except Exception as e:
                messages.error(request, f'Error: {str(e)}')

            return redirect('upload_file')
    else:
        form = UploadFileForm()

    return render(request, 'stafford/stafford-product-upload.html', {'form': form})