from django.shortcuts import render, get_object_or_404, redirect
from .models import Issue
from .forms import IssueForm
from django.utils import timezone
from django.core.paginator import Paginator


def issue_list(request):
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


