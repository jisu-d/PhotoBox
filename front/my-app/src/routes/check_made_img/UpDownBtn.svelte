<script>
    import { writable } from 'svelte/store';
    import { user_data } from '$lib/store'

    const max = 5
    const min = 1
    
    function createCount() {
        const { subscribe, update } = writable(1);
        return {
            subscribe,
            increment: () => update((n) => (n < max ? n + min : n)),
            decrement: () => update((n) => (n > min ? n - min : n)),
        };
    }
    
    const count = createCount();;
    $: user_data.set({ ...$user_data, printoutNum: $count})
</script>

<form class="h-full">
    <div class="relative flex items-center h-full">
        <button type="button" on:click={count.decrement} id="decrement-button" data-input-counter-decrement="quantity-input" class="bg-gray-100  hover:bg-gray-200 border border-gray-300 rounded-s-lg py-3 px-[1.5vh] h-full focus:ring-gray-100 focus:ring-2 focus:outline-none">
            <svg class="w-3 h-3 text-gray-900 " aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 2">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1h16"/>
            </svg>
        </button>
        <input type="text" bind:value={$count} id="quantity-input" data-input-counter aria-describedby="helper-text-explanation" class="bg-gray-50 h-full text-center border-y-[1px] border-gray-300 text-gray-900 text-[1.5vh] focus:ring-blue-500 focus:border-blue-500 block w-full py-2.5" required />
        <button type="button" on:click={count.increment} id="increment-button" data-input-counter-increment="quantity-input" class="bg-gray-100 hover:bg-gray-200 border border-gray-300 rounded-e-lg py-3 px-[1.5vh] h-full focus:ring-gray-100 focus:ring-2 focus:outline-none">
            <svg class="w-3 h-3 text-gray-900 " aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
            </svg>
        </button>
    </div>
</form>