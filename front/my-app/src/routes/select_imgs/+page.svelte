<script>
    import ImageGroup from './ImageGroup.svelte'
    import Button from './Button.svelte';
</script>

<style>
    @media (max-aspect-ratio: 1/1) {
        .dynamic-container {
            width: 47vh;
            /* max-width: 45vh; */
            /* 이 부분 컴퓨터 로 하면 너무 큰데 높이가 2000 넘어가면 이상해서 이렇게 둠 */
        }
    }
    @media (min-aspect-ratio: 1/1) {
        .dynamic-container {
            max-width: 95vh;
        }
    }
</style>


<main class="flex flex-col items-center justify-evenly h-full" >
    <div class=" bg-white dynamic-container border border-gray-200 rounded-lg shadow sm:p-8">
        <h5 class="mb-8 text-[3vh] text-center font-bold text-gray-900">Please select four photos</h5>
        <ImageGroup />
        <Button />
    </div>
</main>

