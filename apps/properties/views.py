from django.shortcuts import render
from django.views import View

class HomeView(View):
    template_name ='index.html'
    
    def get(self,request):
        return render(request,self.template_name)


class AgentView(View):
    template_name ='agent.html'

    def get(self,request):
        return render(request,self.template_name)


class HouseSaleListView(View):
    template_name ='houselistings.html'

    def get(self,request):
        return render(request,self.template_name)

class HouseRentalListView(View):
    template_name ='rentals.html'

    def get(self,request):
        return render(request,self.template_name)


class WareHouseListView(View):
    template_name ='warehouselistings.html'

    def get(self,request):
        return render(request,self.template_name)


class LandListView(View):
    template_name ='landlistings.html'

    def get(self,request):
        return render(request,self.template_name)


class BlogView(View):
    template_name ='blog.html'

    def get(self,request):
        return render(request,self.template_name)


class ContactView(View):
    template_name ='contact.html'

    def get(self,request):
        return render(request,self.template_name)