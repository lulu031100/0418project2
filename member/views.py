from django.views import generic
from .models import Member
from .forms import SearchForm

class IndexView(generic.ListView):
    model = Member
    template_name = 'member/member_list.html'
    paginate_by = 5                           # 追加　この数字が1ページに表示する件数

    # テンプレートで使用する検索フォームの context を定義
    def get_context_data(self):
        # 全ての辞書データを取得
        context = super().get_context_data()
        # form を辞書に登録
        context['form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        # 使用するフォーム
        form = SearchForm(self.request.GET)
        # 不要であるが、使用しないと cleaned_data が使えないので
        form.is_valid()

        # 全ての学生を取得
        queryset = super().get_queryset()

        # 検索条件を取得
        student_meta = form.cleaned_data['student_meta']
        # 学年クラスで絞り込み
        if student_meta:
            queryset = queryset.filter(student_meta=student_meta)

        # 検索条件を取得
        club = form.cleaned_data['club']
        # 部活で絞り込み
        if club:
            queryset = queryset.filter(club=club)

        # 絞り込みした結果を返す
        return queryset