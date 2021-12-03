from django.shortcuts import render, get_object_or_404
from .models import Post,Category,Tag,Link
from django.views.generic import ListView, DetailView
from pure_pagination.mixins import PaginationMixin

class IndexView(PaginationMixin,ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 15

# def index(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})

class PostDetailView(DetailView):
    # 这些属性的含义和 ListView 是一样的
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super().get(request, *args, **kwargs)

        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()

        # 视图必须返回一个 HttpResponse 对象
        return response

# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.increase_views()
#     return render(request, 'blog/detail.html', context={"post": post})

def about(request):
    return render(request, 'blog/about.html')

class LinkView(ListView):
    model = Link
    template_name = 'blog/link.html'
    context_object_name = 'link_list'

# def link(request):
#     return render(request, 'blog/link.html')

def category(request):
    cate_list = Category.objects.all()
    post_list=[]
    for i in cate_list:
        dic={}
        lis = Post.objects.filter(category=i).order_by('-created_time')
        dic[i]=lis
        post_list.append(dic)
    return render(request, 'blog/category.html', context={'post_list': post_list})

def tag(request):
    tag_name_list = Tag.objects.all()
    tag_list=[]
    for i in tag_name_list:
        dic={}
        lis = Post.objects.filter(tags=i)
        dic[i]=str(len(lis)*5+15)
        tag_list.append(dic)
    return render(request, 'blog/tag.html', context={'tag_list': tag_list})

class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(category=cate)

# def category_match(request,pk):
#     cate = get_object_or_404(Category, pk=pk)
#     post_list = Post.objects.filter(category=cate).order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})

class TagView(IndexView):
    def get_queryset(self):
        t = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(tags=t)

# def tag_match(request,pk):
#     t = get_object_or_404(Tag, pk=pk)
#     post_list = Post.objects.filter(tags=t).order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})
