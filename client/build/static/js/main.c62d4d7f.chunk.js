(this.webpackJsonpclient=this.webpackJsonpclient||[]).push([[0],{29:function(e,a,t){e.exports=t(50)},34:function(e,a,t){},36:function(e,a,t){},50:function(e,a,t){"use strict";t.r(a);var n=t(0),r=t.n(n),o=t(12),l=t.n(o),s=(t(34),t(35),t(36),t(13)),c=t(4),i=t(52),m=t(53),u=t(57),d=t(54),p=t(55),h=t(56),f=t(10),E=t(11),g=t(15),b=t(18),w=t.n(b),v=t(27),N=function(){var e=Object(v.a)(w.a.mark((function e(a){var t,n,r,o,l,s=arguments;return w.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=s.length>1&&void 0!==s[1]?s[1]:{},e.next=3,fetch(a,t);case 3:return n=e.sent,e.next=6,n;case 6:return r=e.sent,e.next=9,n.json();case 9:if(o=e.sent,r.ok&&o.success){e.next=14;break}throw new Error("\n"+o.message);case 14:null!==(l=r.headers.get("x-access-tokens"))&&(console.log(l),localStorage.setItem("token",l));case 16:return e.abrupt("return",o);case 17:case"end":return e.stop()}}),e)})));return function(a){return e.apply(this,arguments)}}();var y=function(){var e=Object(n.useState)({username:"",password:""}),a=Object(g.a)(e,2),t=a[0],o=a[1],l=Object(c.f)(),s=function(e){var a=e.target,t=a.id,n=a.value;o((function(e){return Object(E.a)(Object(E.a)({},e),{},Object(f.a)({},t,n))}))};return r.a.createElement("form",{className:"needs-validation",onSubmit:function(e){e.preventDefault(),e.stopPropagation(),e.target.checkValidity()&&N("https://www.noahtigner.com/auth/api-login",{method:"POST",body:JSON.stringify({username:t.username,password:t.password}),headers:{"Content-Type":"application/json"}}).then((function(e){console.log("success: ",e),l.push("/")})).catch((function(e){console.log(e),alert(e)})),e.target.classList.add("was-validated")},noValidate:!0},r.a.createElement("h3",null,"Login"),r.a.createElement("div",{className:"form-group"},r.a.createElement("label",null,"Username"),r.a.createElement("input",{type:"text",className:"form-control",id:"username",placeholder:"Enter Username",value:t.username,onChange:s,required:!0})),r.a.createElement("div",{className:"form-group"},r.a.createElement("label",null,"Password"),r.a.createElement("input",{type:"password",className:"form-control",id:"password",placeholder:"Enter password",value:t.password,onChange:s,required:!0})),r.a.createElement("br",null),r.a.createElement("button",{type:"submit",className:"btn btn-primary btn-block"},"Submit"))};var O=function(){var e=Object(n.useState)({username:"",email:"",password:"",confirmPassword:""}),a=Object(g.a)(e,2),t=a[0],o=a[1],l=Object(c.f)(),s=function(e){var a=e.target,t=a.id,n=a.value;o((function(e){return Object(E.a)(Object(E.a)({},e),{},Object(f.a)({},t,n))}))};return r.a.createElement("form",{className:"needs-validation",onSubmit:function(e){e.preventDefault(),e.stopPropagation(),e.target.checkValidity()&&N("https://www.noahtigner.com/auth/api-register",{method:"POST",body:JSON.stringify({username:t.username,password:t.password}),credentials:"same-origin",headers:{"Content-Type":"application/json"}}).then((function(e){console.log("success: ",e),l.push("/auth/login")})).catch((function(e){console.log(e),alert(e)})),e.target.classList.add("was-validated")},noValidate:!0},r.a.createElement("h3",null,"Register"),r.a.createElement("div",{className:"form-group"},r.a.createElement("label",null,"Username"),r.a.createElement("input",{type:"text",className:"form-control",id:"username",placeholder:"Enter Username",value:t.username,onChange:s,required:!0})),r.a.createElement("div",{className:"form-group"},r.a.createElement("label",null,"Email"),r.a.createElement("input",{type:"email",className:"form-control",id:"email",placeholder:"Enter Email",value:t.email,onChange:s,required:!0})),r.a.createElement("div",{className:"form-group"},r.a.createElement("label",null,"Password"),r.a.createElement("input",{type:"password",className:"form-control",id:"password",placeholder:"Enter Password",value:t.password,onChange:s,required:!0})),r.a.createElement("div",{className:"form-group"},r.a.createElement("label",null,"Confirm Password"),r.a.createElement("input",{type:"password",className:"form-control",id:"confirmPassword",placeholder:"Enter Password",value:t.confirmPassword,onChange:s,pattern:t.password,required:!0}),r.a.createElement("div",{className:"invalid-feedback"},"Passwords must match")),r.a.createElement("br",null),r.a.createElement("button",{type:"submit",className:"btn btn-primary btn-block"},"Submit"))};var j=function(){return r.a.createElement(s.a,null,r.a.createElement(i.a,{color:"inverse",light:!0,expand:"md"},r.a.createElement(m.a,{href:"/auth/login"},"noahtigner.com"),r.a.createElement(u.a,{isOpen:!0,navbar:!0},r.a.createElement(d.a,{className:"ml-auto",navbar:!0},r.a.createElement(p.a,null,r.a.createElement(h.a,{href:"/auth/login"},"Login")),r.a.createElement(p.a,null,r.a.createElement(h.a,{href:"/auth/register"},"Register"))))),r.a.createElement("div",{className:"auth-wrapper"},r.a.createElement("div",{className:"auth-inner"},r.a.createElement(c.c,null,r.a.createElement(c.a,{exact:!0,path:"/auth",component:y}),r.a.createElement(c.a,{path:"/auth/login",component:y}),r.a.createElement(c.a,{path:"/auth/register",component:O})))))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));l.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(j,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[29,1,2]]]);
//# sourceMappingURL=main.c62d4d7f.chunk.js.map