# 基于Flask轻博客开发：
## 基本功能
	目前实现了简单的用户认证，邮箱确认，用户角色，用户资料编辑，博客文章，用户评论，用户互动（相互关注）的功能，
	可以访问[运行](http://119.29.234.113:5000/auth/login)查看运行效果

## 项目结构
	>app      	      
	>>__init__.py		app初始化
	
	>>auth				登录蓝本
	>>>__init__.py		创建登录蓝图
	>>>forms.py			创建登录表单类，包括LoginForm，RegistrationForm
	>>>views.py			创建登录视图，包括login()，loginout()，register()，confire()

	>>decorators.py		定义一个permission的装饰器
	>>email.py			定义异步发送邮件函数，主要用于注册时的邮件确认

	>>main				主页蓝本
	>>>__init__.py		创建主页蓝本
	>>>error.py			定义访问错误的http状态码
	>>>forms.py			主页表单，包括EditProfileForm，EditProfileAdminForm，PostForm，CommentForm
	>>>views.py			主页视图，index()，post(id)，edit(id)，delete(id)，edit_profile()等
	
	>>models.py			定义数据库的类，主要包括用户类User,角色类Role,博客类Post和评论类Comment

	>>static			静态视图
	>>>favicon.ico

	>>templates			模板主目录
	>>>403.html			返回http状态码
	>>>404.html
	>>>500.html
	>>>_comments.html	显示评论子模板
	>>>_macros.html		页码设置子模板
	>>>_posts.html		显示博客内容子模板
	>>>auth				登录模板目录,包括登录，注册，未确认，发送确认邮件模板
	>>>base.html		显示的基模板，其他模板都是继承自它
	>>>edit_post.html	博客编辑模板
	>>>follewrs.html	关注与被关注者显示模板
	>>>index.html		博客主页
	>>>mail				邮箱模板(暂时没用到,测试邮箱发送时用)
	>>>moderate.html	评论管理模块
	>>>post.html		个人博客或单篇博客显示主模块
	>>>user.html		用户信息显示模块

	>config.py			配置文件,设置工作状态和邮件信息和常量的设置

	>data-dev.sqlite	Flask—SALAchemy数据库
	
	>manage.py			程序启动模块
	
	>migrations			数据库迁移仓库
	
    




