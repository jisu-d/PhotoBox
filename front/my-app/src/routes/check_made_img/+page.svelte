<script lang="ts">
    import { onMount } from 'svelte';
    import UpDownBtn from "./UpDownBtn.svelte";
    import PrintBtn from "./PrintBtn.svelte";
    import MadeImg from "./MadeImg.svelte";
    import { user_data } from '$lib/store';
    import { goto } from '$app/navigation';
    
    onMount(() => {
        if($user_data.select_imgs_num.length !== 4){
            alert('정상적인 접근이 아닙니다.')
            goto('/start_page', {
                replaceState: true
            })
        }
    })
</script>

<div class="bg-white border border-gray-200 rounded-lg shadow p-8 flex flex-col ">
    <div class="mb-3 w-full flex justify-evenly">
        <MadeImg />
    </div>
    <div class="flex space-x-4 items-center">
        <UpDownBtn />
        <PrintBtn />
    </div>
    <p id="helper-text-explanation" class="mt-2 text-sm text-gray-500 dark:text-gray-400">Please enter the number of pages you want to print and press the print button.</p>
</div>