from django.shortcuts import render, get_object_or_404, redirect
from .models import Issue
from .forms import IssueForm
from django.utils import timezone
from django.core.paginator import Paginator


def issue_list(request):
    search_argument = request.GET.get("data")
    priority = request.GET.get("priority")
    status = request.GET.get("status")
    label = request.GET.get("label")
    print(priority)

    if search_argument:
        search_data = request.GET.get('data')
        filter_argument = Issue.objects.filter(title__icontains=search_data)
        paginator = Paginator(filter_argument, 10)
    elif priority == "1":
        filter_argument = Issue.objects.filter(priority="1")
        paginator = Paginator(filter_argument, 10)
    elif priority == "2":
        filter_argument = Issue.objects.filter(priority="2")
        paginator = Paginator(filter_argument, 10)
    elif priority == "3":
        filter_argument = Issue.objects.filter(priority="3")
        paginator = Paginator(filter_argument, 10)
    elif priority == "4":
        filter_argument = Issue.objects.filter(priority="4")
        paginator = Paginator(filter_argument, 10)
    else:
        issues = Issue.objects.filter(status="open").order_by('priority')
        paginator = Paginator(issues, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'issue/issues_list.html', {'page_obj': page_obj})


def issue_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    return render(request, 'issue/issue_detail.html', {'issue': issue})


def issue_new(request):
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.creation_date = timezone.now()
            issue.save()
            return redirect('issue_detail', pk=issue.pk)
    else:
        form = IssueForm()
    return render(request, 'issue/issue_edit.html', {'form': form})


def issue_edit(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == "POST":
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.creation_date = timezone.now()
            issue.save()
            return redirect('issue_detail', pk=issue.pk)
    else:
        form = IssueForm(instance=issue)
    return render(request, 'issue/issue_edit.html', {'form': form})


def issue_delete(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == "POST":
        issue.delete()
        return redirect('issue_list')

    return render(request, 'issue/issue_delete.html', {'issue': issue})
