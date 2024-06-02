<script lang="ts">
    import type { MADE_DATE, COLLAGE_IMG_DATE } from '$lib/public/type';
    import { user_data } from '$lib/store';

    import { onMount } from 'svelte';

    let data: COLLAGE_IMG_DATE | null = null;

    let error: unknown | null = null;

    const madeInfo: MADE_DATE = {
        title: $user_data.design_num,
        select_imgs: [$user_data.capture_imgs[$user_data.select_imgs_num[0]], $user_data.capture_imgs[$user_data.select_imgs_num[1]], $user_data.capture_imgs[$user_data.select_imgs_num[2]], $user_data.capture_imgs[$user_data.select_imgs_num[3]]],
    }

    onMount(async () => {
        try {
            const response = await fetch('http://localhost:8000/createCollage', {
            // const response = await fetch('https://pgxx9fwk-8000.asse.devtunnels.ms/createCollage', {

                method: 'POST',
                headers:{
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(madeInfo)
            });
            data = await response.json();
        } catch (err) {
            error = err
        }
    });
</script>

<style>
     @media (max-aspect-ratio: 1/1) {
        .dynamic-img {
            max-width: 55vh;
        }
    }
    @media (min-aspect-ratio: 1/1) {
        .dynamic-img {
            max-width: 50vh;
        }
    }

    .error {
        color: red;
    }
</style>


{#if error}
    <p class="error">{error}</p>
{:else if data == null}
    <div class="py-32">
        <div class="px-3 py-1 text-xs font-medium leading-none text-center text-blue-800 bg-blue-200 rounded-full animate-pulse ">Create image....</div>
    </div>
{:else if data}
    <img src={'data:image/jpeg;base64,' + data.collage_img} class="dynamic-img shadow-lg "  alt="">
{/if}
