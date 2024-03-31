<script lang="ts">
    import {browser} from "$app/environment";
    import {onDestroy, onMount} from "svelte";

    let videoSource: HTMLVideoElement;
    let canvasElement: HTMLCanvasElement;
    let stream: MediaStream
    let value = '4:5'
    // let capturedImage: string | null = null;
    let camShow = false
    let reqNum = 0
    let ctx:CanvasRenderingContext2D

    let imgData: ImageData[] = []

    let capture = false

    let cur = 0
    onMount(() => {
        loop()
    })

    onDestroy(() => {
        if (!browser)  return
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

    const loop = () => {
        if(ctx && cur && Date.now() - cur < 0){
            cur = Date.now() + 2000
            console.log(ctx.getImageData(0, 0, canvasElement.width, canvasElement.height));
            reqNum = requestAnimationFrame(loop)
            return
        }

        if (!videoSource || videoSource.paused || !canvasElement) {
            reqNum = requestAnimationFrame(loop)
            return
        }

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
        <button class="h-40 w-80 rounded bg-gray-800 text-white text-8xl" on:click={() => camShow = !camShow}>Start</button>
    {:else}
        <!-- <input type="text" bind:value={value}> -->
        <!-- svelte-ignore a11y-media-has-caption -->
        <video bind:this={videoSource} class="hidden"></video>
        <canvas bind:this={canvasElement} class=" h-5/6"></canvas>
        <button on:click={() => {
            cur = Date.now()
        }}>capture</button>
    {/if}
</main>