import { writable } from 'svelte/store';

export const user_data = writable({
    design_num: null,
    capture_imgs: [], // 6장의 사진의 데이터를 가진 배열
    select_imgs_num: [], // 배열의 길이가 4개 capture_imgs배열의 이미지 index
    made_img: null,
    cropp_size: '3:4'
});

// count.set(1); // logs '1'
// count.update((n) => n + 1); // logs '2'
// $user_data // 현재 값 불러오기