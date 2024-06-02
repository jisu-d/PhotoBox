<script>
    import { goto } from "$app/navigation";
    import { user_data } from "$lib/store"
    import { onMount } from "svelte";

    onMount(() => {
        console.log($user_data);
    })

    function onClick() {
        goto('/ser2', {
            replaceState: true
        })
    }

    function onClick2() {
        user_data.set('ser2')
        console.log($user_data);
    }
</script>

<button on:click={onClick}>click</button>
<button on:click={onClick2}>update</button>