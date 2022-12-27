from django.shortcuts import render, HttpResponse
import openpyxl
from . models import FilesUpload
from .helper import parse, parse2
import os, glob

# import openpyxl
def home(request):
    if request.method=="POST":
        files = glob.glob('./media/*')
        for f in files:
            os.remove(f)

        file2=request.FILES["file"]
        document = FilesUpload.objects.create(file=file2)
        document.save()

        files = glob.glob('./media/*.xlsx')
        t = [0]*5
        check_values = request.POST.getlist('v')
        for x in check_values:
            t[int(x)-1]=1;
        # wb = openpyxl.load_workbook(file2)
        #
        # # getting a particular sheet by name out of many sheets
        # worksheet = wb["Sheet1"]
        # print(worksheet)
        #
        # excel_data = list()
        # # iterating over the rows and
        # # getting value from each cell in row
        # for row in worksheet.iter_rows():
        #     row_data = list()
        #     for cell in row:
        #         row_data.append(str(cell.value))
        #     excel_data.append(row_data)



        excel_dat1 = parse(files[0], t[0], t[1], t[2], t[3], t[4])
        excel_dat1 = excel_dat1.values.tolist()
        # excel_dat.append(check_values)

        excel_dat2 = parse2(files[0], t[0], t[1], t[2], t[3], t[4])
        excel_dat2 = excel_dat2.values.tolist()

        excel_dat=[excel_dat2, excel_dat1]
        # excel_dat = excel_dat.values.tolist()

        ata2=['Tribe', 'Incidence', 'Intensity', 'TDI']
        ata1=['Serial_no', 'Latitude', 'Longitude', 'House_no', 'Village_name', 'Score']

        excel_dat1.insert(0,ata2)
        excel_dat2.insert(0,ata1)


        documents = FilesUpload.objects.all()

        for file in documents:
            file.delete()



        return render(request, "index.html", {"excel_dat":excel_dat})
    return render(request, "index.html")

# Create your views here.
