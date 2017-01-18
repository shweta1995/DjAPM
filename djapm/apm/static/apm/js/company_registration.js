// Company registration Module

	var companyRegister = (function(){
	
		var validateRegistration = function(){
			var formObj = $('#signup_user_35');
			$('#signup_user_35').validate({
				rules:{
					company_name:{required:true},
					company_domain:{required:true,remote:'company/checksubdomain'},
					email:{required:true,email:true,remote:'company/checkemailemail'}
				},
				messages:{
					company_name:{required:"Please enter company name."},
					company_domain:{required:"Please enter company domain.",remote:"Sub-domain already exists"},
					email:{
					required:"Please enter your email address",
					email:"Please enter valid email address",
					remote:"Email already exists."
					}
				}
				
			});
		};
		return {
			validateRegistration:validateRegistration
			
		};
}());

$(document).ready(function(){	
	companyRegister.validateRegistration();
});

