<script lang="ts">
    import { goto } from '$app/navigation';
    import { user_data } from '$lib/store'
    import type { PRINTOUT_INFO } from '$lib/public/type';
    async function onClick(){
        if ($user_data.printoutNum <= 0) return
        goto('/print_wait', {
            replaceState: true
        });

        const printout_info: PRINTOUT_INFO = {
            printoutNum: $user_data.printoutNum,
            path: $user_data.imgPath
        }

        const response = await fetch('http://localhost:8000/printImgs', {
                method: 'POST',
                headers:{
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(printout_info)
            });
        const data = await response.json();
    }
</script>

<button type="submit" on:click={onClick} class=" h-full w-3/4 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-3">Print now</button>
