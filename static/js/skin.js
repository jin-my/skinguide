// checkbox 선택한 value값 가져오는 script
function value_check() 
{
    var check_count = document.getElementsByName("chk").length;
    alert('aa');
    for (var i=0; i<check_count; i++) 
    {
        if(document.getElementsByName("chk")[i].checked == true) 
        {
        // alert(document.getElementsByName("chk")[i].value);
        alert('aa');
        }
    }
}

function values(){
    var selected = document.querySelectorAll('input[name="check_skin_type"]:checked');
    var selectedstring = '';
    
    for(var i=0; i<selected.length; i++){
        selectedstring += selected[i].value;
    }
    if (selectedstring.length < 4){
        alert('모두 선택해주세요.');
    }else{
<<<<<<< HEAD
        // alert(selectedstring); stresult -> result
        document.getElementById("result").value = selectedstring;
=======
        // alert(selectedstring);
        document.getElementById("stresult").value = selectedstring;
        document.getElementById('skincheckform').submit()
>>>>>>> d1a726d3994fb67d11c0ce3a8cba7dbb8af5491e
    }
    
}

function productvalue(){
    var check_count = document.getElementsByName("product_check").length;
    
    // var checked = document.querySelectorAll('input[name="product_check"]:checked');
    var checkedstring = '';
    for(var i=0; i<check_count; i++){
        if (document.getElementsByName("product_check")[i].checked == true) {
            checkedstring += document.getElementsByName("product_check")[i].value;
            checkedstring += ', ';
        }
        // checkedstring += checked[i].value;
        
    }
    alert(checkedstring);
}


function dontknow(){
    alert('피부타입 테스트를 진행하세요.');
    location.href='../select';
}

function dontlogin(){
    alert('맞춤형 서비스는 로그인 후 이용 가능 합니다.');
    
}