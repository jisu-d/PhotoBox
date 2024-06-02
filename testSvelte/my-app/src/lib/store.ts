import { writable, type Writable } from 'svelte/store';

export const user_data: Writable<string> = writable<string>();
