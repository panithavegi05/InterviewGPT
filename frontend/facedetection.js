async function startCamera(){

```
try{

    let video =
        document.getElementById(
            "video"
        );

    let stream =
        await navigator.mediaDevices
        .getUserMedia({
            video: true
        });

    video.srcObject =
        stream;

    document.getElementById(
        "faceStatus"
    ).innerText =
    "Camera Started ✅";

}

catch(error){

    document.getElementById(
        "faceStatus"
    ).innerText =
    "Camera Permission Denied ❌";

}
```

}

window.addEventListener(
"load",
startCamera
);
