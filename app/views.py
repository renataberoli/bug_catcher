from django.shortcuts import render, get_object_or_404, redirect
from .models import Issue
from .forms import IssueForm
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def issue_list(request):
    search_argument = request.GET.get("data")
    priority = request.GET.get("priority")
    status = request.GET.get("status")
    label = request.GET.get("label")
    assigned = request.GET.get("assigned")

    if not request.GET:
        queryset = Issue.objects.filter(status="open").order_by("priority")

    else:
        queryset = Issue.objects.all()

    if search_argument:
        search_data = request.GET.get('data')
        queryset = queryset.filter(title__icontains=search_data)

    if priority:
        queryset = queryset.filter(priority=priority)

    if status:
        queryset = queryset.filter(status=status)

    if label:
        queryset = queryset.filter(label=label)

    if assigned:
        queryset = queryset.filter(assignee=assigned)

    paginator = Paginator(queryset, 10)

    issue_data = Issue.objects.all()
    users = []
    for issue in issue_data:
        user_assigned = issue.assignee
        if user_assigned not in users:
            users.append(issue.assignee)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'issue/issues_list.html', {'page_obj': page_obj, 'users': users})


def issue_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    return render(request, 'issue/issue_detail.html', {'issue': issue})


def issue_new(request):
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.author = request.user
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

