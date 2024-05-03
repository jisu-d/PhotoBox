<script lang="ts">
    import {browser} from "$app/environment";
    import {onDestroy, onMount} from "svelte";
    import { user_data } from '$lib/store'

    let videoSource: HTMLVideoElement;
    let canvasElement: HTMLCanvasElement;
    let stream: MediaStream
    // let camShow = false
    let camShow = true
    let reqNum = 0

    // 0 : 평소 상태
    // 1 : 찍기 직전
    // 2 : 멈춤
    let status = 0
    let ctx:CanvasRenderingContext2D

    let capture:string[] = []

    let captime = 0

    let cur = 0
    const TERM = 4000
    const WAIT = 2000

    // class display 판단 ture -> none | false -> black
    let capchtimer = true

    onMount(() => {
        loop()
    })

    onDestroy(() => {
        if (!browser) return
        cancelAnimationFrame(reqNum)
        if (stream) stream.getTracks().forEach(v => stream.removeTrack(v))
    })
    


    $: if (camShow && videoSource && videoSource.paused) {
        navigator.mediaDevices.getUserMedia({video: true})
            .then(m => {
                stream = m
                videoSource.srcObject = m
                return videoSource.play()
            })
            .then(() => {
                console.log('잘 플레이됨')
            })
    }

    $:if (canvasElement && !ctx && browser){
        let temp = canvasElement.getContext('2d')
        if(temp) ctx = temp
    }

    let update = () => {
        let value = $user_data.cropp_size
        let [ m, n ] = value.split(':').map(Number)
        if(isNaN(m) || isNaN(n) || m < 1 || n < 1){
            m = 1
            n = 1
        }

        let { width, height } = calculateCroppedSize(videoSource.videoWidth, videoSource.videoHeight, m, n)
        canvasElement.width = width
        canvasElement.height = height
        ctx.setTransform(-1, 0, 0, 1, width, 0)
        ctx.drawImage(videoSource, (videoSource.videoWidth - width) / 2, (videoSource.videoHeight - height) / 2, width, height, 0, 0, width, height)
        ctx.setTransform(1, 0, 0, 1, 0, 0)
    }

    const loop = () => {
        
        if (capture.length > 5) return;
        if(!ctx || !videoSource || videoSource.paused || !canvasElement){
            reqNum = requestAnimationFrame(loop)
            return
        }

        if (status === 1){
            capchtimer = false
            captime = Math.abs(Math.floor((Date.now() - cur) / 1000))
            console.log(captime);
            
        } else if (status === 2 || captime - 1 <= 0){
            capchtimer = true
        }


        if(status === 2){
            if(Date.now() - cur <= 0){
                reqNum = requestAnimationFrame(loop)
                return
            }
            status = 1
            cur = Date.now() + TERM
        }
        
        update()

        if(status === 1 && Date.now() - cur > 0){
            // captime = Math.abs(Math.floor((Date.now() - cur) / 1000))
            canvasElement.toBlob(c => {
                if(!c) return
                capture = [...capture, URL.createObjectURL(c)]
            })
            // capchtimer = false

            cur = Date.now() + WAIT
            status = 2
            
        }

        reqNum = requestAnimationFrame(loop)
    }

    const calculateCroppedSize = (W: number, H: number, m: number, n: number) => {
        let newWidth: number;
        let newHeight: number;

        const currentRatio = W / H;
        const targetRatio = m / n;

        if (currentRatio > targetRatio) {// 이미지의 가로가 더 길 경우
            newWidth = Math.floor(H * targetRatio);
            newHeight = H;
        } else {// 이미지의 세로가 더 길 경우
            newWidth = W;
            newHeight = Math.floor(W / targetRatio);
        }

        return { width: newWidth, height: newHeight};
    }
</script>

<main class="flex flex-col justify-center items-center h-full">
    {#if !camShow}
        <!-- <button class="h-40 w-80 rounded bg-gray-800 text-white text-8xl" on:click={() => camShow = !camShow}>Start</button> -->
    {:else}
        <video bind:this={videoSource} class="hidden"></video>
        <canvas bind:this={canvasElement} class=" h-5/6"></canvas>
        <button on:click={() => {
            cur = Date.now() + TERM
            status = 1
            capchtimer = false
        }}>capture</button>

        <div class="captime" class:capchtimer >{captime - 1}</div>

        <div class="flex justify-center">
            {#each capture as c}
                <img src={c} style="height:100px">
            {/each}
        </div>
    {/if}
</main>


<style>
    .captime{
        position: absolute;
        font-size: 150px;
        color: red;
    }
    .capchtimer {
        display: none;
    }
</style>