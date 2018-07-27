<!DOCTYPE html>
<html>
<head>
   <title>Flight</title>
   <link href="//libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
   <script src="//libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
   <script src="//libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
</head>
<body>

     <div class="container">
	<div class="row clearfix">
		<div class="col-md-12 column">
			<div id="msgArea" class="alert alert-success alert-dismissable">
				 <button class="close" aria-hidden="true" type="button" data-dismiss="alert">×</button>
				<h2>
					Welcom!
				</h2> <info id='infoArea'></info>
			</div>
			<div class="jumbotron">
				<h3>
					Input your e-mail.
				</h3>
				<p>
					<input id="iptEmailId" type="text" class="form-control" placeholder="e-mail">
				</p>
				<p>
					<button type="button" class="btn btn-primary btn-large" onclick="okBtnClick()">OK</button>
				</p>
			</div>
			<div class="panel-group" id="panel-744285">
				<div class="panel panel-default">
					<div class="panel-heading">
						 <a class="panel-title collapsed" href="#panel-element-698385" data-toggle="collapse" data-parent="#panel-744285">About your mail address...</a>
					</div>
					<div class="panel-collapse collapse" id="panel-element-698385">
						<div class="panel-body">
							It will be used to recieve reminder mail, and as a Id to identify you.
						</div>
					</div>
				</div>
				<div class="panel panel-default">
					<div class="panel-heading">
						 <a class="panel-title collapsed" href="#panel-element-727733" data-toggle="collapse" data-parent="#panel-744285">If you can't recieve our mail...</a>
					</div>
					<div class="panel-collapse collapse" id="panel-element-727733">
						<div class="panel-body">
							Add the sender ' chinxk@hotmail.com' to your white-list.
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>

</body>
	<script>
function okBtnClick(){
		var mail = $("#iptEmailId").val();
			if(validMail(mail)){
				//to next
			}else{
				$("#infoArea").text("It's not a valid email :"+mail);
			}
		}
function validMail(mail){
　　var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$"); //正则表达式
　　if(mail === ""){ //输入不能为空
　　　　return false;
　　}else if(!reg.test(mail)){ //正则验证不通过，格式不对
　　　　return false;
　　}else{
　　　　return true;
　　}
}
</script>
</html>