

const body = document.querySelector('body'),
      sidebar = body.querySelector('nav'),
      toggle = body.querySelector(".toggle"),
      searchBtn = body.querySelector(".search-box"),
      modeSwitch = body.querySelector(".toggle-switch"),
      newFolder = body.querySelector("#new-folder"),
      upload =  body.querySelector('#upload'),
      modeText = body.querySelector(".mode-text"),
      createModal =  body.querySelector("#authentication-modal"),
      optionPopup= body.querySelector("#dropdownDots"),
      fileRename =  body.querySelectorAll(".renameFile"),
      folderRename= body.querySelectorAll(".renameFolder"),

      searchInput = body.getElementsByClassName("searchInput").value,
      searchButton = body.querySelector("#search-button"),
      folderPopup =  body.querySelector(".center-div");
    //   closePop =  body.querySelector('#temp');
let   folderIcon = body.querySelectorAll(".folder");
let fileIcon =  body.querySelectorAll(".file");

let counter =0;
const target =  document.getElementById("authentication-modal");
function renameFunction()
{
   
    
    let current_url = window.location.href;
    let toRename = current_url.substring(current_url.lastIndexOf('#')+1);
    let host = current_url.substring(0,current_url.indexOf('/my-files'));
    // console.log("I am the host " +host);
    let formData = new FormData(document.getElementsByClassName('renameForm')[0]); 
    let newName = formData.get('rename');
    let afterRename =  encodeURI(host+toRename+"&rename="+newName);
    console.log("This is the the new url: "+afterRename)
    window.location.href = afterRename;
}
const options =  {
    onHide: () => {
        console.log('modal is hidden');
        document.querySelector('[modal-backdrop]').remove();
    }
};
const modal =  new Modal(target);
fileIcon.forEach(file=> {
    file.addEventListener('click', event =>{
        const target =  document.getElementById("dropdownFile"+file.id.substring(4))
        const trigger = file;
        const dropdown = new Dropdown(target,trigger);
        dropdown.show();
    });
    // counter++;
    // console.log(counter);
})
fileRename.forEach(rename=>{
    rename.addEventListener('click',event=>{
        createModal.innerHTML = '<div class="relative p-4 w-full max-w-md h-full md:h-auto"><div class="relative bg-white rounded-lg shadow dark:bg-gray-700"><button type="button" id="closeModal" class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-800 dark:hover:text-white" data-modal-toggle="authentication-modal"><svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg><span class="sr-only">Close modal</span></button><div class="py-6 px-6 lg:px-8"><h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Rename</h3><form onsubmit="event.preventDefault();renameFunction();" class="space-y-6 renameForm" action="/my-files" method="get"><div><label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Folder name</label><input name="rename" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" type="text" value="Rename" id="form-rename"></div><button  type="submit" class="renameSub w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Rename</button></form></div></div></div>';
        const closeModal =  document.getElementById("closeModal");
        const backdrop = document.getElementsByClassName("bg-gray-900");
        // renameButton = body.querySelector(".renameSub");

        //console.log(renameButton)
        closeModal.addEventListener("click",()=>{
            backdrop[0].style.display = "none";
            modal.hide();
        });
        
    });
})
folderRename.forEach(rename=>{
    rename.addEventListener('click',event=>{
        createModal.innerHTML = '<div class="relative p-4 w-full max-w-md h-full md:h-auto"><div class="relative bg-white rounded-lg shadow dark:bg-gray-700"><button type="button" id="closeModal" class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-800 dark:hover:text-white" data-modal-toggle="authentication-modal"><svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg><span class="sr-only">Close modal</span></button><div class="py-6 px-6 lg:px-8"><h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Rename</h3><form onsubmit="event.preventDefault();renameFunction();" class="space-y-6 renameForm" action="/my-files" method="get"><div><label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Folder name</label><input name="rename" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" type="text" value="Rename" id="form-rename"></div><button  type="submit" class="renameSub w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Rename</button></form></div></div></div>';
        const closeModal =  document.getElementById("closeModal");
        const backdrop = document.getElementsByClassName("bg-gray-900");
        // renameButton = body.querySelector(".renameSub");

        //console.log(renameButton)
        closeModal.addEventListener("click",()=>{
            backdrop[0].style.display = "none";
            modal.hide();
        });
        
    });
})
// console.log(optionPopup);
folderIcon.forEach(folder=> {
    folder.addEventListener('dblclick', event =>{
        let folderChild = folder.children[0].innerHTML;
        let current_url = window.location.href;
        console.log(current_url)
        if ((current_url.indexOf('?')) === -1){
            window.location=window.location.href+"?pathd="+folderChild;
        }
        else{
            console.log("I am the url before all the proccessing "+current_url.substring(0,current_url.indexOf('?')))
            window.location.href = current_url.substring(0,current_url.indexOf('?'))+"?pathd="+folderChild;
            console.log("I am the new url after rename: "+window.location)
        }
        
    })
})

folderIcon.forEach(folder=> {
    folder.addEventListener('click', event =>{
        const target =  document.getElementById("dropdownFolder"+folder.id.substring(6));
        const trigger = folder;
        const dropdown = new Dropdown(target,trigger);
        dropdown.show();
        
    })
})

upload.addEventListener("click",()=>{
    const target =  document.getElementById("authentication-modal");
    
    const modal =  new Modal(target);
    createModal.innerHTML = '<div class="relative p-4 w-full max-w-md h-full md:h-auto"><div class="relative bg-white rounded-lg shadow dark:bg-gray-700"><button type="button" id="closeModal" class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-800 dark:hover:text-white" data-modal-toggle="authentication-modal"><svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg><span class="sr-only">Close modal</span></button><div class="py-6 px-6 lg:px-8"><h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Upload</h3><form enctype="multipart/form-data" method="post" class="space-y-6" action="/upload"><div><input type="file" name="file[]" id="" multiple="" class="block w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 cursor-pointer dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"></div><button name="upload" type="submit" class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Upload</button></form></div></div></div>'
    const closeModal =  document.getElementById("closeModal");
    const backdrop = document.getElementsByClassName("bg-gray-900");
    closeModal.addEventListener("click",()=>{
        backdrop[0].style.display = "none";
        modal.hide();
    });
})
newFolder.addEventListener("click",()=>{
    const target =  document.getElementById("authentication-modal");
    const modal =  new Modal(target);
    // console.log(modal);
    createModal.innerHTML='<div class="relative p-4 w-full max-w-md h-full md:h-auto"><div class="relative bg-white rounded-lg shadow dark:bg-gray-700"><button type="button" id="closeModal" class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-800 dark:hover:text-white" data-modal-toggle="authentication-modal"><svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg><span class="sr-only">Close modal</span></button><div class="py-6 px-6 lg:px-8"><h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Create Folder</h3><form class="space-y-6" action="/my-files" method="post"><div><label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Folder name</label><input name="Folder" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" type="text" value="New Folder" id="form-newFolder"></div><button type="submit" class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Create Folder</button></form></div></div></div>';
    const closeModal =  document.getElementById("closeModal");
    const backdrop = document.getElementsByClassName("bg-gray-900");
    closeModal.addEventListener("click",()=>{
        backdrop[0].style.display = "none";
        modal.hide();
    });
    
})
toggle.addEventListener("click" , () =>{
    sidebar.classList.toggle("close");
})



//  $(document).ready(function() {
//     alert('hi')
//     $('#searchform').on('submit', function(e){
//         $('#searchModal').modal('show');
//         e.preventDefault();
//     });
//   });
   

  


searchBtn.addEventListener("click" , () =>{
    sidebar.classList.remove("close");
})
modeSwitch.addEventListener("click" , () =>{
    let allLinks = body.querySelectorAll(".link")
    body.classList.toggle("dark");
    
    if(body.classList.contains("dark")){
        modeText.innerText = "Light mode";
        allLinks.forEach(link=>{
            link.style.color ='white';
            // console.log(link);
        })
    }else{
        modeText.innerText = "Dark mode";
        allLinks.forEach(link=>{
            link.style.color ='black';
            // console.log(link);
        })
         
    }
});

