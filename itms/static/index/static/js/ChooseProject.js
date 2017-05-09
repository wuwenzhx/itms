function choose_project(pname){
	var project=['dpdk','spdk','waikiki'];

	document.write('<select name="'+pname+'">');
	document.write('<option value="">Choose Project</option>');
	for(var i=0;i<project.length;i++){
		document.write('<option value="'+project[i]+'">'+project[i]+'<option>');
	}
	documrnt.write("</select>");   
}
	
