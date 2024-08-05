<script lang="ts">
    import { onMount } from 'svelte';
    import { user_data } from '$lib/store'
    import { goto } from '$app/navigation';

    let number = $user_data.printoutNum;
    let message = 'Printing';
    let dots = '';
    let intervalId: number | undefined;
    let timeoutId: number | undefined;

    console.log(number);
    
    

    function startPrintMessage() {
        const duration = number * 30;  // 90초

        // Reset dots
        dots = '';
        
        // Clear any existing intervals or timeouts
        if (intervalId) clearInterval(intervalId);
        if (timeoutId) clearTimeout(timeoutId);
        
        intervalId = setInterval(() => {
            if (dots.length < 8) {
                dots += '.';
            } else {
                dots = '';
                message = '프린트중';
            }
        }, 500);


        timeoutId = setTimeout(() => {
            clearInterval(intervalId);
            message = '';
            goto('/start_page', {
                replaceState: true
            });
        }, duration * 1000);
    }

    onMount(() => {
        startPrintMessage();
    });
</script>

<main class="flex items-center justify-evenly h-full">
    <div class="bg-white border border-gray-200 rounded-lg shadow p-8 flex flex-col ">
        {#if message}
            <p class="text-4xl font-bold tracking-tight text-gray-900">{message}{dots}</p>
        {/if}
    </div>
</main>