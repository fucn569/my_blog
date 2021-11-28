var s_ls = document.getElementsByTagName('svg')
for(var i=0;i<s_ls.length;i++){
      s_ls[i].addEventListener("mouseover", hover);
      s_ls[i].addEventListener("mouseout", recover);
}

function hover() {
  this.setAttribute ("fill","#04c4fb");
}
function recover() {
  this.setAttribute ("fill","#707070");
}

