<style>
    .captime {
        font-size: 20vh;
        color: white;
    }
    .capchtimer {
        display: none;
    }

    @media (max-aspect-ratio: 1/1) {
        .dynamic-container {
            width: 95%;
            max-width: 70vh;
        }
    }
    @media (min-aspect-ratio: 1/1) {
        .dynamic-container {
            width: 60%;
            max-width: 70vh;
        }
    }
</style>

<script lang="ts">
    import Loading from "./Loading.svelte";

    import { browser } from "$app/environment";
    import { onDestroy, onMount } from "svelte";
    import { user_data } from '$lib/store';
    import { goto } from "$app/navigation";

    let videoSource: HTMLVideoElement;
    let canvasElement: HTMLCanvasElement;
    let stream: MediaStream;
    let reqNum = 0;

    // 0 : 평소 상태
    // 1 : 찍기 직전
    // 2 : 멈춤
    let status = 0;
    let ctx: CanvasRenderingContext2D;

    const framepath = $user_data.design_num.split('-')[0]

    console.log($user_data);
    

    let canvasSize = { width: 0, height: 0 }

    let camStreame = false

    let capture: string[] = [];

    let captime = 0;

    let cur = 0;
    const TERM = 4000;
    const WAIT = 2000;

    let ranNum = 0

    // class display 판단 ture -> none | false -> black
    let capchtimer = true;

    onMount(() => {
        loop();

        // 사진 촬영 시작
        cur = Date.now() + TERM;
        status = 1;
        capchtimer = false;
    });

    onDestroy(() => {
        if (!browser) return;
        cancelAnimationFrame(reqNum);
        if (stream) stream.getTracks().forEach(v => stream.removeTrack(v));
    });

    $: if (videoSource && videoSource.paused) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(m => {
                stream = m;
                videoSource.srcObject = m;
                return videoSource.play();
            })
            .then(() => {
                console.log('잘 플레이됨');
                camStreame = true
            });
    }

    $: if (canvasElement && !ctx && browser) {
        let temp = canvasElement.getContext('2d');
        if (temp) ctx = temp;
    }

    let overlayImage: HTMLImageElement | null = null;

    $ : {
        if (browser && overlayImage) {
            update();
        }
    }

    const update = () => {
        if (!videoSource || !canvasElement || !ctx) return;

        // 비디오 데이터의 이미지 그리기
        let value = $user_data.cropp_size;
        let [m, n] = value.split(':').map(Number);
        if (isNaN(m) || isNaN(n) || m < 1 || n < 1) {
            m = 1;
            n = 1;
        }

        let { width, height } = calculateCroppedSize(videoSource.videoWidth, videoSource.videoHeight, m, n);
        canvasElement.width = width;
        canvasElement.height = height;
        ctx.setTransform(-1, 0, 0, 1, width, 0);
        ctx.drawImage(videoSource, (videoSource.videoWidth - width) / 2, (videoSource.videoHeight - height) / 2, width, height, 0, 0, width, height);
        ctx.setTransform(1, 0, 0, 1, 0, 0);

        // PNG 투명 이미지 그리기
        if (overlayImage) {
            ctx.drawImage(overlayImage, 0, 0, width, height);
        }
    };

    // PNG 투명 이미지 로드
    const loadOverlayImage = (src: string) => {
        overlayImage = new Image();
        overlayImage.src = src;
        overlayImage.onload = () => {
            update();
        };
    };

    const loop = () => {
        if (capture.length > 5) {
            user_data.set({ ...$user_data, capture_imgs: capture });
            goto('/select_imgs', {
                replaceState: true
            })
            return;
        }
        if (!ctx || !videoSource || videoSource.paused || !canvasElement) {
            reqNum = requestAnimationFrame(loop);
            return;
        }

        if (status === 1) {
            capchtimer = false;
            
            if (capture.length + 1 < 5 && $user_data.cover){
                loadOverlayImage(`/frame/${framepath}/cover_imgs/${capture.length + 1}.png`);
                console.log(1);
            } else if (capture.length + 1 >= 5 && $user_data.cover){
                loadOverlayImage(`/frame/${framepath}/cover_imgs/${ranNum}.png`);
            }
            captime = Math.abs(Math.floor((Date.now() - cur) / 1000));
        } else if (status === 2 || captime - 1 <= 0) {
            capchtimer = true;
        }

        if (status === 2) {
            if (Date.now() - cur <= 0) {
                reqNum = requestAnimationFrame(loop);
                return;
            }

            if (capture.length + 1 >= 5 && $user_data.cover){
                ranNum = Math.floor(Math.random() * 4) + 1
            }
            
            status = 1;
            cur = Date.now() + TERM;
        }

        update();

        if (status === 1 && Date.now() - cur > 0) {
            canvasElement.toBlob(blob => {
                if (!blob) return;
                const reader = new FileReader();
                reader.readAsDataURL(blob);
                reader.onloadend = () => {
                    let base64Data = reader.result as string
                    base64Data = base64Data.replace(/^data:image\/(png|jpeg|jpg);base64,/, '');
                    capture = [...capture, base64Data];
                };
            }, 'image/jpeg');

            cur = Date.now() + WAIT;
            status = 2;
        }

        reqNum = requestAnimationFrame(loop);
    };

    const calculateCroppedSize = (W: number, H: number, m: number, n: number) => {
        let newWidth: number;
        let newHeight: number;

        const currentRatio = W / H;
        const targetRatio = m / n;

        if (currentRatio > targetRatio) {
            newWidth = Math.floor(H * targetRatio);
            newHeight = H;
        } else {
            newWidth = W;
            newHeight = Math.floor(W / targetRatio);
        }

        return { width: newWidth, height: newHeight };
    };
</script>

<div class="relative dynamic-container p-6 bg-white rounded-lg shadow-lg">
    {#if !camStreame}
        <Loading />
    {/if}
    <video bind:this={videoSource} class="hidden"><track kind="captions"></video>
    {#if videoSource}
        <canvas bind:this={canvasElement} class="w-full h-auto rounded-lg shadow-md mb-4"></canvas>
        <div class="font-normal text-gray-700 dark:text-gray-400 text-center">
            {6 - capture.length > 1 ? 6 - capture.length : 'Last'} Chance
        </div>
        <div class="absolute inset-0 flex items-center justify-center">
            <div class="text-white text-4xl font-bold captime" class:capchtimer>{Math.max(captime - 1, 0)}</div>
        </div>
    {/if}
</div>
